import requests

from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

app = Celery('tasks', broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')


@app.task
def add(x, y):
    return x + y


@app.task(name='tasks.count words at url')
def count_words_at_url(url):
    resp = requests.get(url)
    logger.info('Getting info for the URL {0}'.format(url))
    return len(resp.text.split())
