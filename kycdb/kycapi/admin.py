from django.contrib import admin
from .models import UserRegister
# Register your models here.
@admin.register(UserRegister)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','phone_number','password']
