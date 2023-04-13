from django.test import TestCase
from carnews.news import *

class NewsParserTestCase(TestCase):
    
    def test_news_parser(self):
        test_article = {'test_heading': 
        {'title': 'test_heading',
        'description': 'test_description',
        'link': 'test_link',
        'image': 'test_image'}}
        parser = News_parser()
        articles = parser.parse_news()

        for key, value in articles.items():
            for test_key, test_value in test_article.items():
                keys = value.keys()
                test_keys = test_value.keys()

                self.assertEqual(keys, test_keys)