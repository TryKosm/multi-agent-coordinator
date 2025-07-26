def reconcile(conflicts: list[str]) -> dict[str, str]:
    return {task_id: "manual_review" for task_id in conflicts}
