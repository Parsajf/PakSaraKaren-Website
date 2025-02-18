from django.shortcuts import render, redirect
from .forms import *
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
from .tasks import send_email_task

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('profile')

    person_form = PersonConstructionManagerForm()
    company_form = CompanyConstructionManagerForm()

    context = {
        'person_form': person_form,
        'company_form': company_form
    }

    return render(request, 'registration/construction.html', context)

# @require_POST
# def create_person_construction_manager(request):
#     form = PersonConstructionManagerForm(request.POST)
#     if form.is_valid():
#         user = form.save(commit=False)
#         user.set_password(form.cleaned_data['password'])  # Hash the password
#         user.save()
#         return redirect('home')  # Redirect to a success page after saving
#     return redirect('registration-form')
# def create_company_construction_manager(request):
#     form = CompanyConstructionManagerForm(request.POST)
#     if form.is_valid():
#         user = form.save(commit=False)
#         user.set_password(form.cleaned_data['password'])  # Hash the password
#         user.save()
#         return redirect('home')  # Redirect to a success page after saving

#@require_POST
def create_person_construction_manager(request):
    if request.method == 'POST':
        form = PersonConstructionManagerForm(request.POST)
        if form.is_valid():
            try:
                # Create a new user instance
                user = form.save(commit=False)
                # Set the password (hashes it)
                user.set_password(form.cleaned_data['password'])
                user.save()

                # Send email using Celery task
                # subject = "به پاک سرا کارن خوش آمدید"
                # message = "ثبت نام شما با موفقیت انجام شد، از اعتماد شما متشکریم."
                # from_email = None
                # recipient_list = [user.email]

                # send_email_task.delay(subject, message, from_email, recipient_list)

                # authenticated_user = authenticate(username=user.username, password=form.cleaned_data['password'])

                # login(request, authenticated_user)  # This logs the user in automatically
                return redirect('login')
                
            except Exception as e:
                print("Error saving person user:", e)
                messages.error(request, "Failed to create person user.")
        else:
            print("Form is not valid:", form.errors)
    else:
        form = PersonConstructionManagerForm()
    
    return render(request, 'registration/construction.html', {'person_form': form})

@require_POST
def create_company_construction_manager(request):
    form = CompanyConstructionManagerForm(request.POST)
    if form.is_valid():
        try:
            # Create a new user instance
            user = form.save(commit=False)
            # Set the password (hashes it)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Send email using Celery task
            subject = "به پاک سرا کارن خوش آمدید"
            message = "ثبت نام شما با موفقیت انجام شد، از اعتماد شما متشکریم."
            from_email = None
            recipient_list = [user.email]

            send_email_task.delay(subject, message, from_email, recipient_list)
            
            messages.success(request, "Company user created successfully!")
            return redirect('home')
        except Exception as e:
            print("Error saving company user:", e)
            messages.error(request, "Failed to create company user.")
    else:
        print("Form is not valid:", form.errors)
    return redirect('registration/construction.html')

@login_required
def profile(request):
    password_form = PasswordChangeForm(user=request.user)
    # password_form = PasswordChangeForm()
    area_form = AreaUpdateForm()
    floors_form = FloorsUpdateForm()
    district_form = DistrictUpdateForm()
    user = request.user

    return render(request, 'registration/profile.html', {
        'password_form': password_form,
        'area_form': area_form,
        'floors_form': floors_form,
        'district_form': district_form,
        'user': user
    })

def user_login(request):
    # Redirect authenticated users to the profile page
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Authenticate using the custom backend
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirect to profile after login
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()
    
    return render(request, 'registration/login.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        # Pass the logged-in user to the form
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()  # Save the new password
            messages.success(request, "Your password has been changed successfully!")
            return redirect('profile')  # Redirect to the profile page
        else:
            # messages.error(request, "Please correct the errors below.")
            print(form.errors)
            return redirect('profile')
    else:
        user = request.user

    return render(request, 'registration/profile.html', {'user': user})

def user_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')

@login_required
def update_area(request):
    if request.method == 'POST':
        # Initialize the form with POST data and the current user instance
        area_form = AreaUpdateForm(request.POST, instance=request.user)
        if area_form.is_valid():
            # Save changes to the user's first_name, last_name, and email
            area_form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile')  # Redirect to the profile or another page
        else:
            messages.error(request, "Please correct the errors below.")
            return redirect('profile')
    else:
        # If it's a GET request, pre-fill the form with the user's current data
        profile_form = AreaUpdateForm(instance=request.user)

    return render(request, 'profile.html', {'profile_form': profile_form})

@login_required
def update_floors(request):
    if request.method == 'POST':
        # Initialize the form with POST data and the current user instance
        floors_form = FloorsUpdateForm(request.POST, instance=request.user)
        if floors_form.is_valid():
            # Save changes to the user's first_name, last_name, and email
            floors_form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile')  # Redirect to the profile or another page
        else:
            messages.error(request, "Please correct the errors below.")
            return redirect('profile')
    else:
        # If it's a GET request, pre-fill the form with the user's current data
        profile_form = FloorsUpdateForm(instance=request.user)

    return render(request, 'profile.html', {'profile_form': profile_form})

@login_required
def update_district(request):
    if request.method == 'POST':
        # Initialize the form with POST data and the current user instance
        district_form = DistrictUpdateForm(request.POST, instance=request.user)
        
        if district_form.is_valid():
            # Save changes to the user's district (assuming the field is in the user model)
            district_form.save()
            messages.success(request, "Your district has been updated successfully!")
            return redirect('profile')  # Redirect to the profile or another page
        else:
            messages.error(request, "Please correct the errors below.")
            # Render the same template with the form to display errors
            return render(request, 'registration/profile.html', {'profile_form': district_form})
    else:
        # If it's a GET request, pre-fill the form with the user's current data
        district_form = DistrictUpdateForm(instance=request.user)

    return render(request, 'profile.html', {'profile_form': district_form})
