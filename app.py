from flask import Flask, redirect, url_for, flash
from flask_login import LoginManager, current_user
from functools import wraps
from models.engine.database import session
from models.users import Users
from routes.routes_home import home_bp
from routes.routes_strategic import strategic_bp
from routes.routes_gis_task import gis_task_bp
from routes.routes_gis_data import gis_data_bp
from routes.routes_gis_resp_person import gis_resp_person_bp
from routes.routes_gis_output import gis_output_bp
from routes.routes_gis_activity import gis_activity_bp
from routes.routes_projects import projects_bp
from routes.routes_sections import sections_bp
from routes.routes_landing import landing_bp
from routes.routes_APIs import api_bp
from routes.routes_admin_dashboard import admin_dashboard_bp
import os
from dotenv import load_dotenv
from itertools import groupby


load_dotenv()


app = Flask(__name__)
app.register_blueprint(home_bp)
app.register_blueprint(strategic_bp)
app.register_blueprint(gis_task_bp)
app.register_blueprint(gis_data_bp)
app.register_blueprint(gis_resp_person_bp)
app.register_blueprint(gis_output_bp)
app.register_blueprint(gis_activity_bp)
app.register_blueprint(projects_bp)
app.register_blueprint(sections_bp)
app.register_blueprint(landing_bp)
app.register_blueprint(api_bp)
app.register_blueprint(admin_dashboard_bp)
app.secret_key = os.getenv("SECRET_KEY")


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'landing.login'


@login_manager.user_loader
def load_user(user_id):
    """
    Loads a user object from the database based on the user ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        Users or None: The user object if found, None otherwise.
    """
    try:
        user = session.get(Users, int(user_id))
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()
    return user


@app.route('/check_role')
def check_role():
    if current_user.is_authenticated:
        try:
            user = session.query(Users).filter_by(id=current_user.id).first()
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
        finally:
            session.close()
        if current_user.has_role(user.role):
            return "You are logged in as a {}".format(user.role)
    else:
        return "You are not logged in"
    

if __name__ == "__main__":
    app.run(debug=True, port=3000)
