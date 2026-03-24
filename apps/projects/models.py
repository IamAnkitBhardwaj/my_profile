from django.db import models
from cloudinary.models import CloudinaryField
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name  

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image')
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    # tech_stack = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    technologies = models.ManyToManyField(Technology, blank=True)
    def __str__(self):
        return self.title
    
  