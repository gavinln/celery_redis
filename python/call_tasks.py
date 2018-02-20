#!/usr/bin/python

import time

from tasks import add
from tasks import count_text_at_url
from celery.result import AsyncResult


def temp():
    # synchronous
    print(add(4, 4))

    # Asynchronous
    task = add.delay(4, 4)
    print(task)

    print(AsyncResult(task.task_id).get())

    # synchronous
    print(add.delay(4, 4).get())


urls = [
    "Google.com",
    "Youtube.com",
    "Facebook.com",
    "Baidu.com",
    "Yahoo.com",
    "Wikipedia.org",
    "Qq.com",
    "Sohu.com",
    "Taobao.com",
    "Tmall.com",
    "Live.com",
    "Amazon.com",
    "Vk.com",
    "Twitter.com",
    "360.cn",
    "Sina.com.cn",
    "Linkedin.com",
    "Jd.com",
    "Reddit.com",
    "Weibo.com",
    "Hao123.com",
    "Yandex.ru",
    "Ebay.com",
    "Msn.com",
    "Wordpress.com",
    "Bing.com",
    "T.co",
    "Onclkds.com",
    "Ok.ru",
    "Aliexpress.com",
    "Netflix.com",
    "Blogspot.com",
    "Microsoft.com",
    "Tumblr.com"
]


tasks = []

for url in urls:
    tasks.append(count_text_at_url.delay('http://' + url))

start = time.time()

while any(tasks):
    for idx, task in enumerate(tasks):
        if task and task.ready():
            result = task.get()
            tasks[idx] = None
            print('url = {}, result = {}'.format(urls[idx], result))

elapsed = time.time() - start
print('elapsed = {:.2f}'.format(elapsed))
