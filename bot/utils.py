from openai import OpenAI
import os
from dotenv import load_dotenv

from core.models import History, HistoryDetail
import re
from bot.models.bot import Bot
from django.contrib.auth import get_user_model

User = get_user_model()

load_dotenv()


def send_to_openai(user_id, bot_id, message):
    messages = []
    bot = Bot.objects.get(id=bot_id)
    messages.append({"system": bot.description})
    
    user = User.objects.get(id=user_id)
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    system_prompt = {"role": "system", "content": bot.description}
    messages.append(system_prompt)

    history = History.objects.filter(user=user, bot=bot).first()
    if not history:
        history = History.objects.create(user=user, bot=bot)

    history_details = HistoryDetail.objects.filter(history__user__id=user_id, history__bot__id=bot_id)
    
    for detail in history_details:
        messages.append({"role": detail.role, "content": detail.message})

    messages.append({"role": "user", "content": message})

    new_history_obj = HistoryDetail.objects.create(role="user", message=message)
    history.history_detail.add(new_history_obj)

    response = client.chat.completions.create(
        
        model="gpt-4o-mini",
        messages=messages,
    )

    HistoryDetail.objects.create(role="assistant", message=response.choices[0].message.content)

    return response.choices[0].message.content




