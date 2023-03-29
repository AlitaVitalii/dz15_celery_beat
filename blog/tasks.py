import requests
from bs4 import BeautifulSoup


def quotes_parser():
    r = requests.get("https://quotes.toscrape.com/")

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')

