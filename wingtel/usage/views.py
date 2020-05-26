from django.shortcuts import render

# Create your views here.

from rest_framework import mixins, viewsets
from rest_framework.response import Response

from wingtel.usage.models import DataUsageRecord, VoiceUsageRecord
from wingtel.usage.serializers import DataUsageSerializer, VoiceUsageSerializer


class DataUsageViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = DataUsageRecord.objects.all()
    serializer_class = DataUsageSerializer

class VoiceUsageViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = VoiceUsageRecord.objects.all()
    serializer_class = VoiceUsageSerializer
