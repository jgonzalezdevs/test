# django

# django rest
from rest_framework.viewsets import ModelViewSet

from management.filters import TicketsFilter
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import rest_framework as filters

# others
from ..models import Ticket
from ..serializers.TicketSerializers import TicketSerializer
from utils.permissions import DjangoModelPermissionsViewControl

# views


class TicketsViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing law firms.
    """
    model = Ticket
    lookup_field = 'id'
    queryset = model.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [DjangoModelPermissionsViewControl]
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = TicketsFilter
    