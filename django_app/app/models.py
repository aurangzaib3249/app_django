from django.db import models
from rest_framework import serializers

from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import gettext_lazy as _
class UserManger(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Email is Requied")
        if not password:
            raise ValueError("Password is Required")
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_superuser",True)
        return self.create_user(email,password,**extra_fields)

class User(AbstractUser):
    username=None
    id = models.AutoField(primary_key=True)
    email=models.EmailField(_("E-mail"),unique=True)
    full_name=models.CharField(max_length=40)
    phone=models.CharField(_("Phone Number"),max_length=20)
    address=models.CharField(_("Home Address"),max_length=70)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    objects=UserManger()
    def save(self,*args, **kwargs):
        #self.id=User.objects.all().count()+1
        super(User,self).save(*args, **kwargs)
class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ="__all__"