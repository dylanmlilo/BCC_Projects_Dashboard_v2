from flask import Blueprint, render_template, abort, jsonify, request, redirect, url_for, flash
from models.engine.database import session, projects_data_to_dict_list, project_managers_to_dict_list
from models.plot_functions import today_date
from models.projects import ProjectsData, ProjectManagers


projects_bp = Blueprint('projects', __name__)


@projects_bp.route("/projects_data", strict_slashes=False)
def projects_data():
    """
    Function to handle projects data retrieval and rendering.

    Retrieves projects data and today's date, then renders the projects_data.html template.

    Parameters:
    - None

    Returns:
    - Rendered template "projects_data.html" with today's date and projects data.

    """
    projects_data = projects_data_to_dict_list()
    project_managers = project_managers_to_dict_list()
    formatted_date = today_date()
    return render_template("projects_data.html", today_date=formatted_date,
                           projects_data=projects_data, project_managers=project_managers)


@projects_bp.route("/insert_project_manager", methods=['POST'])
def insert_project_manager():
    """
    Function to handle insert project manager route."""

    if request.method == 'POST':
        try:
            name = request.form.get('name')
            section = request.form.get('section')

            new_project_manager = ProjectManagers(name=name, section=section)
            session.add(new_project_manager)
            session.commit()
            flash('Data inserted successfully')
            return redirect(request.referrer)
        
        except Exception as e:
            session.rollback()
            return jsonify({'error': str(e)}), 400
        
        finally:
            session.close()


@projects_bp.route("/update_projects_project_manager/<int:project_manager_id>", methods=['POST'])
def update_projects_project_manager(project_manager_id):
    """
    Function to handle update project manager route."""

    if request.method == 'POST':
        try:
            project_manager = session.query(ProjectManagers).filter_by(id=project_manager_id).first()
            if project_manager:
                project_manager.name = request.form.get('name')
                project_manager.section = request.form.get('section')
                session.commit()
                flash('Data updated successfully')
            else:
                flash('Project manager not found')

            return redirect(request.referrer)

        except Exception as e:
            session.rollback()
            return jsonify({'error': str(e)}), 400

        finally:
            session.close()



@projects_bp.route('/insert_projects_data', methods=['POST'])
def insert_projects_data():
    """
    Inserts the project data into the database and redirects to the projects page.

    Returns:
        flask.Response: A redirect response to the projects page or a JSON response with an error message.
    """
    if request.method == 'POST':
        try:
            # Get form data
            contract_number = request.form.get('contract_number')
            contract_name = request.form.get('contract_name')
            contract_type_id = request.form.get('contract_type_id')
            project_manager_id = request.form.get('project_manager_id')
            section_id = request.form.get('section_id')
            contractor = request.form.get('contractor')
            year = request.form.get('year')
            date_contract_signed = request.form.get('date_contract_signed')
            date_contract_signed_by_bcc = request.form.get('date_contract_signed_by_bcc')
            early_start_date = request.form.get('early_start_date')
            contract_duration_weeks = request.form.get('contract_duration_weeks')
            contract_duration_months = request.form.get('contract_duration_months')
            early_finish_date = request.form.get('early_finish_date')
            extension_of_time = request.form.get('extension_of_time')
            project_status = request.form.get('project_status')
            contract_value_including_ten_percent_contingency = request.form.get('contract_value_including_ten_percent_contingency')
            performance_guarantee_value = request.form.get('performance_guarantee_value')
            performance_guarantee_expiry_date = request.form.get('performance_guarantee_expiry_date')
            advance_payment_value = request.form.get('advance_payment_value')
            advance_payment_guarantee_expiry_date = request.form.get('advance_payment_guarantee_expiry_date')
            total_certified_interim_payments_to_date = request.form.get('total_certified_interim_payments_to_date')
            financial_progress_percentage = request.form.get('financial_progress_percentage')
            roads_progress = request.form.get('roads_progress')
            water_progress = request.form.get('water_progress')
            sewer_progress = request.form.get('sewer_progress')
            storm_drainage_progress = request.form.get('storm_drainage_progress')
            public_lighting_progress = request.form.get('public_lighting_progress')
            physical_progress_percentage = request.form.get('physical_progress_percentage')
            tax_clearance_validation = request.form.get('tax_clearance_validation')
            link = request.form.get('link')
        
            # Create new project record
            new_project_record = ProjectsData(
                contract_number=contract_number,
                contract_name=contract_name,
                contract_type_id=contract_type_id,
                project_manager_id=project_manager_id,
                section_id=section_id,
                contractor=contractor,
                year=year,
                date_contract_signed=date_contract_signed,
                date_contract_signed_by_bcc=date_contract_signed_by_bcc,
                early_start_date=early_start_date,
                contract_duration_weeks=contract_duration_weeks,
                contract_duration_months=contract_duration_months,
                early_finish_date=early_finish_date,
                extension_of_time=extension_of_time,
                project_status=project_status,
                contract_value_including_ten_percent_contingency=contract_value_including_ten_percent_contingency,
                performance_guarantee_value=performance_guarantee_value,
                performance_guarantee_expiry_date=performance_guarantee_expiry_date,
                advance_payment_value=advance_payment_value,
                advance_payment_guarantee_expiry_date=advance_payment_guarantee_expiry_date,
                total_certified_interim_payments_to_date=total_certified_interim_payments_to_date,
                financial_progress_percentage=financial_progress_percentage,
                roads_progress=roads_progress,
                water_progress=water_progress,
                sewer_progress=sewer_progress,
                storm_drainaige_progress=storm_drainage_progress,
                public_lighting_progress=public_lighting_progress,
                physical_progress_percentage=physical_progress_percentage,
                tax_clearance_validation=tax_clearance_validation,
                link=link)
            
            session.add(new_project_record)
            session.commit()
            flash('Data inserted successfully')
            return redirect(url_for('projects.projects_data'))

        
        except Exception as e:
            session.rollback()
            return jsonify({'error': str(e)}), 400
        
        finally:
            session.close()