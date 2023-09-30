from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class CustomUserManager(BaseUserManager):
    def create_user(self, user_id, full_name, password=None):
        """
        Creates and saves a User with the given user_id, 
        full_name and password.
        """
        if not user_id:
            raise ValueError("Users must have a user_id i.e Matric No or Staff Id")

        user = self.model(
            user_id=user_id,
            full_name=full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, full_name, password=None):
        """
        Creates and saves a superuser with the given user_id, 
        full_name and password.
        """
        user = self.create_user(
            user_id=user_id,
            password=password,
            full_name=full_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    user_id = models.PositiveIntegerField(primary_key=True, null=False, blank=False)
    full_name = models.TextField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "user_id"
    REQUIRED_FIELDS = ["full_name"]

    def __str__(self):
        return str(self.user_id)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin