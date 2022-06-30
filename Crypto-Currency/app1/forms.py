
from django import forms
from django.contrib.auth import get_user_model 
# User
# from django.conf import settings
# from django.db.models import fields
from app1.models import User
# Withdraw, fund, userwallet

from django.contrib.auth.forms import UserCreationForm
# from .models import profile


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))

    wallet_address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Wallet Address",                
                "class": "form-control"
            }
        ))

    phone_no = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Phone No",                
                "class": "form-control"
            }
        ))
   


    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('wallet_address', 'phone_no',)

    # def clean_password2(self):
    #     # Check that the two password entries match
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError("Passwords don't match")
    #     return password2

    # def save(self, commit=True):
    #     # Save the provided password in hashed format
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user




class creditEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fund_amount', 'fund_method']

class DebitEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['withdrawal_amount', 'withdrawal_method']