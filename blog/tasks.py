import requests
from bs4 import BeautifulSoup
from celery import shared_task


@shared_task()
def quotes_parser():
    r = requests.get("https://quotes.toscrape.com/")
    print(r)
    # if r.status_code == 200:
    #     soup = BeautifulSoup(r.text, 'html.parser')

