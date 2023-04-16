from rest_framework import viewsets

from api.serializers import UserSerializer
from core_auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
