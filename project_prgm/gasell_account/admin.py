from django.contrib import admin
from django.contrib.auth.models import User

from .models import Profile
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['__str__']
    list_per_page = 20
