from bs4 import BeautifulSoup
import requests


class News_parser(object):

    def __init__(self):
        self.news_parser = self
        self.news = {}
        url = 'https://www.motor1.com/news/category/official/'
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.text, "html.parser")

    # Create news storage with titles, descriptions, links and images
    def parse_news(self):

        for article in self.soup.findAll('div', class_='item wcom'):
            if article.find(
                'span',
                    class_='sticker type cat-official') is not None:
                # Articles titles
                title = article.find('h3').get_text()
                self.news[title] = {}
                self.news[title]['title'] = f'{title}'

                # Articles descriptions
                description = article.find('a', class_='text').get_text()
                self.news[title]['description'] = f'{description}'

                # Articles links to the official site
                short_link = article.find('a', class_='thumb zoom').get('href')
                full_link = f'https://www.motor1.com{short_link}'
                self.news[title]['link'] = f'{full_link}'

                # Image for the current article
                img_location = article.find(
                    'source', media='(min-width: 320px)')
                self.news[title]['image'] = f"{img_location['data-srcset']}"

        return(self.news)
