from django.contrib import admin

from ttb_backend.models import Document, Transaction, CreditCard

# Register your models here.
admin.site.register(Document)
admin.site.register(Transaction)
admin.site.register(CreditCard)