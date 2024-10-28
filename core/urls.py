from django.urls import path
from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('chat-history/<int:bot_id>/', views.ChatHistoryAPIView.as_view(), name='chat-history'),
]
