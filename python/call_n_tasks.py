import time

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


def main():
    word_counts = []

    for idx, site in enumerate(sites):
        word_counts.append(
            count_words_at_url.delay('http://' + site, idx % TASK_ID_COUNT))

    print 'submitted {} tasks'.format(len(sites))

    def isComplete():
        return not any(word_counts)

    while True:
        taskCount = getTaskCount()
        print taskCount
        if getTotalTaskCount(taskCount) == 0:
            break

    return

    while True:
        for idx, word_count in enumerate(word_counts):
            if word_count and word_count.ready():
                print(sites[idx], word_count.get())
                word_counts[idx] = None
        if isComplete():
            break
        time.sleep(1)


if __name__ == "__main__":
    main()
