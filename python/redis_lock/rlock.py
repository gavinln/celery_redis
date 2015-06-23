from __future__ import print_function

import redis
from pprint import pprint

import time
import redlock


def lock():
    server = redis.Redis(host='localhost', port=6379)
    time.sleep(2)
    #lock = server.lock('lock0').acquire(blocking=True)
    lock = server.lock('lock1', timeout=10)
    isLocked = lock.acquire(blocking_timeout=5)
    print(isLocked)
    time.sleep(2)
    print('finished sleeping')
    if isLocked:
        #lock.release()
        pass


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
