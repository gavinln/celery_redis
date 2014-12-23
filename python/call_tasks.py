from tasks import count_words_at_url
from tasks import add

#print add.delay(4, 4).get()

word_counts = [
    count_words_at_url.delay('http://wsj.com'),
    count_words_at_url.delay('http://nytimes.com')
]


print 'wsj: ',  word_counts[0].get()
print 'nytimes: ', word_counts[1].get()
