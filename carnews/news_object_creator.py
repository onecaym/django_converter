from carnews.news import *


class Newsobject():

    def __init__(self, one_new):
        self.title = one_new['title']
        self.link = one_new['link']
        self.description = one_new['description']
        self.image = one_new['image']
