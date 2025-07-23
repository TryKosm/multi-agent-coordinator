from .models import Task


def plan(tasks: list[Task]) -> list[Task]:
    return sorted(tasks, key=lambda t: t.priority, reverse=True)
