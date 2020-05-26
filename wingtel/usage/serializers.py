from rest_framework import serializers
from wingtel.usage.models import DataUsageRecord, VoiceUsageRecord


class DataUsageSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataUsageRecord
        fields = "__all__"

class VoiceUsageSerializer(serializers.ModelSerializer):

    class Meta:
        model = VoiceUsageRecord
        fields = "__all__"
