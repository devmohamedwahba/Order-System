from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from django.utils.translation import gettext as _


class UserAdminClass(UserAdmin):
    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal_Info"), {"fields": ("name",)}),
        (
            _("Permission"),
            {
                "fields": ("is_active", "is_staff", "is_superuser")
            }
        ),
        (_("Important Dates"), {"fields": ("last_login",)})
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2")
        }),
    )


admin.site.register(models.User, UserAdminClass)