from sqlalchemy import insert, select, update, delete
from datetime import datetime
from src.database.models import users, tasks, subtasks 


def insert_user(username, password, email):
    return insert(users).values(
        username=username, password=password, email=email
    )

def select_all_users():
    return select(users)

def select_user_by_email(email):
    return select(users).where(users.c.email == email)

def delete_user(user_id):
    return delete(users).where(users.c.id == user_id)


def insert_task(user_id, name, due_date=None):
    return insert(tasks).values(
        user_id=user_id,
        task_name=name,
        due_date=due_date
    )

def select_tasks_by_user(user_id):
    return select(tasks).where(tasks.c.user_id == user_id)

def update_task_status(task_id, status):
    return update(tasks).where(tasks.c.id == task_id).values(
        status=status,
        updated_at=datetime.utcnow()
    )

def delete_task(task_id):
    return delete(tasks).where(tasks.c.id == task_id)


def insert_subtask(task_id, name, due_date=None):
    return insert(subtasks).values(
        task_id=task_id,
        name=name,
        due_date=due_date
    )

def select_subtasks_by_task(task_id):
    return select(subtasks).where(subtasks.c.task_id == task_id)

def update_subtask_status(subtask_id, status):
    return update(subtasks).where(subtasks.c.id == subtask_id).values(
        status=status,
        updated_at=datetime.utcnow()
    )

def delete_subtask(subtask_id):
    return delete(subtasks).where(subtasks.c.id == subtask_id)