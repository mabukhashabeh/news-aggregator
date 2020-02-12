import requests
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from django.views.generic import ListView
from news.models import News
import dateutil.parser


def scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.skysports.com/news-wire"
    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    news = soup.find_all('div', {'class': 'news-list__item news-list__item--show-thumb-bp30'})

    for article in news:
        title = article.find('a', {'class': 'news-list__headline-link'}).string
        description = article.find('p', {'class': 'news-list__snippet'}).string
        image = article.find('img').get('data-src')
        url = article.find('a', {'class': 'news-list__headline-link'}).get('href')
        tag = article.find('a', {'class': 'label__tag'}).string
        date = article.find('span', {'class': 'label__timestamp'}).string

        News.objects.update_or_create(title=title, description=description, image=image, url=url, tag=tag,
                                   date=dateutil.parser.parse(date))

    return redirect('../')


class ListNews(ListView):
    template_name = 'news/home.html'
    model = News
    paginate_by = 9
    ordering = '-date'




