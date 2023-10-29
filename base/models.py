import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):

    client_id = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=50000, null=True, blank=True)
    l_name = models.CharField(max_length=50000, null=True, blank=True)
    company_name = models.CharField(max_length=50000, null=True, blank=True)
    address = models.CharField(max_length=50000, null=True, blank=True)
    address_phone = models.CharField(max_length=50000, null=True, blank=True)
    phone = models.CharField(max_length=50000, null=True, blank=True)
    email = models.CharField(max_length=50000, null=True, blank=True)
    is_mailed = models.BooleanField(default=False)
    last_mail_date = models.DateField(auto_now=True, null=True, blank=True)
    count = models.IntegerField(default=0)
    assignee = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} - {self.company_name}"

