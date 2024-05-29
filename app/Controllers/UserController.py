from flask import render_template, request, redirect, url_for, flash
from ..models.user import db, User
from flask_login import login_user, logout_user, current_user, login_required
from app import bcrypt
from ..forms.auth import RegistrationForm, LoginForm

def dashboard():
    user = User.query.filter_by(email=current_user.email, phone=current_user.phone).first()
    return render_template('sections/users/dashboard.html', user=user)

def submit():
    form = RegistrationForm()
    if form.validate_on_submit():
        full_name = form.full_name.data
        email = form.email.data
        phone = form.phone.data
        password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = User.query.filter_by(full_name=full_name).first()
        if user:
            flash('Username already exists.', 'danger')
            return redirect(url_for('web.submit'))
        
        new_user = User(full_name=full_name, email=email, phone=phone, password=password)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully!', 'success')
            return redirect(url_for('web.index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {e}', 'danger')
            return redirect(url_for('web.submit'))
    return render_template('sections/users/form.html', form=form)

def login():
    form = LoginForm()
    if form.validate_on_submit():
        email_or_phone = form.email_or_phone.data  # Assuming you have a single field for email or phone in your form

        user = User.query.filter((User.email == email_or_phone) | (User.phone == email_or_phone)).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('web.index'))
        else:
            flash('Login failed. Check your phone number or email and Password.', 'danger')
    return render_template('sections/users/login.html', form=form)

def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('web.index'))
