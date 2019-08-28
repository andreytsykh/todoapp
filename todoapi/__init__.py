from flask import Blueprint
from todoapi import handlers

list_bp = Blueprint('lists', __name__)

list_bp.add_url_rule('/', view_func=handlers.create_todo_lists, methods=['POST', ])
list_bp.add_url_rule('/<int:list_id>/tasks', view_func=handlers.add_task, methods=['POST', ])
list_bp.add_url_rule('/<int:list_id>/tasks', view_func=handlers.get_all_tasks, methods=['GET', ])
