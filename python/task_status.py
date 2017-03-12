from celery.task.control import inspect
from celery import Celery

from collections import namedtuple
import copy

import click
import time


def getInspector():
    app = Celery('tasks', broker='redis://localhost:6379/0',
                 backend='redis://localhost:6379/0')

    inspector = inspect(app=app)
    return inspector


def count_tasks(taskList):
    for key, value in taskList.items():
        return len(value)


TaskCount = namedtuple(
    'TaskCount', ['scheduled', 'revoked', 'active', 'reserved'])


def getTaskCount():
    inspector = getInspector()
    return TaskCount(
        count_tasks(inspector.scheduled()),
        count_tasks(inspector.revoked()),
        count_tasks(inspector.active()),
        count_tasks(inspector.reserved())
    )


def getTotalTaskCount(taskCount):
    return sum([
        getattr(taskCount, field) for field in taskCount._fields
        ])


def displayTaskProgressBar(tasks):
    def noneItemCount(items):
        ' number of items that are None '
        return len(list(item for item in items if item is None))

    oldCount = 0
    processedCount = 0

    with click.progressbar(length=len(tasks),
                           label='Processing') as bar:
        while True:
            for idx, task in enumerate(tasks):
                if task and task.ready():
                    tasks[idx] = None
                    processedCount = noneItemCount(tasks)
                    if processedCount > oldCount:
                        updatedCount = processedCount - oldCount
                        bar.update(updatedCount)
                        oldCount = processedCount

            if processedCount == bar.length:
                break
            time.sleep(1)
