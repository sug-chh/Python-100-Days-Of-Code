from pprint import pprint
import requests
from bs4 import BeautifulSoup

# This script no longer works as most of the sites are dynamically rendered in the client side. It is just for reference.

response = requests.get("https://news.ycombinator.com")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser" )

headings = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for heading in headings:
    article_texts.append(heading.get_text())
    article_links.append(heading.get("href"))


spans = soup.find_all(name="span", class_= "score")
article_upvotes = [int(span.get_text().split()[0]) for span in spans]

index_of_the_article_with_highest_upvotes = (article_upvotes.index(max(article_upvotes)))

pprint(article_texts[index_of_the_article_with_highest_upvotes])
pprint(article_links[index_of_the_article_with_highest_upvotes])


