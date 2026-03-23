from django.shortcuts import render

# Create your views here.
from .models import Blog

from django.core.paginator import Paginator

def blog_list(request):
    blogs = Blog.objects.all()

    paginator = Paginator(blogs, 6)  # 👈 6 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/blog.html', {
        'page_obj': page_obj
    })

def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blog/blog_detail.html', {'blog': blog})