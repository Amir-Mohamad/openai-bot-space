from bot.models import Bot

class BotSelector:
    @staticmethod
    def get_all_bots():
        return Bot.objects.all()

    @staticmethod
    def get_all_bots_based_on_user(user):
        return Bot.objects.filter(user=user)