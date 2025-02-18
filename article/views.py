from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from .models import *
from random import sample

# Create your views here.
def article_list(request, ArticleCategorySlug=None):
    # Use In Template
    categories = ArticleCategory.objects.all()
    tags = Tag.objects.all().order_by('-popularity')[:6]
    last_articles = Article.objects.all().order_by('-date')[:2]

    if ArticleCategorySlug:
        # Get Articles by Category
        try:
            # Category Exists
            category = get_object_or_404(ArticleCategory, slug=ArticleCategorySlug)
            articles = category.articles.all().order_by('-date')
        except ArticleCategory.DoesNotExist:
            # Category Doesn't Exist
            return render(request, '404.html', {'massage': 'دسته بندی مقاله مورد نیاز موجود نمیباشد'})
    else:
        # Get All Articles
        category = None
        articles = Article.objects.all().order_by('-date')

    # Search Article
    search_query = request.GET.get('search', '')
    if search_query:
        articles = articles.filter(title__icontains=search_query)

    # Sorting Articles
    sort_option = request.GET.get('sort', '')
    if sort_option == 'جدیدترین':
        articles = articles.order_by('-date')
    elif sort_option == 'قدیمی ترین':
        articles = articles.order_by('date')
    elif sort_option == 'پربازدید ترین':
        articles = articles.order_by('-view_count')

    # Tag Filter
    tag_id = request.GET.get('tag')
    if tag_id:
        try:
            tag = get_object_or_404(Tag, id=tag_id)
        except Tag.DoesNotExist:
            return render(request, '404.html', {})
        articles = articles.filter(tags=tag)

    # Pagination
    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    page_articles = paginator.get_page(page_number)

    # Template Data
    context = {
        'categories': categories,
        'tags': tags,
        'category': category,
        'articles': page_articles,
        'search_query': search_query,
        'sort_option': sort_option,
        'last_articles': last_articles
    }

    return render(request, 'article/list.html', context)

def article_detail(request, ArticleCategorySlug, ArticleSlug):
    # Get Article
    try:
        category = get_object_or_404(ArticleCategory, slug=ArticleCategorySlug)
        article = get_object_or_404(Article, slug=ArticleSlug, category=category)
        article_tags = article.tags.all()

        # Increase Article View Cout
        article.view_count += 1
        article.save()

        # Increase Article Tag Popularity
        for article_tag in article_tags:
            article_tag.popularity += 1
            article_tag.save()
    except ArticleCategory.DoesNotExist:
        # Category Doesn't Exist
        return render(request, '404.html', {'massage': 'دسته بندی مقاله مورد نیاز موجود نمیباشد'})
    except Article.DoesNotExist:
        # Article Doesn't Exist
        return render(request, '404.html', {'massage': 'مقاله مورد نیاز موجود نمیباشد'})

    # Use In Template
    categories = ArticleCategory.objects.all()
    tags = Tag.objects.all().order_by('-popularity')[:6]
    last_articles = Article.objects.all().order_by('-date')[:2]

    # Recommended Articles
    recommended_articles = []
    for tag in article_tags:
        try:
            recommended_articles.extend(get_list_or_404(Article, tag=tag))
        except Article.DoesNotExist:
            pass
    recommended_articles = sample(recommended_articles, len(article_tags)*2)

    # Templae Data
    context = {
        'categories': categories,
        'category': category,
        'article': article,
        'tags': tags,
        'article_tags': article_tags,
        'last_articles': last_articles
    }

    return render(request, 'article/detail.html', context)
