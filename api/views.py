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


# class DocumentViewSet(viewsets.ModelViewSet):
#     queryset = Document.objects.all()
#     serializer_class = DocumentSerializer
#
#     def create(self, request, *args, **kwargs):
#         # Check if a document with the same title already exists
#         title = request.data.get('title')
#         if Document.objects.filter(title=title).exists():
#             return Response({'error': 'Document with the same title already exists.'}, status=400)
#         return super().create(request, *args, **kwargs)
#
#     def update(self, request, *args, **kwargs):
#         # Allow overriding the document with the same title
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         if not partial and instance.title != request.data.get('title'):
#             return Response({'error': 'Title cannot be changed during update.'}, status=400)
#         return super().update(request, *args, **kwargs)
#
#     def list(self, request, *args, **kwargs):
#         # Limit to a single set of document objects
#         queryset = self.filter_queryset(self.get_queryset())
#         if len(queryset) > 1:
#             return Response({'error': 'Only one set of document objects is allowed.'}, status=400)
#         return super().list(request, *args, **kwargs)
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Check if a document with the same user already exists
        user = request.data.get('user')
        if Document.objects.filter(user=user).exists():
            return Response({'error': 'Document with the same user already exists.'}, status=400)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # Allow overriding the document with the same user
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if not partial and instance.user != request.data.get('user'):
            return Response({'error': 'User cannot be changed during update.'}, status=400)
        return super().update(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        # Limit to a single set of document objects
        queryset = self.filter_queryset(self.get_queryset())
        if len(queryset) > 1:
            return Response({'error': 'Only one set of document objects is allowed.'}, status=400)
        return super().list(request, *args, **kwargs)


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
