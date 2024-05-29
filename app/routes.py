from flask import Blueprint, render_template
from flask_login import login_required

from .Controllers import UserController

# Define a blueprint named 'web'
web = Blueprint('web', __name__, template_folder='templates')

# Define routes using the blueprint
@web.route('/')
def index():
    return render_template('sections/home/index.html')

@web.route('/about')
def about():
    return render_template('sections/about/about.html')

@web.route('/contact')
def contact():
    return render_template('sections/contact/contact.html')

# Example of passing a variable to a route
@web.route('/user/<full_name>')
def user_profile(full_name):
    return render_template('sections/users/user_profile.html', full_name=full_name)

@web.route('/submit', methods=['GET', 'POST'])
def submit():
    return UserController.submit()

@web.route('/login', methods=['GET', 'POST'])
def login():
    return UserController.login()

@web.route('/logout')
@login_required
def logout():
    return UserController.logout()

@web.route('/dashboard')
@login_required  # Protect this route
def dashboard():
    return UserController.dashboard()
