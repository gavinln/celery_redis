import requests

from celery import Celery
from celery.utils.log import get_task_logger

import redis

logger = get_task_logger(__name__)

app = Celery('tasks', broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

import time

@app.task
def add(x, y):
    time.sleep(5)
    return x + y


@app.task
def count_words_at_url(url, id=-1):
    if id >= 0:
        with redis.Redis(host='localhost', port=6379).lock('id_%s' % id):
            logger.warning('Used id_%s' % id)
            resp = requests.get(url)
    else:
        resp = requests.get(url)

    logger.info('Getting info for the URL {0}'.format(url))
    return len(resp.text.split())
