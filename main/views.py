from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.paginator import Paginator
from .forms import *

# Create your views here.
def home_page(request):
    return render(request, 'main/home.html', {})

def about_page(request):
    return render(request, 'main/about.html', {})

def contact_page(request):
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or provide a success message
            return redirect('home')
    else:
        form = ContactRequestForm()

        return render(request, 'main/contact_us.html', {'form': form})

def project_list_page(request):
    projects = PortfolioProject.objects.all()

    # Set up pagination: Show 10 projects per page
    paginator = Paginator(projects, 10)  # 10 projects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'projects': page_obj
    }

    return render(request, 'main/project_list.html', context)

def project_detail_page(request, project_slug):
    try:
        project = get_object_or_404(PortfolioProject, slug=project_slug)
    except PortfolioProject.DoesNotExist:
        return render(request, '404.html', {})

    return render(request, 'main/project_detail.html', {'project': project})

def submit_project(request):
    if request.method == "POST":
        form = ProjectRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'success_page' with the actual success URL
    else:
        form = ProjectRequestForm()

        return render(request, 'main/submit_project.html', {'form': form})
    
def test(request):
    return render(request, 'main/construction.html', {})
