from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Answer(models.Model):
    name = models.CharField(max_length=20)
    sn = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class cal4_ans(models.Model):
    total = models.CharField(max_length=100)
    beforeMarry = models.CharField(max_length=100)
    partnerDA = models.CharField(max_length=100)
    partnerName = models.CharField(max_length=20)
    childName = models.CharField(max_length=20)
    parentName = models.CharField(max_length=20)
    broName = models.CharField(max_length=20)
    gPaName = models.CharField(max_length=20)
    estate = models.CharField(max_length=100,blank=True)
    successName = models.CharField(max_length=20,blank=True)
    spendEnd = models.CharField(max_length=100,blank=True)
    successName2 = models.CharField(max_length=20,blank=True)
    spendEnd2 = models.CharField(max_length=100,blank=True)
    childNum = models.CharField(max_length=20)
    parentNum = models.CharField(max_length=20)
    broNum = models.CharField(max_length=20)
    gPaNum = models.CharField(max_length=20)

