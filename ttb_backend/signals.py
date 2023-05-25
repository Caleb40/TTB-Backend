from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from core_auth.models import User
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
    if created and instance.status == 'S' and instance.transaction_type == 'DEPOSIT':
        # Add gift bonus to the user's account_balance attribute
        instance.user.account_balance += instance.gift_bonus
        instance.user.save()


@receiver(post_save, sender=Transaction)
def alert_admin_of_new_transaction(sender, instance, created, **kwargs):
    if created:
        subject = f'New Transaction Request!! [{instance.transaction_type.upper()}]'
        message = f'User, {instance.user.first_name} {instance.user.last_name} with email:' \
                  f' {instance.user.email} just initiated a transaction!!! 🎉.' \
                  f' The amount is £{instance.amount}. Check the admin and wallet address' \
                  f' to confirm the transaction and update the status accordingly.'
        recipient_list = ['toptierbinary@gmail.com']
        send_mail(subject, message, from_email=None, recipient_list=recipient_list)


@receiver(post_save, sender=Transaction)
def send_email_on_transaction_successful(sender, instance, created, **kwargs):
    if instance.status == 'S':
        subject = 'Transaction Successful'
        message = f'Your transaction of amount £{instance.amount} was successful.' \
                  f' Your account balance will be updated shortly, thanks for your patronage.'
        recipient_list = [
            instance.user.email]
        send_mail(subject, message, from_email=None, recipient_list=recipient_list)
