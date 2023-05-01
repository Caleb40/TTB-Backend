from rest_framework import viewsets, status
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


class DocumentViewSet(viewsets.ViewSet):
    serializer_class = DocumentSerializer

    def list(self, request):
        user = request.user
        try:
            document = Document.objects.get(user=user)
            serializer = self.serializer_class(document)
            return Response(serializer.data)
        except Document.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        user = request.user
        try:
            Document.objects.get(user=user)
            return Response({'error': 'Document already exists for this user.'}, status=status.HTTP_400_BAD_REQUEST)
        except Document.DoesNotExist:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(user=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        user = request.user
        try:
            document = Document.objects.get(user=user)
            serializer = self.serializer_class(document, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Document.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get_queryset(self):
        user = self.request.user
        return Document.objects.filter(user=user)


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
