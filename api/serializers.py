from rest_framework import serializers

from core_auth.models import User
from ttb_backend.models import Transaction, Document


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
        
