from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {
            "fields": ("phone_number", "role"),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields": ("phone_number", "role"),
        }),
    )

    list_display = (
        "username",
        "email",
        "phone_number",
        "role",
        "is_staff",
    )

    list_filter = ("role", "is_staff")