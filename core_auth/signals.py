from django.contrib.auth import get_user_model
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
