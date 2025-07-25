def detect_conflicts(results: list[dict[str, str]]) -> list[str]:
    seen = {}
    conflicts = []
    for row in results:
        key = row["task_id"]
        value = row["status"]
        if key in seen and seen[key] != value:
            conflicts.append(key)
        seen[key] = value
    return conflicts
