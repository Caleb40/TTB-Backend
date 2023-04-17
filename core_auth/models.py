from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from core_auth.managers import UserManager


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    phone = models.CharField(max_length=14, null=True, blank=True)
    city = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=50, null=True)

    # Corporate Info (Optional)
    company_name = models.CharField(max_length=50, null=True, blank=True)
    corporate_phone = models.CharField(max_length=14, null=True, blank=True)
    corporate_reg_no = models.CharField(max_length=50, null=True, blank=True)
    company_vat_no = models.CharField(max_length=50, null=True, blank=True)

    profile_image = models.ImageField(blank=True, null=True, upload_to='customers/profiles/')

    # Financial Info
    total_investment_plans = models.IntegerField(default=0)
    active_investment_plans = models.IntegerField(default=0)
    total_deposit = models.IntegerField(default=0)
    total_withdrawal = models.IntegerField(default=0)
    total_ref_bonus = models.IntegerField(default=0)
    account_balance = models.IntegerField(default=0)
