from flask import Blueprint, render_template
from flask_login import login_required


admin_dashboard_bp = Blueprint('admin_dashboard', __name__)


@admin_dashboard_bp.route("/admin_dashboard", strict_slashes=False)
@login_required
def admin_dashboard():
    """
    Renders the admin dashboard page.

    Returns:
        flask.Response: The rendered admin dashboard template.
    """
    return render_template("admin_dashboard.html")