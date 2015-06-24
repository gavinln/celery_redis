import multiprocessing

from rlock import lock, lock2
import time


def worker(num):
    """thread worker function"""
    lock(num)
    return

if __name__ == '__main__':
    jobs = []
    for i in range(6):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
