from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
import os



class CustomUserManager(BaseUserManager):
    
    def create_user(self, userID: int, fullName, password=None):
        """
        Creates and saves a User with the given 
        i. UserID e.g Matric No/Staff Id,
        ii. Full Name e.g Yekorogha Ayebatariwalate
        iii. Password e.g janet2003
        """
        if not userID:
            raise ValueError("Users must have a Matric Number/Staff ID")
        
        user = self.model(
            userID=userID,
            fullName=fullName,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userID: int, fullName, password=None):
        """
        Creates and saves a superuser with the given:
        i. UserId e.g Matric No/ Staff ID,
        ii. Full Name e.g Yekorogha Ayebatariwalate
        iii. Password e.g janet 2003
        """
        user = self.create_user(
            userID,
            fullName,
            password
        )
        user.is_mtu_staff = True
        user.save(using=self._db)
        return user



def get_upload_path(instance, filename):
    return os.path.join('images', 'avatars', str(instance.pk), filename)



class CustomUser(AbstractBaseUser):
    fullName = models.CharField(max_length=200, blank=False, null=False)
    userID = models.PositiveIntegerField(unique=True, blank=False, null=False)
    is_mtu_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to=get_upload_path, blank=True, null=True, default="default/account.png")
    objects = CustomUserManager()

    # username
    USERNAME_FIELD = 'userID'
    REQUIRED_FIELDS = ['fullName']

    def get_full_name(self) -> str:
        return self.fullName
    
    def __str__(self) -> str:
        return self.fullName
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        '''Is the user a member of MTU STAFF?'''
        return self.is_mtu_staff
    