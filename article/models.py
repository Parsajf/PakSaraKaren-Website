from django.db import models
from django.urls import reverse

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    popularity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class ArticleCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("article_list", args=[self.slug])
    
    def get_article_count(self):
        return self.articles.count()
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Article(models.Model):
    category = models.ForeignKey(ArticleCategory, related_name="articles", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='articles/%Y/%m/%d', blank=True)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    persian_date = models.CharField(max_length=20)
    view_count = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name='articles')


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article-detail", args=[self.category.slug, self.slug])
