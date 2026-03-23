from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from apps.projects.models import *
from .models import *

def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()[:6]
    social_links = SocialLink.objects.all()

    education = Education.objects.all()
    experience = Experience.objects.all()
    certifications = Certification.objects.all()
    clients = Client.objects.all()

    return render(request, 'home.html', {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'social_links': social_links,
        'education': education,
        'experience': experience,
        'certifications': certifications,
        'clients': clients
    })

def project_detail(request):
    return render(request, 'project_detail.html')

def about(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    certifications = Certification.objects.all()
    clients = Client.objects.all()
    projects = Project.objects.all()

    return render(request, 'about.html', {
        'profile': profile,
        'skills': skills,
        'education': education,
        'experience': experience,
        'certifications': certifications,
        'clients': clients,
        'projects': projects
    })
