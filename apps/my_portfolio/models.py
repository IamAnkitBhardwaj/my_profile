from django.db import models
from cloudinary.models import CloudinaryField
class Profile(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    bio = models.TextField()
    image = CloudinaryField('image')
    resume = CloudinaryField('resume', resource_type='raw')
    
    def __str__(self):
        return self.name

class Skill(models.Model):

    SKILL_TYPE_CHOICES = [
        ('technical', 'Technical'),
        ('tools', 'Tools'),
    ]

    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()
    type = models.CharField(
        max_length=20,
        choices=SKILL_TYPE_CHOICES,
        default='technical'
    )

    # Optional but powerful 🔥
    icon = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Enter FontAwesome class (e.g. fa-brands fa-python)"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-percentage']   # highest skill first
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return f"{self.name} ({self.type})"


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.degree


class Experience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.role


class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=200)
    project = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SocialLink(models.Model):
    platform = models.CharField(max_length=100)
    link = models.URLField()

    icon = models.CharField(
        max_length=100,
        default='fa-solid fa-link',   # 👈 SAFE DEFAULT
        help_text="Enter FontAwesome class (e.g. fa-brands fa-github)"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['platform']

    def __str__(self):
        return self.platform
    
