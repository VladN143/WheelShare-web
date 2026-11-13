from django.contrib import admin
from .models import CustomUser, Car, Review
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Car)
admin.site.register(Review)