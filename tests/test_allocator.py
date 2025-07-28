from coordinator.allocator import allocate
from coordinator.models import Task


def test_allocate_round_robin() -> None:
    assigned = allocate([Task("a", "x", 1), Task("b", "y", 1)], ["alpha", "beta"])
    assert len(assigned["alpha"]) == 1
