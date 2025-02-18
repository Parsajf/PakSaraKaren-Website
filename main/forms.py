from django import forms
from .models import *

class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'contact_info', 'description']  # Fields you want in the form

        # Optionally, you can customize widgets for each field
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': "نام و نام خانوادگی خود را وارد کنید", 'id': "c-name", 'type': "text"}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': "ایمیل یا شماره خود را وارد کنید", 'id': "c-email", 'type': "text"}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'placeholder': "متن مورد نظر خود را بنویسید ...", 'id': "c-message", 'rows': "4"}),
        }

class ProjectRequestForm(forms.ModelForm):
    price = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'قیمت', 'type': "text", 'id': "price"
    }))
    class Meta:
        model = ProjectRequest
        fields = [
            'first_name', 'last_name', 'phone_number', 'email', 
            'state', 'city', 'district', 'zip_code', 'address',
            'area', 'floor_count', 'description', 'price'
        ]
        
        # Optionally add widgets to customize the appearance
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام شخص', 'type': "text", 'id': "person-name", 'oninput': "validatePersian(this)"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی', 'type': "text", 'id': "personal-last-name", 'oninput': "validatePersian(this)"}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره موبایل', 'type': "text", 'id': "person-name"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل', 'type': "text", 'id': "personal-last-name"}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'استان', 'type': "text", 'id': "state", 'oninput': "validatePersian(this)"}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شهر', 'type': "text", 'id': "city", 'oninput': "validatePersian(this)"}),
            'district': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'منطقه پروژه', 'type': "text", 'id': "district"}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کد پستی', 'type': "text", 'id': "zip-code"}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس', 'type': "text", 'id': "address"}),
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'مساحت کل بر اساس متر مربع', 'type': "text", 'id': "area"}),
            'floor_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'تعداد طبقات', 'type': "text", 'id': "floor-count"}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'توضیحات', 'type': "text", 'id': "description"}),
            # 'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'قیمت', 'type': "text", 'id': "price"}),
        }
