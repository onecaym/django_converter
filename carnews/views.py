from django.shortcuts import render
from carnews.news import *
from carnews.article import *

# Show only official car news from Motor1.com


def news(request):

    # News storage
    all_news = []

    # Initialize and call news parser
    parser = News_parser()
    parsed_news = parser.parse_news()
    for key, value in parsed_news.items():
        print(value.keys())

    for article in parsed_news:

        # Update storage with articles
        all_news.append(Article(parsed_news[article]))

    context = {'parsed_news': parsed_news, 'all_news': all_news}

    return render(request, 'carnews/news.html', context)
# Create your views here.
