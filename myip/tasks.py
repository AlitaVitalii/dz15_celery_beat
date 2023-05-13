import requests
from bs4 import BeautifulSoup
from celery import shared_task
from django.core.mail import send_mail

from myip.models import Myip


@shared_task()
def ip_parser():
    r = requests.get("https://2ip.ua/ru/")
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser').find('div', {'class', 'ip'})
        myip = Myip.objects.create(ip_txt=soup.text[6:20].replace('\n', ''))
        send_mail(
            f'{myip}',
            f'{myip.ip_txt}\n{myip.pubdate}',
            "alita.v@ukr.net",
            ["alita.avs@gmail.com"],
            fail_silently=False,)


