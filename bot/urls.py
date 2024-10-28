from django.urls import path
from . import views

app_name = 'bot'

urlpatterns = [
    path('chat/<int:bot_id>/', views.UserMessageAPIView.as_view(), name='chat'),
]