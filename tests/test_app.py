import pytest
from src.app import add_task, complete_task, get_tasks


def test_add_task():
    tasks = []
    task = add_task(tasks, "Learn Git")
    assert task["title"] == "Learn Git"
    assert task["completed"] is False


def test_add_empty_task():
    with pytest.raises(ValueError):
        add_task([], "")


def test_complete_task():
    tasks = []
    add_task(tasks, "Practice Git")
    task = complete_task(tasks, 1)
    assert task["completed"] is True


def test_task_not_found():
    with pytest.raises(ValueError):
        complete_task([], 10)


def test_get_tasks():
    tasks = []
    add_task(tasks, "Learn GitHub")
    assert len(get_tasks(tasks)) == 1