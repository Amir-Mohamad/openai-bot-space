from django.contrib import admin
from .models import Bot

class BotAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')

admin.site.register(Bot, BotAdmin)