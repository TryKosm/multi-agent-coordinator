from coordinator.models import Task
from coordinator.planner import plan


def test_plan_orders_by_priority() -> None:
    out = plan([Task("a", "x", 1), Task("b", "y", 3)])
    assert out[0].task_id == "b"
