from django import forms
from .models import PersonConstructionManager, CompanyConstructionManager, ConstructionManager
from django.core.exceptions import ValidationError
import re

# Validations
def validate_password(value):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$'
    if not re.match(pattern, value):
        raise ValidationError(
            'لطفا، رمزعبور خود را تغییر دهید'
        )

# class PersonConstructionManagerForm(forms.ModelForm):
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={
#             'type': 'password',
#             'minlength': '8',
#             'class': 'form-control',
#             'placeholder': 'رمزعبور خود را وارد کنید (حداقل 8 کاراکتر)'
#         }),
#         validators=[validate_password]
#     )
#     confirm_password = forms.CharField(
#         widget=forms.PasswordInput(attrs={
#             'type': 'password',
#             'minlength': '8',
#             'class': 'form-control',
#             'placeholder': 'رمزعبور خود را تایید کنید'
#         })
#     )

#     class Meta:
#         model = PersonConstructionManager
#         fields = [
#             'email', 'first_name', 'last_name', 'state', 'city', 'phone_number',
#             'district_1st', 'district_2nd', 'district_3rd', 'district_4th', 'district_5th',
#             'min_floors', 'max_floors', 'min_area', 'max_area'
#         ]
#         widgets = {
#             'email': forms.EmailInput(attrs={'type': "text", 'id': "personal-last-name", 'placeholder': "ایمیل", 'class': 'form-control'}),
#             'first_name': forms.TextInput(attrs={'type': "text", 'id': "person-name", 'placeholder': "نام شخص", 'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'type': "text", 'id': "personal-last-name", 'placeholder': "نام خانوادگی شخص", 'class': 'form-control'}),
#             'phone_number': forms.TextInput(attrs={'type': "text", 'id': "person-name", 'placeholder': "شماره موبایل", 'class': 'form-control'}),
#             'state': forms.TextInput(attrs={'class': "form-control", 'type': "text", 'id': "state", 'placeholder': "استان"}),
#             'city': forms.TextInput(attrs={'class': "form-control", 'type': "text", 'id': "city", 'placeholder': "شهر"}),
#             'district_1st': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'id': "district1", 'min': "1"}),
#             'district_2nd': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'id': "district2", 'min': "1", 'style': "display: none;"}),
#             'district_3rd': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'id': "district3", 'min': "1", 'style': "display: none;"}),
#             'district_4th': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'id': "district4", 'min': "1", 'style': "display: none;"}),
#             'district_5th': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'id': "district5", 'min': "1", 'style': "display: none;"}),
#             'min_floors': forms.NumberInput(attrs={'class': "form-control", 'type': "text", 'id': "min-area", 'placeholder': "حداقل طبقات"}),
#             'max_floors': forms.NumberInput(attrs={'class': "form-control", 'type': "text", 'id': "max-area", 'placeholder': "حداکثر طبقات"}),
#             'min_area': forms.TextInput(attrs={'class': "form-control", 'type': "text", 'id': "min-area", 'placeholder': "حداقل متراژ"}),
#             'max_area': forms.TextInput(attrs={'class': "form-control", 'type': "text", 'id': "max-area", 'placeholder': "حداکثر متراژ"}),
#         }

class PersonConstructionManagerForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'minlength': '8',
            'class': 'form-control',
            'placeholder': 'رمزعبور خود را وارد کنید (حداقل 8 کاراکتر)'
        }),
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'minlength': '8',
            'class': 'form-control',
            'placeholder': 'رمزعبور خود را تایید کنید'
        })
    )

    district_2nd = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control', 'style': 'display: none;'
    }))
    district_3rd = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control', 'style': 'display: none;'
    }))
    district_4th = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control', 'style': 'display: none;'
    }))
    district_5th = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control', 'style': 'display: none;'
    }))
    min_floors = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'حداقل طبقات'
    }))
    max_floors = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'حداکثر طبقات'
    }))
    min_area = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'حداقل متراژ'
    }))
    max_area = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'حداکثر متراژ'
    }))

    class Meta:
        model = PersonConstructionManager
        fields = [
            'email', 'first_name', 'last_name', 'state', 'city', 'phone_number',
            'district_1st', 'district_2nd', 'district_3rd', 'district_4th', 'district_5th',
            'min_floors', 'max_floors', 'min_area', 'max_area'
        ]
        widgets = {
            'email': forms.EmailInput(attrs={'type': "text", 'placeholder': "ایمیل", 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'type': "text", 'placeholder': "نام شخص", 'class': 'form-control', 'oninput': "validatePersian(this)"}),
            'last_name': forms.TextInput(attrs={'type': "text", 'placeholder': "نام خانوادگی شخص", 'class': 'form-control', 'oninput': "validatePersian(this)"}),
            'phone_number': forms.TextInput(attrs={'type': "text", 'placeholder': "شماره موبایل", 'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': "form-control", 'type': "text", 'placeholder': "استان", 'oninput': "validatePersian(this)"}),
            'city': forms.TextInput(attrs={'class': "form-control", 'type': "text", 'placeholder': "شهر", 'oninput': "validatePersian(this)"}),
            'district_1st': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'min': "1"}),
            # 'district_2nd': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'min': "1", 'style': "display: none;"}),
            # 'district_3rd': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'min': "1", 'style': "display: none;"}),
            # 'district_4th': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'min': "1", 'style': "display: none;"}),
            # 'district_5th': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'min': "1", 'style': "display: none;"}),
            # 'min_floors': forms.NumberInput(attrs={'class': "form-control", 'placeholder': "حداقل طبقات"}),
            # 'max_floors': forms.NumberInput(attrs={'class': "form-control", 'placeholder': "حداکثر طبقات"}),
            # 'min_area': forms.TextInput(attrs={'class': "form-control", 'placeholder': "حداقل متراژ"}),
            # 'max_area': forms.TextInput(attrs={'class': "form-control", 'placeholder': "حداکثر متراژ"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("رمزهای عبور با یکدیگر مطابقت ندارند.")

        return cleaned_data

class CompanyConstructionManagerForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'minlength': '8',
            'class': 'form-control',
            'placeholder': 'رمزعبور خود را وارد کنید (حداقل 8 کاراکتر)'
        }),
        validators=[validate_password]
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'minlength': '8',
            'class': 'form-control',
            'placeholder': 'رمزعبور خود را تایید کنید'
        })
    )

    class Meta:
        model = CompanyConstructionManager
        fields = [
            'email', 'name', 'state', 'city', 'phone_number',
            'district_1st', 'district_2nd', 'district_3rd', 'district_4th', 'district_5th',
            'min_floors', 'max_floors', 'min_area', 'max_area'
        ]
        widgets = {
            'email': forms.EmailInput(attrs={'type': "text", 'id': "personal-last-name", 'placeholder': "ایمیل", 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'type': "text", 'id': "person-name", 'placeholder': "نام شرکت", 'class': 'form-control', 'oninput': "validatePersian(this)"}),
            'phone_number': forms.TextInput(attrs={'type': "text", 'id': "person-name", 'placeholder': "شماره موبایل", 'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': "form-control", 'type': "text", 'id': "state", 'placeholder': "استان", 'oninput': "validatePersian(this)"}),
            'city': forms.TextInput(attrs={'class': "form-control", 'type': "text", 'id': "city", 'placeholder': "شهر", 'oninput': "validatePersian(this)"}),
            'district_1st': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'id': "district1", 'min': "1"}),
            'district_2nd': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'id': "district2", 'min': "1", 'style': "display: none;"}),
            'district_3rd': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'id': "district3", 'min': "1", 'style': "display: none;"}),
            'district_4th': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'id': "district4", 'min': "1", 'style': "display: none;"}),
            'district_5th': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'id': "district5", 'min': "1", 'style': "display: none;"}),
            'min_floors': forms.NumberInput(attrs={'class': "form-control", 'type': "text", 'id': "min-area", 'placeholder': "حداقل طبقات"}),
            'max_floors': forms.NumberInput(attrs={'class': "form-control", 'type': "text", 'id': "max-area", 'placeholder': "حداکثر طبقات"}),
            'min_area': forms.TextInput(attrs={'class': "form-control", 'type': "text", 'id': "min-area", 'placeholder': "حداقل متراژ"}),
            'max_area': forms.TextInput(attrs={'class': "form-control", 'type': "text", 'id': "max-area", 'placeholder': "حداکثر متراژ"}),
        }

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )

class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(
        label="Old Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your old password'}),
    )
    new_password = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter a new password'}),
        validators=[validate_password],
    )
    confirm_new_password = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm the new password'}),
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise ValidationError("The old password is incorrect.")
        return old_password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")

        if new_password and confirm_new_password and new_password != confirm_new_password:
            raise ValidationError("The new passwords do not match.")
        
        return cleaned_data

    def save(self, commit=True):
        new_password = self.cleaned_data["new_password"]
        self.user.set_password(new_password)
        if commit:
            self.user.save()  # Ensure the user is saved with the new password
        return self.user

class AreaUpdateForm(forms.ModelForm):
    class Meta:
        model = ConstructionManager  # Replace with your actual model
        fields = ['min_area', 'max_area']

    min_area = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Add your desired CSS class here
            'placeholder': "حداقل متراژ"
        })
    )

    max_area = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "حداکثر متراژ"
        })
    )

class FloorsUpdateForm(forms.ModelForm):
    class Meta:
        model = ConstructionManager  # Replace with your actual model
        fields = ['min_floors', 'max_floors']

    min_floors = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',  # Add your desired CSS class here
            'placeholder': "حداقل طبقات"
        })
    )

    max_floors = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "حداکثر طبقات"
        })
    )

class DistrictUpdateForm(forms.ModelForm):
    class Meta:
        model = ConstructionManager  # Replace with your base user model
        fields = ['district_1st', 'district_2nd', 'district_3rd', 'district_4th', 'district_5th']  # Add other fields if needed
        widgets = {
            'district_1st': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'id': "district1", 'min': "1"}),
            'district_2nd': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'id': "district2", 'min': "1", 'style': "display: none;"}),
            'district_3rd': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'id': "district3", 'min': "1", 'style': "display: none;"}),
            'district_4th': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'id': "district4", 'min': "1", 'style': "display: none;"}),
            'district_5th': forms.NumberInput(attrs={'class': "form-control", 'type': "number", 'id': "district5", 'min': "1", 'style': "display: none;"}),
        }

    def __init__(self, *args, **kwargs):
        super(DistrictUpdateForm, self).__init__(*args, **kwargs)
        # Customize each field's attributes here if needed
        self.fields['district_1st'].required = True

    def save(self, commit=True):
        # Get the form data
        user = super(DistrictUpdateForm, self).save(commit=False)
        
        # Perform any additional actions if needed
        # Example: user.username = f"{user.first_name}_{user.last_name}"

        if commit:
            user.save()  # Save to the database
        return user
