from flask import Blueprint
import taskapi.handlers

tasks_bp = Blueprint('tasks', __name__)

tasks_bp.add_url_rule('/<int:task_id>', view_func=handlers.delete, methods=['DELETE', ])
tasks_bp.add_url_rule('/<int:task_id>', view_func=handlers.edit, methods=['PATCH', ])
tasks_bp.add_url_rule('/<int:task_id>/finish', view_func=handlers.finish, methods=['PATCH', ])


