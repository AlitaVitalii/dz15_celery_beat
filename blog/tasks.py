import requests
from bs4 import BeautifulSoup
from celery import shared_task
from django.core.mail import send_mail

from blog.models import Author, Quote


@shared_task()
def quotes_parser():
    r = requests.get("https://quotes.toscrape.com/")
    quote_list = []
    author_list = []

    while True:
        if r.status_code == 200:
            soup_nav = BeautifulSoup(r.text, 'html.parser').find_all('li', {'class': 'next'})
            soup = BeautifulSoup(r.text, 'html.parser').find_all('div', {'class', 'quote'})

            for i in range(len(soup)):
                author = Author.objects.filter(name=soup[i].find('small', {'class': 'author'}).text).first()
                if not author:
                    a = requests.get(f"https://quotes.toscrape.com/{soup[i].find('a').get('href')}")
                    soup_author = BeautifulSoup(a.text, 'html.parser').find_all('div', {'class': 'author-description'})
                    author = Author.objects.create(
                        name=soup[i].find('small', {'class': 'author'}).text,
                        about=soup_author[0].text,
                    )

                quote = Quote.objects.filter(quote=soup[i].find('span', {'class': 'text'}).text)
                if not quote:
                    quote_list.append(soup[i].find('span', {'class': 'text'}).text)
                    author_list.append(author)

                if len(quote_list) == 5:
                    break

            if not soup_nav:
                if len(quote_list) < 5:
                    send_mail(
                        'Quote',
                        'Новых цитат больше нет',
                        ['admin@mail.com'],
                        ["support@example.com"],
                        fail_silently=False,
                    )
                break
            r = requests.get(f"https://quotes.toscrape.com{soup_nav[0].find('a').get('href')}")

        if len(quote_list) == 5:
            break

    Quote.objects.bulk_create([Quote(
        quote=quote_list[n],
        author=author_list[n]
    ) for n in range(len(quote_list))])
