from django.shortcuts import render
from carnews.news import *
from carnews.news_object_creator import *


def news(request):

    news_objects = []

    parser = NewsParser()
    news = parser.parse_news()

    for new in news:
        news_objects.append(Newsobject(news[new]))

    context = {'news': news, 'news_objects': news_objects}

    return render(request, 'carnews/news.html', context)
# Create your views here.
