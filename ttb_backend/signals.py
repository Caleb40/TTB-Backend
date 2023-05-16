from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Transaction


@receiver(post_save, sender=Transaction)
def update_user_total_deposit(sender, instance, created, **kwargs):
    if created and instance.transaction_type == 'DEPOSIT' and instance.status == 'S':
        # Update the user's total_deposit attribute
        instance.user.total_deposit += instance.amount
        instance.user.account_balance += instance.amount
        instance.user.save()


@receiver(post_save, sender=Transaction)
def add_gift_bonus(sender, instance, created, **kwargs):
    if created:
        # Add gift bonus to the user's account_balance attribute
        instance.user.account_balance += instance.gift_bonus
        instance.user.save()


@receiver(post_save, sender=Transaction)
def send_email_on_transaction_sucessful(sender, instance, created, **kwargs):
    if instance.status == 'S':
        subject = 'Transaction Successful'
        message = f'Your transaction of amount £{instance.amount} was successful.' \
                  f' Your account balance will be updated shortly, thanks for your patronage.'
        recipient_list = [
            instance.user.email]
        send_mail(subject, message, from_email=None, recipient_list=recipient_list)
