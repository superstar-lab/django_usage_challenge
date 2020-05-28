from rest_framework import generics
from wingtel.usage.models import UsageRecord
from wingtel.usage.serializers import UsageSerializer, UsageSumSerializer
from django.db.models import F, Sum
from datetime import datetime as dt

# Create your views here.

class UsageList(generics.ListAPIView):
    serializer_class = UsageSerializer
    
    def get_queryset(self):
        try:
            price_limit = int(self.kwargs.get('limit', None))
        except ValueError:
            return []
        return UsageRecord.objects.filter(price__gt=price_limit).annotate(price_exceed=F('price')-price_limit)

class UsageSummary(generics.ListAPIView):
    serializer_class = UsageSumSerializer

    def get_queryset(self):
        try:
            from_date = dt.strptime(self.kwargs['from_date'], '%Y-%m-%d')
            to_date = dt.strptime(self.kwargs['to_date'], '%Y-%m-%d')
            usage_type = self.kwargs['usage_type']
        except ValueError:
            return []
        return UsageRecord.objects.filter(usage_date__range=[from_date, to_date]).values('att_subscription_id', 'sprint_subscription_id').annotate(total_price=Sum('price'), total_usage=Sum('used_units'))
