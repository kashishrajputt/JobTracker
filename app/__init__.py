from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#create database object globally
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)


    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kashish@localhost:5432/jobtracker'
    app.config['ASQLALCHEMY_TRACK_MODIFICATIONS']=False

    db.__init__(app)

    from app.routes.auth import auth_bp
    from app.routes.auth import jobs_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(jobs_bp)

    return app