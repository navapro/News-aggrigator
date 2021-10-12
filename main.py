import requests
from bs4 import BeautifulSoup

news_site = "https://techcrunch.com/"
keyword = "tesla"


class aggregator:

    def __init__(self,keyword,url):
        self.key = keyword
        self.website = requests.get(url).text
        self.headlines = []
        self.links = []

    def filter(self):
        soup = BeautifulSoup(self.website, 'html.parser')
        for link in soup.find_all('a'):
            current = link.text.strip('\n')
            current = current.strip('\t')
            self.headlines.append(current)
            self.links.append(link.get('href'))

        print(self.headlines)

        for i in range(len(self.headlines),2):







new = aggregator(keyword,news_site)
new.filter()
print(new.links)
print(new.headlines)