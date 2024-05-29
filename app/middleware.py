from flask import redirect, url_for, request
from flask_login import current_user

def restrict_access():
    if current_user.is_authenticated:
        # Redirect logged-in users away from login and home page
        if request.endpoint in ['web.login', 'web.index']:
            return redirect(url_for('web.dashboard'))
    else:
        # Redirect non-logged-in users away from protected pages
        if request.endpoint in ['web.dashboard']:
            return redirect(url_for('web.login'))