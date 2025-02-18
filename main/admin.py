from django.contrib import admin
from .models import *

# Inline for Image to display images related to each project in the same view
class ImageInline(admin.TabularInline):
    model = Image
    extra = 1  # Number of extra blank fields

# Inline for Primary_Image to display primary images related to each project in the same view
class PrimaryImageInline(admin.TabularInline):
    model = PrimaryImage
    extra = 1

@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageInline, PrimaryImageInline]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'image')

@admin.register(PrimaryImage)
class PrimaryImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'image')

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info', 'description_short')

    def description_short(self, obj):
        return f"{obj.description[:20]}..." if len(obj.description) > 20 else obj.description
    description_short.short_description = "Description"

@admin.register(ProjectRequest)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'city', 'state', 'price')
    search_fields = ('first_name', 'last_name', 'city', 'state')

@admin.register(Member)
class Member(admin.ModelAdmin):
    list_display = ('image', 'full_name', 'position')
