from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import User
from werkzeug.security import check_password_hash, generate_password_hash
from app import db

# Create a blueprint for authentication-related routes
auth_bp = Blueprint('auth',__name__)

# User Registration 
#------------------------------------------------------------------------------------------
@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    # Handle for submission
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        #check for existing users
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose another.', 'warning')
            return redirect(url_for('auth.register'))

        # hash password for secure storage
        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password=hashed_pw)
        # saving user to database
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

#user login route
#-----------------------------------------------------------------------------
@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    # handles form submission
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # fetch user from database
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            #store user id in session to maintain login state
            session['user_id'] = user.id
            flash('Login Successful', 'success')
            return redirect(url_for('jobs.view_jobs'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

#user logout
#--------------------------------------------------------------------------------
@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out', 'info')
    return redirect(url_for('auth.login'))

