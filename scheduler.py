from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
import time

from executor import execute_task
from task_model import Task


scheduler = BackgroundScheduler(executors={'default': ThreadPoolExecutor(20)})


def schedule_task(task: Task):
    scheduler.add_job(
        execute_task,
        'cron',
        **parse_cron_expression(task.schedule),
        args=[task],
        id=task.task_id
    )


def parse_cron_expression(cron_expression: str) -> dict[str, str]:
    # Implement a parser for the cron expression
    return {
        "day_of_week": "mon-fri",
        "hour": "12",
        "minute": "30"
    }


def start_scheduler(tasks: list[Task]):
    for task in tasks:
        schedule_task(task)
    scheduler.start()


tasks = [
    Task(task_id="task1", command="echo 'Hello, World!'", schedule="0 12 * * *")
]

start_scheduler(tasks)
