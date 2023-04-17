from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction


@receiver(post_save, sender=Transaction)
def update_user_total_deposit(sender, instance, created, **kwargs):
    if created and instance.transaction_type == 'DEPOSIT':
        # Update the user's total_deposit attribute
        instance.user.total_deposit += instance.amount
        instance.user.save()


@receiver(post_save, sender=Transaction)
def add_gift_bonus(sender, instance, created, **kwargs):
    if created:
        # Add gift bonus to the user's account_balance attribute
        instance.user.account_balance += instance.gift_bonus
        instance.user.save()
