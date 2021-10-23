from django.contrib.auth import get_user_model

# django rest
from rest_framework.viewsets import ModelViewSet

# others
from ..serializers.UserSerializers import UserSerializer
from utils.permissions import DjangoModelPermissionsViewControl

# views


class UsersViewset(ModelViewSet):
    """
    A simple ViewSet for viewing and editing users.
    """
    model = get_user_model()
    lookup_field = 'id'
    queryset = model.objects.all()
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissionsViewControl]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context