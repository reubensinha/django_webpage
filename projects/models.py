from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='projects/img/')
    technologies = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    startDate = models.DateField()
    endDate = models.DateField()
    desc = models.TextField(max_length=200)
    visable = models.BooleanField(default=False)    
    
    def __str__(self):
        return self.title
