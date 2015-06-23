import multiprocessing

from rlock import lock, lock2
import time


def worker(num):
    """thread worker function"""
    print 'Worker:', num
    lock()
    return

if __name__ == '__main__':
    jobs = []
    for i in range(2):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
