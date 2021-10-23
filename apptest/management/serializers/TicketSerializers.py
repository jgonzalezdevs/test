from rest_framework import serializers
from management.models import Ticket

class TicketSerializer(serializers.ModelSerializer):

    class Meta:

        model = Ticket
        fields = ('title', 'description', 'status', 'start_date', 'created_time')
        read_only_fields = ('id',)