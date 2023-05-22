from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import TransactionSerializer, CreditCardSerializer, DocumentSerializer
from core_auth.models import User
from core_auth.serializers import UserSerializer
from ttb_backend.models import Transaction, Document, CreditCard


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
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Check if a document with the same user already exists
        user = request.user
        if Document.objects.filter(user=user).exists():
            return Response({'error': 'Document with the same user already exists.'}, status=400)
        return Document.objects.create(user_id=user.id, *args, **kwargs)


class CreditCardViewSet(viewsets.ModelViewSet):
    serializer_class = CreditCardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CreditCard.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        context = {
            'user': self.request.user.id,
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
        }
        return context
