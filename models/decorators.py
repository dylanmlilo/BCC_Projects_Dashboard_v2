""" Required Roles """
from flask import flash, redirect, url_for
from flask_login import current_user
from functools import wraps


def required_roles(*roles):
    """Decorator that checks if the user has the required role(s)
    
    The user must have at least one of the specified roles to access the
    decorated view. If the user does not have the required role(s), a
    flash message will be displayed and the user will be redirected to
    the index page.
    
    :param roles: The roles required to access the decorated view.
    """
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if not any(current_user.has_role(role) for role in roles):
                flash('You role does not allow you to access this page', 'error')
                return redirect(url_for('login.login'))
            return f(*args, **kwargs)
        return wrapped
    return wrapper
