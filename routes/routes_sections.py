from flask import Blueprint, render_template
from models.engine.database import projects_data_to_dict_list
from models.plot_functions import today_date, plot_servicing_page_charts


sections_bp = Blueprint('sections', __name__)


@sections_bp.route("/Servicing", strict_slashes=False)
def servicing():
    """
    Renders the 'servicing.html' template with project data for servicing contracts.

    This function fetches project data for servicing contracts, generates a bar chart,
    and renders the 'servicing.html' template with the necessary data.

    Returns:
        Flask.Response: The rendered template.
    """
    projects_data = projects_data_to_dict_list(1)
    servicing_data_JSON = plot_servicing_page_charts()
    formatted_date = today_date()
    return render_template("servicing.html", projects_data=projects_data,
                           today_date=formatted_date,
                           servicing_data_JSON=servicing_data_JSON)


@sections_bp.route("/Goods", strict_slashes=True)
def goods():
    """
    Function to handle /Goods route.

    Retrieves projects data and today's date, then renders the goods.html template.

    Parameters:
    - None

    Returns:
    - Rendered template "goods.html" with today's date and projects data.

    """
    projects_data = projects_data_to_dict_list(3)
    formatted_date = today_date()
    return render_template("goods.html", today_date=formatted_date, 
                           projects_data=projects_data)


@sections_bp.route("/Works", strict_slashes=False)
def works():
    """
    Function to handle works data retrieval and rendering.

    Retrieves projects data and today's date, then renders the works.html template.

    Parameters:
    - None

    Returns:
    - Rendered template "works.html" with today's date and projects data.

    """
    projects_data = projects_data_to_dict_list(4)
    formatted_date = today_date()
    return render_template("works.html", today_date=formatted_date,
                           projects_data=projects_data)


@sections_bp.route("/Services", strict_slashes=False)
def services():
    """
    Function to handle Services route.

    Retrieves projects data and today's date, then renders the services.html template.

    Parameters:
    - None

    Returns:
    - Rendered template "services.html" with today's date and projects data.

    """
    projects_data = projects_data_to_dict_list(2)
    formatted_date = today_date()
    return render_template("services.html", today_date=formatted_date,
                           projects_data=projects_data)