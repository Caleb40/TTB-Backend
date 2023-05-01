from rest_framework import serializers

from core_auth.models import User
from ttb_backend.models import Transaction, Document, CreditCard


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transaction_id', 'transaction_type', 'status',
                  'channel', 'amount', 'date', 'return_amount',
                  'investment_duration', 'gift_bonus']

        read_only_fields = ['date', 'transaction_id']

    def create(self, validated_data):
        user = User.objects.get(id=self.context['user'])
        return Transaction.objects.create(user=user, **validated_data)


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Document
        read_only_fields = ['user']

    # def create(self, validated_data):
    #     # Check if a document already exists for the user
    #     user = self.context['user']
    #     document = Document.objects.filter(user_id=user).first()
    #     if document:
    #         # Update the existing document
    #         Document.objects.filter(user_id=user).update(**validated_data)
    #         # Retrieve the updated object
    #         document = Document.objects.get(user_id=user)
    #         return document
    #     # Otherwise, create a new document
    #     return Document.objects.create(user_id=user, **validated_data)
    #

class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = [
            'cardholders_name', 'card_number', 'expiry_date',
            'cvv', 'billing_address'
        ]

    def create(self, validated_data):
        user = self.context['user']
        credit_card = CreditCard.objects.create(user_id=user, **validated_data)
        return credit_card
