from flask import Flask, render_template
from flask_login import LoginManager
from models.plot_functions import today_date, plot_home_page_charts
from models.engine.database import session, projects_data_to_dict_list
from models.users import Users
from routes.routes_strategic import strategic_bp
from routes.routes_gis_task import gis_task_bp
from routes.routes_gis_data import gis_data_bp
from routes.routes_gis_resp_person import gis_resp_person_bp
from routes.routes_gis_output import gis_output_bp
from routes.routes_gis_activity import gis_activity_bp
from routes.routes_projects import projects_bp
from routes.routes_sections import sections_bp
from routes.routes_login import login_bp
from routes.route_APIs import api_bp
from routes.routes_admin_dashboard import admin_dashboard_bp
import os
from dotenv import load_dotenv


load_dotenv()


app = Flask(__name__)
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
login_manager.login_view = 'login'


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
        user = session.query(Users).get(int(user_id))
    except:
        session.rollback()
    finally:
        session.close()
    return user


@app.route("/", strict_slashes=False)
def index():
    projects_data = projects_data_to_dict_list()
    graph1JSON, graph2JSON, graph3JSON, graph4JSON, graph5JSON = plot_home_page_charts()
    formatted_date = today_date()
    return render_template("home.html", graph1JSON=graph1JSON, today_date=formatted_date,
                           graph2JSON=graph2JSON, graph3JSON=graph3JSON,
                           graph4JSON=graph4JSON, projects_data=projects_data,
                           graph5JSON=graph5JSON)


if __name__ == "__main__":
    app.run(debug=True, port=3000)