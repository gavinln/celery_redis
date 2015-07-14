from celery.task.control import inspect
from celery import Celery

from collections import namedtuple

app = Celery('tasks', broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')


inspector = inspect(app=app)


def count_tasks(taskList):
    for key, value in taskList.items():
        return len(value)


TaskCount = namedtuple(
    'TaskCount', ['scheduled', 'revoked', 'active', 'reserved'])


def getTaskCount():
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
