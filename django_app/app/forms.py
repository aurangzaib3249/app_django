from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["full_name",'email','phone','phone','address',"password1","password2"]
        widget={
            "full_name":forms.TextInput({"class":"form-control","placeholder":"Enter Full Name"}),
            "email":forms.TextInput({"class":"form-control","placeholder":"E-mail"}),
            "phone":forms.TextInput({"class":"form-control","placeholder":"Phone Number"}),
            "password1":forms.PasswordInput({"class":"form-control","placeholder":"Password"}),
            "password2":forms.PasswordInput({"class":"form-control","placeholder":"Confirm Password"}),
            "address":forms.Textarea({"class":"form-control","placeholder":"Full adddres"}),
            
        }
   