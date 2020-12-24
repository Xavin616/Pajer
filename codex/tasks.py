from bs4 import BeautifulSoup as bs
from celery import Celery
from time import sleep
from datetime import datetime
from plyer import notification
from celery.schedules import crontab
from celery import shared_task
from .models import Source, Headline

import requests, json, os, webbrowser

app = Celery('tasks', broker='amqp://localhost')

sources = Source.objects.all()

@shared_task
def notifier(title, body):
    notification.notify(
        title=title,
        message=body,
        timeout=10
    )

@shared_task(serializer='json')
def save_function(list):
    for article in list:
        head = Headline.objects.filter(title=article['title'], link=article['link'])
        if head:
            continue
        else:
            Headline.objects.create(
                title=article['title'],
                link=article['link'],
                source=Source.objects.get(name=article['source']),
                description=article['description'],
                date=article['date']
            )
        
@shared_task
def rss_feeder(source, url):
    article_list = []
    request = requests.get(url)
    soup = bs(request.text, features='xml')
    soup = soup.findAll('item')
    for a in soup:
        title = a.find('title').text
        link = a.find('link').text
        date = a.find('pubDate').text
        description = a.find('description').text

        article = {
            'source': source,
            'title': title,
            'link': link,
            'description': description,
            'date':date,
        }

        article_list.append(article)
        print(f"{article['source']}: {article['title']}")
    return save_function(article_list)
        
@shared_task
def scrape():    
    for source in sources:
        rss_feeder(source.name, source.feed)
    print('Done!')
#    notifier('Success', 'Feed Aggregator is done!')

