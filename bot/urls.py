from django.urls import path
from . import views

app_name = 'bot'

urlpatterns = [
    path('chat/<int:bot_id>/', views.UserMessageAPIView.as_view(), name='chat'),

    # List bot view
    path('bots/', views.BotListAPIView.as_view(), name='bots'),
    # List bot based on user view
    path('bots/user/', views.BotListBasedOnUserAPIView.as_view(), name='bots-user'),
]