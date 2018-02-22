from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from .models import Category

def index(rs):
    all_cat = Category.objects.all()
    context = {
        'all_cat': all_cat, 
    }
    #for item in all_cat:
    #    url = '/news/' + str(item.id) + '/'
    #    html += '<a href="' + url + '">' + item.genre + '</a><br>'
    return render(rs, 'news/index.html', context)

def detail(rs, news_id):
    try:
        album = Category.objects.get(pk=news_id)
    except Album.DoesNotExist:
        raise Http404("News doesn't exist")
    return render(rs, 'news/detail.html', {'album': album})