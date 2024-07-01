import subprocess
from time import sleep
from task_model import Task


def execute_task(task: Task):
    for attempt in range(task.retries):
        try:
            result = subprocess.run(task.command, shell=True, timeout=task.timeout)
            if result.returncode == 0:
                print(f"Task {task.task_id} completed successfully.")
                return
        except subprocess.TimeoutExpired:
            print(f"Task {task.task_id} timed out.")
        print(f"Retrying task {task.task_id} in {task.retry_delay} seconds...")
        sleep(task.retry_delay)
    print(f"Task {task.task_id} failed after {task.retries} attempts.")
