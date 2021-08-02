

# Create your views here.
from django.http import HttpResponse
from .models import News
from django.shortcuts import render  # для рендера шаблонов




def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'news/index.html',context)

def index2(request):
    news = News.objects.all()
    res = '<h1>Список новостей</h1>'
    for item in news :
        res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n'
    return HttpResponse(res)

def test(request):

    return HttpResponse('<h1>Тестовая страница</h1>')