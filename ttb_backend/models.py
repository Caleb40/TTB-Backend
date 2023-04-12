from django.db import models


class Documents(models.Model):
    id_front = models.ImageField(blank=True, null=True, upload_to='customers/documents/')
    id_back = models.ImageField(blank=True, null=True, upload_to='customers/documents/')
    passport = models.ImageField(blank=True, null=True, upload_to='customers/documents/')
    selfie = models.ImageField(blank=True, null=True, upload_to='customers/documents/')
    proof_of_address = models.ImageField(blank=True, null=True, upload_to='customers/documents/')
