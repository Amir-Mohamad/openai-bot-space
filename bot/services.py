from .models import Bot

class BotService:
    @staticmethod
    def create_bot(user, name, description):
        return Bot.objects.create(user=user, name=name, description=description)

# def access_data(**data):
#     try:
#         return data['name'], data['description']
#     except KeyError as e:
#         return Response({"error": f"Missing key: {e}"}, status=status.HTTP_400_BAD_REQUEST) 