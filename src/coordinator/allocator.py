from .models import Task


def allocate(tasks: list[Task], agents: list[str]) -> dict[str, list[Task]]:
    out = {a: [] for a in agents}
    for idx, task in enumerate(tasks):
        out[agents[idx % len(agents)]].append(task)
    return out
