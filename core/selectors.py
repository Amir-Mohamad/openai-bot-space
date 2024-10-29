from core.models import History

def get_chat_history(user_id, bot_id):
    return History.objects.filter(user__id=user_id, bot__id=bot_id).prefetch_related('history_detail')
