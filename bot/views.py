from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import send_to_openai

class UserMessageAPIView(APIView):
    def get(self, request, bot_id, *args, **kwargs):
        user_message = "how old are you?"

        if not user_message:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            response = send_to_openai(request.user.id, bot_id, user_message)
            
            return Response({"response": response}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)