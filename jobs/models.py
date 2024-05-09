from django.db import models

# Create your models here.
class Job(models.Model):
    logo = models.ImageField(upload_to='jobs/img/')
    title = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    startDate = models.DateField()
    endDate = models.DateField()
    desc = models.TextField(max_length=200)