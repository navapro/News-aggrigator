import requests
from bs4 import BeautifulSoup
import smtplib, ssl

news_site = "https://techcrunch.com/"


class aggregator:

    def __init__(self,url):
        self.website = requests.get(url).text
        self.headlines = []
        self.links = []
        self.set = {}

    def filter(self):
        soup = BeautifulSoup(self.website, 'html.parser')
        for link in soup.find_all('a'):
            current = link.text.strip('\n')
            current = current.strip('\t')
            current = current.replace(u"\u2018", "'").replace(u"\u2019", "'")
            self.headlines.append(current)
            self.links.append(link.get('href'))

        print(self.headlines)
        new_headline = []
        for i in range(0,len(self.headlines)-2):
            if self.headlines[i] == "":
                new_headline.append(self.headlines[i+1])

        self.headlines = new_headline

        print(self.headlines)
        for j in range(len(self.headlines)):
            self.set[self.headlines[j]] = self.links[j]


new = aggregator(news_site)
new.filter()
print(new.set)
email_body = ""

for k in new.set:
    email_body = email_body + k +"\n" + new.set[k] +"\n"

print(email_body)



port = 465  # For SSL
password = input("Type your password and press enter: ")
smtp_server = "smtp.gmail.com"
sender_email = "morning.newsletter.tech@gmail.com"
receiver_email = "krishnanaveen858@gmail.com"
message = """
Subject: Good Morning Newsletter

%s

This message is sent from Python."""%email_body
# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


#TODO: send html emial
#TODO: different websites

