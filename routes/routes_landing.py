from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from models.users import Users
from models.login import LoginForm
from models.engine.database import session
from dotenv import load_dotenv


load_dotenv()


landing_bp = Blueprint('landing', __name__)


@landing_bp.route('/', strict_slashes=False, methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    """
    Handles the login process for the application.

    Returns:
        flask.Response: A redirect response to the home page if the login is successful,
                        or a rendered template for the login page if the login fails.
    """
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
            return redirect(url_for('home.index'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('landing.html', form=form)


@landing_bp.route('/logout', strict_slashes=False)
def logout():
    """
    Logs out the current user and redirects to the login page.

    Returns:
        flask.Response: A redirect response to the login page.
    """
    logout_user()
    return redirect(url_for('landing.login'))


@landing_bp.route("/denied_access", strict_slashes=False)
def denied_access():
    return render_template("denied_access.html")
