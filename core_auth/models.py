import os

import requests
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from core_auth.managers import UserManager
import cloudinary
from cloudinary import uploader
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_NAME'),
    api_key=os.getenv('CLOUDINARY_KEY'),
    api_secret=os.getenv('CLOUDINARY_SECRET')
)


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

    profile_image = models.ImageField(blank=True, null=True, upload_to='profile_image')

    # Financial Info
    total_investment_plans = models.IntegerField(default=0)
    active_investment_plans = models.IntegerField(default=0)
    total_deposit = models.IntegerField(default=0)
    total_withdrawal = models.IntegerField(default=0)
    total_ref_bonus = models.IntegerField(default=0)
    account_balance = models.IntegerField(default=0)

    # def save(self, *args, **kwargs):
    #     if self.profile_image:
    #         compressed_image = self.compress_image(self.profile_image)
    #         self.image = compressed_image
    #     super().save(*args, **kwargs)

    # @staticmethod
    # def compress_image(image):
    #     image_io = BytesIO(image.read())
    #     compressed_image = uploader.upload(
    #         image_io,
    #         transformation=[
    #             {'quality': 'auto:low'}
    #         ]
    #     )
    #     compressed_image_url = compressed_image['secure_url']
    #     print(compressed_image_url)
    #     image.seek(0)
    #     image_name = image.name.split('/')[-1]
    #     image_content_type = image.file.content_type
    #     compressed_image_io = BytesIO(requests.get(compressed_image_url).content)
    #     compressed_image_io.seek(0)
    #     compressed_image_io = InMemoryUploadedFile(
    #         compressed_image_io,
    #         None,
    #         image_name,
    #         image_content_type,
    #         None,
    #         None
    #     )
    #     return compressed_image_io
