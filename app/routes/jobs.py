from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import Job
from datetime import datetime

#blueprint for job related routes
job_bp = Blueprint('jobs', __name__)

# View All Jobs for Logged-in User
#-------------------------------------------------------------------------
@job_bp.route('/')
def view_jobs():
    """
    Display all jobs associated with the currently logged-in user.

    Redirects to login page if the user is not authenticated.
    Otherwise, fetches and displays all jobs linked to the current user's ID.

    Returns:
        Rendered template (jobs.html) with user's jobs.
    """

    # redirect to user login if not authenticated
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    #fetch job only for logged-in user
    jobs = Job.query.filter_by(user_id=session['user_id']).all()

    #render job list template
    return render_template('jobs.html', jobs=jobs)

@job_bp.route('/add', methods = ['GET','POST'])
def add_jobs():
    """
    Add a new job entry for the logged-in user.

    Handles both GET and POST requests:
        - GET: Displays the job addition form.
        - POST: Submits form data to create a new job and saves it in the database.

    Returns:
        Redirects to job list page upon success, or login page if unauthenticated.
    """

    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    
    new_job = Job(
            company=request.form['company'],
            position=request.form['position'],
            status = request.form['status'],
            notes=request.form['notes'],
            deadline = datetime.strptime(request.form['deadline'],'%Y-%m-%d')  if request.form['deadline'] else None,
            user_id=session['user_id']  # link to user
    )
    db.session.add(new_job)
    db.session.commit()
    flash('New Job added successfully!')

    return redirect(url_for('jobs.view_jobs'))

@job_bp.route('/edit/<int:id>', methods =['GET','POST'])
def edit_job(id):
    """
    Edit an existing job entry for the logged-in user.

    Args:
        id (int): ID of the job to edit.

    On GET: Displays the job form with existing values.
    On POST: Updates the job record with form data.

    Returns:
        Redirects to job list page upon successful update.
        Renders form with prefilled data if method is GET.
        Redirects to login if unauthenticated or unauthorized.
    """  
    job = Job.query.get_or_404(id)

    # Ensure job belongs to the logged-in user
    if job.user_id != session.get('user_id'):
        flash("Unauthorized access to job edit.", 'danger')
        return redirect(url_for('jobs.view_jobs'))
    
    if request.method == 'POST':
        job.company = request.form['company']
        job.position = request.form['position']
        job.status = request.form['status']
        job.notes = request.form['notes']
        job.deadline = datetime.strptime(request.form['deadline'], '%Y-%m-%d') if request.form['deadline'] else None
        db.session.commit()
        return redirect(url_for('jobs.view_jobs'))
    
    # Fetch all jobs for display, mark one as editable
    jobs = Job.query.filter_by(user_id=session['user_id']).all()
    return render_template('jobs.html', jobs=jobs, job_to_edit=job)

@job_bp.route('/delete/<int:id>', methods=['POST'])
def delete_job(id):
    """
    Delete a job entry by its ID if it belongs to the current user.

    Args:
        id (int): ID of the job to delete.

    Returns:
        Redirects to job list page upon successful deletion.
        Redirects to login or job list if unauthenticated or unauthorized.
    """
    job = Job.query.get_or_404(id)
    db.session.delete(job)
    db.session.commit()
    flash("Job deleted successfully!", "info")
    return redirect(url_for('jobs.view_jobs'))
