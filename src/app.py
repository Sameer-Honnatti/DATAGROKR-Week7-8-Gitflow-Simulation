def add_task(tasks, title):
    title = title.strip()

    if not title:
        raise ValueError("Task title cannot be empty")

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    return task


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return task

    raise ValueError("Task not found")


def get_tasks(tasks):
    return tasks


def main():
    tasks = []

    add_task(tasks, "Learn Git")
    add_task(tasks, "Practice Gitflow")

    complete_task(tasks, 1)

    for task in get_tasks(tasks):
        status = "Completed" if task["completed"] else "Pending"
        print(f'{task["id"]}. {task["title"]} - {status}')


if __name__ == "__main__":
    main()