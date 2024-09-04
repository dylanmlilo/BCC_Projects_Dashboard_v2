from flask import Blueprint, render_template
from models.plot_functions import today_date, plot_home_page_charts
from models.projects import projects_data_to_dict_list

home_bp = Blueprint('home', __name__)


@home_bp.route("/", strict_slashes=False)
def index():
    projects_data = projects_data_to_dict_list()
    graph1JSON, graph2JSON, graph3JSON, graph4JSON, graph5JSON = plot_home_page_charts()
    formatted_date = today_date()
    return render_template("home.html", graph1JSON=graph1JSON, today_date=formatted_date,
                           graph2JSON=graph2JSON, graph3JSON=graph3JSON,
                           graph4JSON=graph4JSON, projects_data=projects_data,
                           graph5JSON=graph5JSON)