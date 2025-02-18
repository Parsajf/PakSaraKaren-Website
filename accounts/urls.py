from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name="registration-form"),
    path('register/person/', create_person_construction_manager, name="person-registration"),
    path('register/company/', create_company_construction_manager, name="company-registration"),
    path('profile/', profile, name="profile"),
    path('login/', user_login, name="login"),
    path('change-password/', change_password, name='change-password'),
    path('logout/', user_logout, name='logout'),
    path('change-area/', update_area, name="change-area"),
    path('change-floors/', update_floors, name="change-floors"),
    path('change-districts/', update_district, name="change-districts"),
]
