from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

# Blog model contains title, brief description , date , picture and file to be uploaded
class Blog(models.Model):
    title = models.CharField(max_length=100)
    brief_description = models.TextField()
    date = models.DateField()
    picture = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='files/')

# Daily Updates will contain the number of cases in the country and the date.
class DailyUpdates(models.Model):
    number_of_cases = models.IntegerField()
    date = models.DateField()


# Alerts will contain location , date and time of the alert.
class Alerts(models.Model):
    location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

# The statistics will contain month, the number of positive cases , the deaths and the cures
class Statistics(models.Model):
    month = models.CharField(max_length=100)
    positive_cases = models.IntegerField()
    deaths = models.IntegerField()
    cures = models.IntegerField()

# The report form will contain the name of the person, reason for the test , date , address and a picture and the form will be specific for each user.
class ReportForm(models.Model):
    name = models.CharField(max_length=100)
    reason_for_test = models.TextField()
    date = models.DateField()
    address = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True , null= True)
    avg_color = models.CharField(max_length=20, null=True, blank=True)
    processed_image = models.ImageField(upload_to='processed_image/', blank=True , null= True)
    result = models.CharField(max_length=100, null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

# The results will contain the name of the person , the result of the test and the date of the test.
class Results(models.Model):
    name = models.CharField(max_length=100)
    result = models.ForeignKey(ReportForm, on_delete=models.CASCADE)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# The user model will contain the username, email and password.
class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Change related_name to avoid clash
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Change related_name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    
