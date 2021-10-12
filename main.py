import requests
from bs4 import BeautifulSoup
import smtplib, ssl

news_site = "https://techcrunch.com/"
keyword = "tesla"


class aggregator:

    def __init__(self,keyword,url):
        self.key = keyword
        self.website = requests.get(url).text
        self.headlines = []
        self.links = []
        self.set = {}

    def filter(self):
        soup = BeautifulSoup(self.website, 'html.parser')
        for link in soup.find_all('a'):
            current = link.text.strip('\n')
            current = current.strip('\t')
            self.headlines.append(current)
            self.links.append(link.get('href'))


        new_headline = []
        for i in range(0,len(self.headlines)-2, 3):
            new_headline.append(self.headlines[i])

        self.headlines = new_headline

        for j in range(len(self.headlines)):
            self.set[self.headlines[j]] = self.links[j]


new = aggregator(keyword,news_site)
new.filter()
print(new.set)




port = 465  # For SSL
password = input("Type your password and press enter: ")
smtp_server = "smtp.gmail.com"
sender_email = "morning.newsletter.tech@gmail.com"
receiver_email = "krishnanaveen858@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""
# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

