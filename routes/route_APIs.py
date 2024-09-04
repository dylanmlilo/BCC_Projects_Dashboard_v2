from flask import Blueprint, request, jsonify
from models.projects import projects_data_to_dict_list


api_bp = Blueprint('api', __name__)


@api_bp.route("/api/projects_data", strict_slashes=False)
def projects_data_api():
    """
    Function to handle projects data API endpoint.

    Retrieves projects data and returns it in JSON format.

    Parameters:
    - None

    Returns:
    - JSON response containing projects data.

    """
    projects_data = projects_data_to_dict_list()
    return jsonify(projects_data)

# @api_bp.route("/get_data_from_my_api", strict_slashes=False)
# def get_data_from_my_api():
#     response = requests.get("http://127.0.0.1:3000/api/projects_data")
#     return response.json()

# response = requests.get("http://127.0.0.1:3000/api/projects_data")
# print(response.json())