import werkzeug.exceptions
from flask import Flask
from database import db_session, init_db


def create_app():
    app = Flask(__name__)
    from database import db_session
    from taskapi import tasks_bp
    from todoapi import list_bp

    app.register_blueprint(tasks_bp, url_prefix='/tasks')
    app.register_blueprint(list_bp)

    @app.teardown_appcontext
    def shutdown_db_session(exception=None):
        db_session.remove()

    @app.cli.command("init-db")
    def init_db_command():
        init_db()

    @app.errorhandler(werkzeug.exceptions.BadRequest)
    def handle_bad_request(e):
        return 'bad request!', 400

    return app

