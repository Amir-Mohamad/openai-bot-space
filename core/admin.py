from django.contrib import admin
from core.models import History, HistoryDetail

class HistoryDetailAdmin(admin.ModelAdmin):
    list_display = ('role', 'message')
    search_fields = ('role', 'message')


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'bot')
    search_fields = ('user__username', 'bot__name')
    list_filter = ('user', 'bot')


admin.site.register(HistoryDetail, HistoryDetailAdmin)
admin.site.register(History, HistoryAdmin)
