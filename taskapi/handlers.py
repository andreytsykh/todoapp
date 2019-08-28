from flask import Response, jsonify, request
from models import Task
from database import db_session


def delete(task_id):
    task = Task.query.filter_by(id=task_id).first()
    db_session.delete(task)
    db_session.commit()
    return jsonify("Success")


def edit(task_id):
    json_data = request.json
    db_session.query(Task).filter_by(id=task_id).update(json_data)
    db_session.commit()
    return jsonify("Success")


def finish(task_id):
    db_session.query(Task).filter_by(id=task_id).update({'status': 'DONE'})
    db_session.commit()
    return jsonify("Success")
