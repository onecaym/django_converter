from carnews.news import *

# Contains all info about each article


class Article():

    def __init__(self, article):
        self.title = article['title']
        self.link = article['link']
        self.description = article['description']
        self.image = article['image']
