from django.db import models

class UserRegister(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)

class UserLogin(models.Model):
    username_email = models.CharField(max_length=255)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username_email

