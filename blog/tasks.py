import requests
from bs4 import BeautifulSoup
from celery import shared_task

from blog.models import Author, Quote


@shared_task()
def quotes_parser():
    r = requests.get("https://quotes.toscrape.com/")
    page = 1
    quote_list = []
    author_list = []
    while True:

        # quote_list = []
        # author_list = []
        if r.status_code == 200:
            soup_nav = BeautifulSoup(r.text, 'html.parser').find_all('li', {'class': 'next'})
            soup = BeautifulSoup(r.text, 'html.parser').find_all('div', {'class', 'quote'})  # soup_about[0].find('a').get('href')
            if not soup_nav:
                print('больше нет цитат')
                break
            r = requests.get(f"https://quotes.toscrape.com{soup_nav[0].find('a').get('href')}")
            for i in range(len(soup)):
                author = Author.objects.filter(name=soup[i].find('small', {'class': 'author'}).text)
                if author:
                    author = Author.objects.get(name=soup[i].find('small', {'class': 'author'}).text)
                if not author:
                    a = requests.get(f"https://quotes.toscrape.com/{soup[i].find('a').get('href')}")
                    soup_author = BeautifulSoup(a.text, 'html.parser').find_all('div', {'class': 'author-description'})
                    author = Author.objects.create(
                        name=soup[i].find('small', {'class': 'author'}).text,
                        about=soup_author[0].text,
                    )
                print(author)

                quote = Quote.objects.filter(quote=soup[i].find('span', {'class': 'text'}).text)
                if not quote:
                    quote_list.append(soup[i].find('span', {'class': 'text'}).text)
                    author_list.append(author)
                if len(quote_list) == 20:
                    break
        if len(quote_list) < 20:
            page += 1
        print("len", len(quote_list))
        print("page", page)
        if len(quote_list) == 20:
            break

    Quote.objects.bulk_create([Quote(
        quote=quote_list[n],
        author=author_list[n]
    ) for n in range(len(quote_list))])
