from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Project, Technology

from django.core.paginator import Paginator

def projects_list(request):
    query = request.GET.get('q')
    tech = request.GET.get('tech')

    projects = Project.objects.all()
    all_technologies = Technology.objects.all()   # 👈 MUST

    if query:
        projects = projects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    if tech:
        projects = projects.filter(technologies__name__iexact=tech)

    paginator = Paginator(projects, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'projects/projects.html', {
        'page_obj': page_obj,
        'all_technologies': all_technologies   # 👈 MUST
    })


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'projects/project_detail.html', {'project': project})