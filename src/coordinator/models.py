from dataclasses import dataclass


@dataclass
class Task:
    task_id: str
    summary: str
    priority: int
