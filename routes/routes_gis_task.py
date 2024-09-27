from flask import Blueprint, request, redirect, url_for, flash, jsonify
from models.engine.database import session
from models.gis import Task
from flask_login import login_required
from models.decorators import required_roles


gis_task_bp = Blueprint('gis_task', __name__)


@gis_task_bp.route("/insert_gis_task_data", methods=['POST'])
@login_required
@required_roles("admin", "admin_gis")
def insert_gis_task_data():

    if request.method == "POST":
        try:
            activity_id = request.form.get('activity_id')
            description = request.form.get('task_description')
            percentage_of_activity = request.form.get('percentage_of_activity')

            if not percentage_of_activity:
                percentage_of_activity = None
            else:
                percentage_of_activity = float(percentage_of_activity)

            new_task = Task(activity_id=activity_id, description=description,
                            percentage_of_activity=percentage_of_activity)
            session.add(new_task)
            session.commit()
            flash('Data inserted successfully')
            return redirect(url_for('gis_data.gis_data'))

        except Exception as e:
            session.rollback()
            return jsonify({'error': str(e)}), 400

        finally:
            session.close()


@gis_task_bp.route(
    "/update_gis_task_data/<int:gis_task_data_id>", methods=['POST'])
@login_required
@required_roles("admin", "admin_gis")
def update_gis_task_data(gis_task_data_id):
    """
    Updates the gis data into the database and redirects to the gis data page.

    Returns:
        flask.Response: A redirect response to the
        dagista page or a JSON response with an error message.
    """
    if request.method == 'POST':
        try:

            task = session.query(Task).filter_by(id=gis_task_data_id).first()
            if task:
                task.activity_id = request.form.get('activity_id')
                task.description = request.form.get('task_description')
                percentage_of_activity = (
                    request.form.get('percentage_of_activity')
                    )
                if percentage_of_activity:
                    task.percentage_of_activity = percentage_of_activity
                else:
                    task.percentage_of_activity = None

                session.commit()
                flash('Data updated successfully')
                return redirect(url_for('gis_data.gis_data'))

        except Exception as e:
            session.rollback()
            return jsonify({'error': str(e)}), 400

        finally:
            session.close()


@gis_task_bp.route("/delete_gis_task_data/<int:gis_task_data_id>")
@login_required
@required_roles("admin", "admin_gis")
def delete_gis_task_data(gis_task_data_id):
    """
    Deletes the gis data from the database and redirects to the gis data page.

    Returns:
        flask.Response: A redirect response to the
        dagista page or a JSON response with an error message.
    """
    try:
        task = session.query(Task).filter_by(id=gis_task_data_id).first()
        if task:
            session.delete(task)
            session.commit()
            flash('Data deleted successfully')
            return redirect(url_for('gis_data.gis_data'))

    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400

    finally:
        session.close()
