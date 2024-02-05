from django.db import models
from django.contrib.auth.models import User

class userprofile(models.Model):
    profile_pic=models.ImageField(blank=True, upload_to="profile_pic")
    portfolio_url=models.URLField(blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

