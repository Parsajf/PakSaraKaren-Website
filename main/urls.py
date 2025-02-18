from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name="home"),
    path('about/', about_page, name="about"),
    path('contact-us/', contact_page, name="contact-us"),
    path('projects/', project_list_page, name="project-list"),
    path('submit-project/', submit_project, name="submit-project"),
    path('projects/<slug:project_slug>/', project_list_page, name="project-detail"),
    path('test/', test, name="test"),
]
