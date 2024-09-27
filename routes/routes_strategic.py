from flask import (
    Blueprint, render_template, request, redirect, url_for, flash, jsonify
    )
from flask_login import login_required
from models.plot_functions import today_date
from models.engine.database import session
from models.strategic import StrategicTask
from models.projects import ProjectManagers
from models.decorators import required_roles


strategic_bp = Blueprint('strategic', __name__)


@strategic_bp.route("/StrategicPlanning", strict_slashes=False)
@login_required
def strategic_planning():
    """
    Function to handle Strategic Planning route.

    Retrieves strategic data list and today's date,
    then renders the strategic_planning.html template.

    Parameters:
    - None

    Returns:
    - Rendered template "strategic_planning.html"
    with today's date and strategic data list.

    """
    strategic_data_list = StrategicTask.strategic_tasks_to_dict_list()
    formatted_date = today_date()
    return render_template("strategic_planning.html",
                           today_date=formatted_date,
                           strategic_data_list=strategic_data_list)


@strategic_bp.route("/strategic_planning_data", strict_slashes=False)
@login_required
@required_roles('admin', 'admin_struts')
def strategic_planning_data():
    """
    Function to handle Strategic Planning data route.

    Retrieves strategic data list and renders
    the strategic_planning.html template.

    Parameters:
    - None

    Returns:
    - Rendered template "strategic_planning.html" with strategic data list.
    """
    formatted_date = today_date()
    strategic_data_list = StrategicTask.strategic_tasks_to_dict_list()
    project_managers = (
        ProjectManagers.project_managers_to_dict_list("strategic planning")
        )
    return render_template("strategic_planning_data.html",
                           strategic_data_list=strategic_data_list,
                           today_date=formatted_date,
                           project_managers=project_managers)


@strategic_bp.route("/insert_strategic_data", methods=['POST'])
@login_required
@required_roles('admin', 'admin_struts')
def insert_strategic_data():
    """
    Function to handle insert strategic data route.

    Retrieves strategic data list and renders
    the strategic_planning.html template.

    Parameters:
    - None

    Returns:
    - Rendered template "strategic_planning.html" with strategic data list.
    """
    if request.method == 'POST':
        try:
            task = request.form.get('task')
            description = request.form.get('description')
            if description == '':
                description = None
            deliverables = request.form.get('deliverables')
            if deliverables == '':
                deliverables = None
            assigned_to = request.form.get('assigned_to')
            deadline = request.form.get('deadline')
            if deadline == '':
                deadline = None
            status = request.form.get('status')
            priority = request.form.get('priority')
            percentage_done = request.form.get('percentage_done')
            if percentage_done == '':
                percentage_done = None
            fixed_cost = request.form.get('fixed_cost')
            if fixed_cost == '':
                fixed_cost = None
            estimated_hours = request.form.get('estimated_cost')
            if estimated_hours == '':
                estimated_hours = None
            actual_hours = request.form.get('actual_cost')
            if actual_hours == '':
                actual_hours = None

            new_task = StrategicTask(task=task, description=description,
                                     deliverables=deliverables,
                                     assigned_to=assigned_to,
                                     deadline=deadline, status=status,
                                     priority=priority,
                                     percentage_done=percentage_done,
                                     fixed_cost=fixed_cost,
                                     estimated_hours=estimated_hours,
                                     actual_hours=actual_hours)
            session.add(new_task)
            session.commit()
            flash('Data inserted successfully')
            return redirect(url_for('strategic.strategic_planning_data'))

        except Exception as e:
            session.rollback()
            return jsonify({'error': str(e)}), 400

        finally:
            session.close()


@strategic_bp.route(
    "/update_strategic_data/<int:strategic_data_id>", methods=['POST'])
@login_required
@required_roles('admin', 'admin_struts')
def update_strategic_data(strategic_data_id):
    """
    Function to handle update strategic data route.

    Retrieves strategic data list and renders
    the strategic_planning.html template.

    Parameters:
    - None

    Returns:
    - Rendered template "strategic_planning.html" with strategic data list.
    """
    if request.method == 'POST':
        try:
            task = (session.query(StrategicTask)
                    .filter_by(task_id=strategic_data_id).first())
            if task:
                task.task = request.form.get('task')
                task.description = request.form.get('description')
                if task.description == '':
                    task.description = None
                task.deliverables = request.form.get('deliverables')
                if task.deliverables == '':
                    task.deliverables = None
                task.assigned_to = request.form.get('assigned_to')
                task.deadline = request.form.get('deadline')
                if task.deadline == '':
                    task.deadline = None
                task.status = request.form.get('status')
                task.priority = request.form.get('priority')
                task.percentage_done = request.form.get('percentage_done')
                if task.percentage_done == '':
                    task.percentage_done = None
                task.fixed_cost = request.form.get('fixed_cost')
                if task.fixed_cost == '':
                    task.fixed_cost = None
                task.estimated_hours = request.form.get('estimated_cost')
                if task.estimated_hours == '':
                    task.estimated_hours = None
                task.actual_hours = request.form.get('actual_cost')
                if task.actual_hours == '':
                    task.actual_hours = None

                session.commit()
                flash('Data updated successfully')
                return redirect(url_for('strategic.strategic_planning_data'))

        except Exception as e:
            session.rollback()
            return jsonify({'error': str(e)}), 400

        finally:
            session.close()


@strategic_bp.route("/delete_strategic_data/<int:strategic_data_id>")
@login_required
@required_roles('admin', 'admin_struts')
def delete_strategic_data(strategic_data_id):
    """
    Function to handle delete strategic data route.

    Retrieves strategic data list and renders the
    strategic_planning.html template.

    Parameters:
    - None

    Returns:
    - Rendered template "strategic_planning.html" with strategic data list.
    """
    try:
        task = (session.query(StrategicTask)
                .filter_by(task_id=strategic_data_id).first())
        if task:
            session.delete(task)
            session.commit()
            flash('Data deleted successfully')
            return redirect(url_for('strategic.strategic_planning_data'))

    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400

    finally:
        session.close()
