from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, 'pybo.db')
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

    #app.config.from_object(config)
    # dd
    #ORM 연결 메서드
    db.init_app(app)
    migrate.init_app(app, db)
    
    from . import models
    from .views import main_views, question_views,answer_views

    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    return app

