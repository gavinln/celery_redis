import time
import click

from task_status import getTaskCount
from task_status import getTotalTaskCount

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


@click.command()
def main():
    word_counts = []

    for idx, site in enumerate(sites):
        word_counts.append(
            count_words_at_url.delay('http://' + site, idx % TASK_ID_COUNT))

    print 'submitted {} tasks'.format(len(sites))

    def isComplete(items):
        return not any(items)

    def invalidLength(items):
        return len(list(item for item in items if item is None))

    # while True:
    #     taskCount = getTaskCount()
    #     print taskCount
    #     if getTotalTaskCount(taskCount) == 0:
    #         break

    oldCount = 0
    processedCount = 0

    with click.progressbar(length=len(word_counts),
                           label='Processing') as bar:
        while True:
            for idx, word_count in enumerate(word_counts):
                if word_count and word_count.ready():
                    word_counts[idx] = None
                    processedCount = invalidLength(word_counts)
#                    print(processedCount,
#                          sites[idx], word_count.get())
                    if processedCount > oldCount:
                        updatedCount = processedCount - oldCount
                        bar.update(updatedCount)
                        oldCount = processedCount

            if processedCount == len(word_counts):
                break
            time.sleep(1)


if __name__ == "__main__":
    main()
