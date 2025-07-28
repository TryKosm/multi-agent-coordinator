from coordinator.conflicts import detect_conflicts


def test_detect_conflicts_for_mismatched_status() -> None:
    rows = [{"task_id": "1", "status": "ok"}, {"task_id": "1", "status": "failed"}]
    assert detect_conflicts(rows) == ["1"]
