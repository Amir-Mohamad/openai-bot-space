from .models import Bot

class BotSerivce:
    @staticmethod
    def create_bot(user, name):
        return Bot.objects.create(user=user, name=name)