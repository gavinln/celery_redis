from __future__ import print_function

import redis
from pprint import pprint

import time
import random
import redlock

import datetime


class RedisLock(object):
    def __init__(self, server, lockCount, timeout):
            self.server = server
            self.lockCount = lockCount
            self.name = 'lock' + str(random.randint(0, self.lockCount - 1))
            self.lock = self.server.lock(self.name, timeout)
            self.isLocked = None
            self.createTime = datetime.datetime.now()
            self.acquireTime = None
            self.releaseTime = None

    def acquire(self, blocking_timeout):
        self.isLocked = self.lock.acquire(blocking_timeout)
        if self.isLocked:
            self.acquireTime = datetime.datetime.now()
        return self.isLocked

    def release(self):
        if self.isLocked:
            self.releaseTime = datetime.datetime.now()
            self.lock.release()

    def __str__(self):
        acquireDiff = self.acquireTime - self.createTime
        releaseDiff = self.releaseTime - self.acquireTime
        return 'lock={}, create={}, acquire={}, release={}'.format(
            self.name, self.createTime, acquireDiff, releaseDiff)


def lock(num):
    server = redis.Redis(host='localhost', port=6379)
    #lock = server.lock('lock1', timeout=10)
    lock = RedisLock(server, 2, timeout=10)
    try:
        while True:
            isLocked = lock.acquire(blocking_timeout=5)
            print('Worker {}: {}'.format(num, isLocked))
            if isLocked:
                time.sleep(1)
                print('Worker {}: finished'.format(num))
                break
            else:
                time.sleep(1)
    finally:
        lock.release()
        print(lock)


def lock2():
    dlm = redlock.Redlock([{"host": "localhost", "port": 6379, "db": 0}, ])
    time.sleep(2)
    my_lock = dlm.lock('lock0', 10000)
    while not my_lock:
        time.sleep(2)
        my_lock = dlm.lock('lock0', 10000)
    time.sleep(2)
    dlm.unlock(my_lock)


def redis_info(server):
    pprint(server.info())


def main():
    print('in main')
    server = redis.Redis(host='localhost', port=6379)
    return server


if __name__ == '__main__':
    logging.basicConfig(level=DEBUG)
    main()
