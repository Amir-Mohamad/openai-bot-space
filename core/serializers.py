from rest_framework import serializers
from .models import History, HistoryDetail

class HistoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryDetail
        fields = ['role', 'message']

class HistorySerializer(serializers.ModelSerializer):
    history_detail = HistoryDetailSerializer()

    class Meta:
        model = History
        fields = ['user', 'bot', 'history_detail']