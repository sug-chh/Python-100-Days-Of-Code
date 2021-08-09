from bs4 import BeautifulSoup
import requests


# Code to get 100 best movies from Hollywood reporter
# This script no longer works as most of the sites are dynamically rendered in the client side. It is just for reference
def get_movies():
    response = requests.get(url="https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512")
    hollywood_reporter_page = response.text

    soup = BeautifulSoup(hollywood_reporter_page, "html.parser")
    # print(soup.prettify())

    h1s = soup.findAll(name="h1", class_="list-item__title")

    top_movies = [h1.get_text() for h1 in h1s]
    top_movies.reverse()
    return top_movies

try:
    with open("100_greatest_movies_to_watch.txt", mode="r") as data:
        print(data.read())

except FileNotFoundError:
    with open("100_greatest_movies_to_watch.txt", mode="w") as data:
        top_movies = get_movies()
        for movie in top_movies:
            data.write(f"{movie}\n")



