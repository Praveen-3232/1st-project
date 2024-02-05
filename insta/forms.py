from django import forms
from .models import userprofile
from django.contrib.auth.models import User
class userprofileform(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','password','email')



class portfolioform(forms.ModelForm):
    class Meta:
        model=userprofile
        field=('profile_pic','portfolio_url')
        exclude=('user',)