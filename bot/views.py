from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from bot.models import Bot
from bot.serializers import BotSerializer
from .utils import send_to_openai
from .selectors import BotSelector


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
    
class BotListAPIView(APIView):
    serializer_class = BotSerializer

    def get(self, request):
        bots = BotSelector.get_all_bots()
        serializer = self.serializer_class(bots, many=True)
        return Response(serializer.data)

class BotListBasedOnUserAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = BotSerializer

    def get(self, request):
        bots = BotSelector.get_all_bots_based_on_user(user=request.user.id)
        serializer = self.serializer_class(bots, many=True)

        return Response(serializer.data)