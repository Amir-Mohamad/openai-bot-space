from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .selectors import get_chat_history
from .services import format_chat_history

class ChatHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, bot_id):
        history_queryset = get_chat_history(request.user.id, bot_id)
        formatted_history = format_chat_history(history_queryset)

        return Response(formatted_history)