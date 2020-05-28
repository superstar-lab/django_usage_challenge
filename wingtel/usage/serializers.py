from rest_framework import serializers
from wingtel.usage.models import UsageRecord

class UsageSerializer(serializers.Serializer):
    att_subscription_id = serializers.CharField()
    sprint_subscription_id = serializers.CharField()
    usage_type = serializers.CharField()
    used_units = serializers.FloatField()
    price = serializers.FloatField()
    price_exceed = serializers.FloatField()

class UsageSumSerializer(serializers.Serializer):
    att_subscription_id = serializers.CharField()
    sprint_subscription_id = serializers.CharField()
    total_price = serializers.FloatField()
    total_usage = serializers.FloatField()
