from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'full_name', 'department', 'program', 'is_staff', 'is_doctor', )
    list_filter = ('email', 'full_name', 'department', 'program', 'is_staff', 'is_doctor')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username',)}),
        ('Personal info', {'fields': ('full_name', 'department', 'program','user_id','security_question', 'secureQusAns')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_doctor', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username', 'full_name', 'department', 'program', 'user_id', 'password1', 'password2', 'is_staff', 'is_doctor', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return self.add_form
        else:
            return self.form

admin.site.register(CustomUser, CustomUserAdmin)
