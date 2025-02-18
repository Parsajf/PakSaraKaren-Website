from django.urls import path
from .views import *

urlpatterns = [
    path('', article_list, name="articles"),
    path('<slug:ArticleCategorySlug>/', article_list, name="articles-by-category"),
    path('<slug:ArticleCategorySlug>/<slug:ArticleSlug>/', article_detail, name="article-detail"),
]
