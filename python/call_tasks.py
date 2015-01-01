#!/usr/bin/python

from tasks import add

# synchronous
print add(4, 4)

# Asynchronous
task = add.delay(4, 4)
print task

from celery.result import AsyncResult
print AsyncResult(task.task_id).get()

# synchronous
print add.delay(4, 4).get()

#from tasks import count_words_at_url
#word_counts = [
#    count_words_at_url.delay('http://wsj.com'),
#    count_words_at_url.delay('http://nytimes.com')
#]
#
#
#print 'wsj: ',  word_counts[0].get()
#print 'nytimes: ', word_counts[1].get()
