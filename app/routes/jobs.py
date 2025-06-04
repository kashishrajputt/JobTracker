from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import Job
from datetime import datetime

job_bp = Blueprint('jobs', __name__)

@job_bp.route('/')
def view_jobs():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    jobs = Job.query.all()
    return render_template('jobs.html', jobs=jobs)

@job_bp.route('/add', methods = ['POST'])
def add_jobs():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    company = request.form.get('company')
    if company:
        new_job = Job(
            comapny=request.form['comapny'],
            position=request.form['position'],
            status = request.form['status'],
            notes=request.form['notes'],
            deadline = datetime.strptime(request.form['deadline'],'%Y-%m-%d') if request.form['deadline'] else None
        )
        db.session.add(new_job)
        db.sessiom.commit()
        flash('New Job added successfully!')

    return redirect(url_for('tasks.view'))
