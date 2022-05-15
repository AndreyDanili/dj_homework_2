from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    ordering = '-published_at'
    template = 'articles/news.html'
    articles = Article.objects.all().prefetch_related('scopes')
    order_articles = articles.order_by(ordering)
    context = {
        'object_list': order_articles
    }
    return render(request, template, context)
