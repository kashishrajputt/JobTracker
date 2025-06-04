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
    if request.method == "POST":
        new_job = Job(
            comapny=request.form['comapny'],
            position=request.form['position'],
            status = request.form['status'],
            notes=request.form['notes'],
            deadline = datetime.strptime(request.form['deadline'],'%Y-%m-%d')
            if request.form['deadline'] else None
        )
        db.session.add(new_job)
        db.session.commit()
        flash('New Job added successfully!')

    return redirect(url_for('jobs.view_jobs'))

@job_bp.route('/edit/<int:id>', methods =['GET','POST'])
def edit_job(id):
    job = Job.query.get_or_404(id)
    if request.method == 'POST':
        job.company = request.form['company']
        job.position = request.form['position']
        job.status = request.form['status']
        job.notes = request.form['notes']
        job.deadline = datetime.strptime(request.form['deadline'], '%Y-%m-%d') if request.form['deadline'] else None
        db.session.commit()
        return redirect('/')
    return redirect(url_for('jobs.view_jobs'))

@job_bp.route('/delete/<int:id>')
def delete_job(id):
    job = Job.query.get_or_404(id)
    db.session.delete(job)
    db.session.commit()
    return redirect('/')
