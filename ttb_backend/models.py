from uuid import uuid4

from django.db import models

from core_auth.models import User

D = 'DEPOSIT'
W = 'WITHDRAWAL'
R = 'ROI'
N = 'NUB'
TRANSACTION_TYPES = [
    (D, 'Deposit'),
    (W, 'Withdrawal'),
    (R, 'Return on Investment'),
    (N, 'New User Bonus'),
]

STATUSES = [
    ('P', 'PENDING'),
    ('S', 'SUCCESSFUL'),
    ('F', 'FAILED'),
]

CHANNELS = [
    ('BTC', 'Bitcoin'),
    ('WIR', 'Wire'),
    ('PPL', 'Paypal'),
    ('CSH', 'Cash App'),
    ('ACB', 'Added to Account Balance'),
]


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_id = models.UUIDField(default=uuid4, editable=False)
    transaction_type = models.CharField(choices=TRANSACTION_TYPES, default=D, max_length=20)
    status = models.CharField(choices=STATUSES, max_length=5, default='P')
    channel = models.CharField(choices=CHANNELS, max_length=5)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    # Extra Fields
    return_amount = models.IntegerField(default=0)
    investment_duration = models.IntegerField(default=0)
    gift_bonus = models.IntegerField(default=True)


class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_front = models.ImageField(blank=True, null=True, upload_to='customers/documents/')
    id_back = models.ImageField(blank=True, null=True, upload_to='customers/documents/')
    passport = models.ImageField(blank=True, null=True, upload_to='customers/documents/')
    selfie = models.ImageField(blank=True, null=True, upload_to='customers/documents/')
    proof_of_address = models.ImageField(blank=True, null=True, upload_to='customers/documents/')
