from django.db import models

# Create your models here.

class SendEmailClass(models.Model):
    name = models.TextField(max_length=30)
    surname = models.TextField(max_length=30)
    email = models.EmailField(max_length=30)
    description = models.TextField(max_length=250)