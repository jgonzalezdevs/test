from django.urls import path, include
from management.views.TicketViews import TicketsViewSet
# jwt
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from management.views.UserViews import UsersViewset
from .simple_jwt.tokenPairs import UserTokenObtainPairView

app_name = 'management'

ticket_list = TicketsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
user = UsersViewset.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('token/', UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('registration/', user, name='create_user'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('ticket/', ticket_list, name='ticket_list_and_creation'),
]