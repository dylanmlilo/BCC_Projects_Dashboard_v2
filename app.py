from flask import Flask, render_template
from flask_login import LoginManager
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
from routes.routes_login import login_bp
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
app.register_blueprint(login_bp)
app.register_blueprint(api_bp)
app.register_blueprint(admin_dashboard_bp)
app.secret_key = os.getenv("SECRET_KEY")


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login.login'


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


# Sample data
gis_data = [
    {"output_name": "Output 1", "activity": "Activity 1", "task_description": "Task 1", "responsible_person": "Person 1", "designation": "Designation 1"},
    {"output_name": "Output 1", "activity": "Activity 2", "task_description": "Task 2", "responsible_person": "Person 2", "designation": "Designation 2"},
    {"output_name": "Output 2", "activity": "Activity 3", "task_description": "Task 3", "responsible_person": "Person 3", "designation": "Designation 3"},
    {"output_name": "Output 2", "activity": "Activity 4", "task_description": "Task 4", "responsible_person": "Person 4", "designation": "Designation 4"},
    {"output_name": "Output 3", "activity": "Activity 5", "task_description": "Task 5", "responsible_person": "Person 5", "designation": "Designation 5"}
]

@app.route("/test")
def index():
    # Group consecutive rows by output_name
    gis_data_grouped = []
    for key, group in groupby(gis_data, key=lambda x: x["output_name"]):
        gis_data_grouped.append((key, list(group)))
    return render_template("test.html", gis_data_grouped=gis_data_grouped)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
