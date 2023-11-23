from django.db import models


class userdata(models.Model):
    username=models.CharField(max_length=255,null=True)
    email = models.CharField(max_length=255,null=True)
    password = models.CharField(max_length=255,null=True)
    otp = models.CharField(max_length=255,null=True)
    