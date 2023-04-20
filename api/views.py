from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core_auth.serializers import UserSerializer
from api.serializers import TransactionSerializer, DocumentSerializer
from core_auth.models import User
from ttb_backend.models import Transaction, Document


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = {
            'user': self.request.user.id,
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
        }
        return context

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Document.objects.filter(user=self.request.user)
