from executor import execute_task
from task_model import Task


def check_dependencies(task: Task, executed_tasks: dict[str, bool]) -> bool:
    for dependency in task.dependencies:
        if not executed_tasks.get(dependency, False):
            return False
    return True


executed_tasks = {}


def execute_task_with_dependencies(task: Task):
    if check_dependencies(task, executed_tasks):
        execute_task(task)
        executed_tasks[task.task_id] = True
    else:
        print(f"Task {task.task_id} dependencies not met.")
