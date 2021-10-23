import django_filters
from management.models import Ticket

class TicketsFilter(django_filters.FilterSet):

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'status', 'start_date']
