from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#create database object globally
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)


    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kashish@localhost:5432/jobtracker'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    db.init_app(app)

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)
    from app.routes.jobs import job_bp
    app.register_blueprint(job_bp)

    with app.app_context():
        db.create_all()
    return app