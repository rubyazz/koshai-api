from datetime import timedelta

import django_filters.rest_framework as filters
from orders.models import Order


class OrderFilter(filters.FilterSet):
    date_from = filters.DateTimeFilter(method="filter_date_from")
    date_to = filters.DateTimeFilter(method="filter_date_to")

    class Meta:
        model = Order
        fields = ("date_from", "date_to")

    def filter_date_from(self, queryset, _field_name, value):
        if value:
            # TODO take time zone from company and calculate difference hours
            date_from = value - timedelta(hours=6)
            queryset = queryset.filter(created_at__gte=date_from)
        return queryset

    def filter_date_to(self, queryset, _field_name, value):
        if value:
            date_to = value + timedelta(days=1, hours=-6)
            queryset = queryset.filter(created_at__lte=date_to)
        return queryset
