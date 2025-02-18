from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from .models import Article, ArticleCategory, Tag

# Customize the ArticleCategory admin
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # Show name and slug in the list view
    prepopulated_fields = {'slug': ('name',)}  # Automatically generate slug from name
    search_fields = ['name']  # Add search functionality

# Customize the Article admin
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'view_count')  # Show these fields in the list view
    list_filter = ('category', 'date', 'tags')  # Add filters for category, date, and tags
    search_fields = ['title', 'body']  # Add search functionality for title and body
    prepopulated_fields = {'slug': ('title',)}  # Automatically generate slug from title
    autocomplete_fields = ['tags']  # Enable autocomplete for tags
    list_editable = ('view_count',)  # Allow editing the view count directly from the list view
    raw_id_fields = ('category',)  # Use raw ID field for category (if you have many categories)

    formfield_overrides = {
        models.TextField: {
            'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})
        },
    }

# Customize the Tag admin (optional)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

# Register the models with admin
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Tag, TagAdmin)
