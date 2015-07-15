import time
import click

from task_status import getTaskCount
from task_status import getTotalTaskCount
from task_status import displayTaskProgressBar

from tasks import count_words_at_url

sites = [
    'go.com',
    'vk.com',
    'cnn.com',
    'msn.com',
    'live.com',
    'imdb.com',
    'ebay.com',
    'youku.com',
    'apple.com',
    'imgur.com',
    'yahoo.com',
    'adobe.com',
    'amazon.com',
    'adcash.com',
    'PayPal.com',
    'tumblr.com',
    'reddit.com',
    'blogger.com',
    'dropbox.com',
    'alibaba.com',
    'walmart.com',
    'bestbuy.com',
    'twitter.com',
    'espn.go.com',
    'netflix.com',
    'youtube.com',
    'blogspot.com',
    'flipkart.com',
    'Buzzfeed.com',
    'facebook.com',
    'linkedin.com',
    'microsoft.com',
    'pinterest.com',
    'wordpress.com',
    'instagram.com',
    'aliexpress.com',
    'dailymotion.com',
    'stackoverflow.com',
    'huffingtonpost.com',
    'Onclickads.net',
    'Cntv.cn',
    'craigslist.org',
    'bbc.co.uk',
    'wikipedia.org',
    'odnoklassniki.ru',
    't.co'
]

TASK_ID_COUNT = 5  # number tasks from 0 to 4


def displayWebSiteCounts(tasks, names):
    def isComplete(tasks):
        return not any(tasks)

    while True:
        for idx, task in enumerate(tasks):
            if task and task.ready():
                print(names[idx], task.get())
                tasks[idx] = None
        if isComplete(tasks):
            break
        time.sleep(1)


@click.command()
def main():
    word_counts = []

    for idx, site in enumerate(sites):
        word_counts.append(
            count_words_at_url.delay('http://' + site, idx % TASK_ID_COUNT))

    print 'submitted {} tasks'.format(len(sites))

    displayWebSiteCounts(word_counts, sites)

    # displayTaskProgressBar(word_counts)


if __name__ == "__main__":
    main()
