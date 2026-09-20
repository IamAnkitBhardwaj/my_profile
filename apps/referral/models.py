from django.db import models
from cloudinary.models import CloudinaryField

class ReferralApplication(models.Model):
    EXPERIENCE_CHOICES = [
        ('Fresher', 'Fresher'),
        ('Experienced', 'Experienced'),
    ]

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    qualification = models.CharField(max_length=150)
    graduation_year = models.PositiveIntegerField()

    experience = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES
    )
    current_company_name = models.CharField(max_length=150, blank=True)
    experience_years = models.PositiveIntegerField(blank=True, null=True)
    skills = models.TextField()

    preferred_location = models.CharField(max_length=150)

    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)

    resume = CloudinaryField(
    'resume',
    resource_type='raw'
)

    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name