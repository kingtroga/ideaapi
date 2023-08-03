from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import CustomUser

class UserCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )
    class Meta:
        model = CustomUser
        fields = ['userID', 'fullName']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        # save the provided password in hashed forms
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    

class UserChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on the
    user, but replaces the password field with admin's disabled
    password hash display field
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ['userID', 'fullName', 'is_mtu_staff', 'is_active']
        
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User
    list_display = ["userID", "fullName", "is_mtu_staff"]
    list_filter = ["is_mtu_staff"]
    fieldsets = [
        (None, {"fields": ["userID", "password"]}),
        ("Personal info", {"fields": ['fullName']}),
        ("Permissions", {"fields":["is_mtu_staff"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attributes when creating a user
    add_fieldsets = [
        (
            None, 
            {
                "classes": ["wide"],
                "fields": ["userID", "fullName", "password1", "password2" ]
            },
        ),
    ]
    search_fields = ["userID", "fullName"]
    ordering = ["userID"]
    filter_horizontal = []

admin.site.register(CustomUser, UserAdmin)

