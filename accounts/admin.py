from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
    "email",
    "username",
    'dungeon_name',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("dm",'dungeon_name')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("dm",'dungeon_name')}),)

admin.site.register(CustomUser, CustomUserAdmin)
