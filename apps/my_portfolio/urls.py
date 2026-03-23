from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home, name='home'),
    path('project/<int:id>/', project_detail, name='project_detail'),
    path('about/', about, name='about'),
    
]

