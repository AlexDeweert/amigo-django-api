from django.db import models

class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    api_token = models.CharField(max_length=100)

class Timer(models.Model):
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Interval(models.Model):
    description = models.CharField(max_length=100)
    duration = models.IntegerField(default=0)
    timer = models.ForeignKey(Timer, on_delete=models.CASCADE)
