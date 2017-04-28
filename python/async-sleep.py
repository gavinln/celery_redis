'''
Example from web page:
https://hackernoon.com/asyncio-for-the-working-python-developer-5c468e6e2e8e

ohttp://masnun.rocks/2016/10/06/async-python-the-different-forms-of-concurrency/
'''


import time
import asyncio

start = time.time()


def tic():
    return 'at %1.1f seconds' % (time.time() - start)


async def task1():
    print('task1 started work: {}'.format(tic()))
    await asyncio.sleep(2)
    print('task1 ended work: {}'.format(tic()))


async def task2():
    print('task2 started work: {}'.format(tic()))
    await asyncio.sleep(1)
    print('task2 ended work: {}'.format(tic()))


def task3():
    print('task3 started work: {}'.format(tic()))
    time.sleep(2)
    print('task3 ended work: {}'.format(tic()))


def task4():
    print('task4 started work: {}'.format(tic()))
    time.sleep(1)
    print('task4 ended work: {}'.format(tic()))


loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(task1()),
    asyncio.ensure_future(task2()),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

task3()
task4()
