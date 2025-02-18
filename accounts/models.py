from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class ConstructionManagerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('لطفا ایمیل را وارد کنید')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # Add defaults for fields you don't want to specify during superuser creation
        extra_fields.setdefault('district_1st', 0)
        extra_fields.setdefault('district_2nd', 0)
        extra_fields.setdefault('district_3rd', 0)
        extra_fields.setdefault('district_4th', 0)
        extra_fields.setdefault('district_5th', 0)
        extra_fields.setdefault('min_floors', 0)
        extra_fields.setdefault('max_floors', 0)
        extra_fields.setdefault('min_area', '0')
        extra_fields.setdefault('max_area', '0')
        extra_fields.setdefault('state', '0')
        extra_fields.setdefault('city', '0')

        return self.create_user(email, password, **extra_fields)

# Create your models here.
class ConstructionManager(AbstractUser):
    username = None  # Remove the username field
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)  # Make email unique and required
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    district_1st = models.PositiveIntegerField()
    district_2nd = models.PositiveIntegerField(null=True, blank=True)
    district_3rd = models.PositiveIntegerField(null=True, blank=True)
    district_4th = models.PositiveIntegerField(null=True, blank=True)
    district_5th = models.PositiveIntegerField(null=True, blank=True)
    min_floors = models.PositiveIntegerField(null=True, blank=True)
    max_floors = models.PositiveIntegerField(null=True, blank=True)
    min_area = models.CharField(max_length=15, null=True, blank=True)
    max_area = models.CharField(max_length=15, null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'  # Set email as the unique identifier
    REQUIRED_FIELDS = ['phone_number', 'state', 'city', 'district_1st', 'min_floors', 'max_floors', 'min_area', 'max_area']

    objects = ConstructionManagerManager()

    def user_type(self):
        if hasattr(self, 'personconstructionmanager'):
            return "person"
        elif hasattr(self, 'companyconstructionmanager'):
            return "company"
        return "general"

    class Meta:
        verbose_name = "All"
        verbose_name_plural = "All"
    
class PersonConstructionManager(ConstructionManager):
    REQUIRED_FIELDS = ConstructionManager.REQUIRED_FIELDS + ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

class CompanyConstructionManager(ConstructionManager):
    name = models.CharField(max_length=30)

    REQUIRED_FIELDS = ConstructionManager.REQUIRED_FIELDS + ['name']

    def __str__(self):
        return f"{self.name}"
    
    def company_name(self):
        return self.name
    
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
