from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from models.users import Users
from models.login import LoginForm
from models.engine.database import session
from dotenv import load_dotenv


load_dotenv()


login_bp = Blueprint('login', __name__)


@login_bp.route('/login', strict_slashes=False, methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = (session.query(Users)
                    .filter_by(username=form.username.data).first())
        except Exception as e:
            session.rollback()
            print("Error:", e)
        finally:
            session.close()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('admin_dashboard.admin_dashboard'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html', form=form)


@login_bp.route('/logout', strict_slashes=False)
def logout():
    """
    Logs out the current user and redirects to the login page.

    Returns:
        flask.Response: A redirect response to the login page.
    """
    logout_user()
    return redirect(url_for('login.login'))
