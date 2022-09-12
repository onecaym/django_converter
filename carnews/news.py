from bs4 import BeautifulSoup
import requests


class NewsParser(object):

    def __init__(self):
        self.newsparser = self
        self.news = {}
        url = 'https://www.motor1.com/news/category/official/'
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.text, "html.parser")

    def parse_news(self):

        for new in self.soup.findAll('div', class_='item wcom'):
            if new.find(
                'span',
                    class_='sticker type cat-official') is not None:
                title = new.find('h3').get_text()
                self.news[title] = {}
                self.news[title]['title'] = f'{title}'

                description = new.find('a', class_='text').get_text()
                self.news[title]['description'] = f'{description}'

                partial_link = new.find('a', class_='thumb zoom').get('href')
                full_link = f'https://www.motor1.com{partial_link}'
                self.news[title]['link'] = f'{full_link}'

                images_location = new.find(
                    'source', media='(min-width: 320px)')
                self.news[title]['image'] = f"{images_location['data-srcset']}"

        return(self.news)
