# django
# django rest
from rest_framework.serializers import ModelSerializer

# others
from ..models import User

# serializers


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'