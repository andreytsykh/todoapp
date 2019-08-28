from flask import request, Response, jsonify
from database import db_session
from models import TodoList, Task


def create_todo_lists():
    json_data = request.json
    lists = json_data['lists']
    for todo_list in lists:
        db_session.add(TodoList(**todo_list))
    db_session.commit()
    return jsonify('Success')


def add_task(list_id):
    json_data = request.json
    task = Task(todo_list_id=list_id, **json_data['task'])
    todo_list = TodoList.query.filter_by(id=list_id).first()
    todo_list.tasks.append(task)
    db_session.add(task)
    db_session.add(todo_list)
    db_session.commit()
    return jsonify('Success')


def get_all_tasks(list_id):
    tasks = Task.query.filter(Task.todo_list.has(id=list_id)).all()
    tasks_list = []
    for task in tasks:
        tasks_list.append(task.as_dict())
    return jsonify({'tasks': tasks_list})
