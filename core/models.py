from django.db import models
from common.models import BaseModel

class HistoryDetail(BaseModel):
    role = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.role}: {self.message[:50]}"


class History(BaseModel):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    bot = models.ForeignKey("bot.Bot", on_delete=models.CASCADE)
    history_detail = models.ManyToManyField(HistoryDetail, related_name="history")

    def __str__(self):
        return f"{self.user}: {self.bot}"


