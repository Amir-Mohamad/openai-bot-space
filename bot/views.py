from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from bot.models import Bot
from bot.serializers import BotSerializer
from rest_framework import serializers
from .utils import send_to_openai
from .selectors import BotSelector
from .services import BotService


class UserMessageAPIView(APIView):
    class InputSerializer(serializers.Serializer):
        user_message = serializers.CharField(max_length=255)
        
    def post(self, request, bot_id, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data["user_message"]
            

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

class BotCreateAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255)
        description = serializers.CharField(max_length=1024, required=False)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)

        if serializer.is_valid():
            try:
                name = serializer.validated_data["name"]
                description = serializer.validated_data["description"]
            except KeyError as e:
                return Response({"error": f"Missing key: {e}"}, status=status.HTTP_400_BAD_REQUEST)

            bot = BotService.create_bot(
                user=request.user,
                name=name,
                description=description,
            )
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)