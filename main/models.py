from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class PortfolioProject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    project = models.ForeignKey(PortfolioProject, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="portfolio_project_images/")

    def __str__(self):
        return f"Image for {self.project.title}"
    
class PrimaryImage(models.Model):
    project = models.ForeignKey(PortfolioProject, on_delete=models.CASCADE, related_name="primary_image")
    image = models.ImageField(upload_to="portfolio_project_primary_images/")

    def __str__(self):
        return f"Image for {self.project.title}"
    
class ContactRequest(models.Model):
    name = models.CharField(max_length=200)
    contact_info = models.CharField(
        max_length=200,
        validators=[
            RegexValidator(
                regex=r'^(09\d{9}|[0-9]{8}|[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$',
                message="لطفا راه ارتباطی خود را با دقت وارد کنید"
            )
        ]
    )
    description = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.description[:20]}..."
    
class ProjectRequest(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()

    # Location
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.IntegerField()
    zip_code = models.CharField(max_length=10)
    address = models.TextField()

    # Property Details
    area = models.CharField(max_length=15)
    floor_count = models.IntegerField()
    description = models.TextField(null=True, blank=True)

    # Price
    price = models.CharField(max_length=15, null=True, blank=True)

    request_date = models.DateField(auto_now_add=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.city}, {self.state}"
    
class Member(models.Model):
    image = models.ImageField(upload_to="members_images/")
    full_name = models.CharField(max_length=400)
    position = models.CharField(max_length=200)
