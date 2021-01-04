from django.db import models

# Create your models here.
class Drama(models.Model):
    value = models.CharField(max_length=100)
    id = models.IntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=200)
    channel = models.CharField(max_length=100)
    info_url = models.TextField()

class Survey(models.Model):
    date = models.DateTimeField()
    age = models.IntegerField
    gender = models.CharField(max_length=4)
    personality = models.CharField(max_length=6)
    activity = models.BooleanField()
    job = models.CharField(max_length=50)
    interested = models.TextField()
    school = models.BooleanField()
    work = models.BooleanField()
    abode = models.CharField(max_length=50)
    siblings = models.IntegerField()
    family = models.IntegerField()
    livealone = models.BooleanField()
    major = models.CharField(max_length=4)
    homeecomony = models.CharField(max_length=6)
    havedate = models.BooleanField()
    physicaltrouble = models.BooleanField()
    mentaltrouble = models.BooleanField()
    prefergenre = models.BooleanField()
    preferchannel = models.CharField(max_length=6)
    watchingtime = models.CharField(max_length=10)
    used = models.TextField()
    way = models.TextField()
    first = models.TextField()
    second = models.TextField()
    third = models.TextField()