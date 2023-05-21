from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

SIGNON_BONUS_AMOUNT = 10


@receiver(post_save, sender=User)
def add_signon_bonus(sender, instance, created, **kwargs):
    if created:
        # Add sign-on bonus to the user's account_balance attribute
        instance.account_balance += SIGNON_BONUS_AMOUNT
        instance.save()


@receiver(post_save, sender=User)
def alert_admin_of_new_user(sender, instance, created, **kwargs):
    if created and instance.is_active:
        subject = 'New User Activated'
        message = f'A new user {instance.first_name} - "{instance.email}" has been created and activated. 🎉'
        recipient_list = ['toptierbinary@gmail.com']
        send_mail(subject, message, from_email=None, recipient_list=recipient_list)
