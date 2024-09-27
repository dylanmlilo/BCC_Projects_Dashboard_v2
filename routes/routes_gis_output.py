from flask import Blueprint, request, redirect, url_for, flash, jsonify
from models.engine.database import session
from models.gis import Output
from flask_login import login_required
from models.decorators import required_roles


gis_output_bp = Blueprint('gis_output', __name__)


@gis_output_bp.route("/insert_gis_output_data", methods=['POST'])
@login_required
@required_roles("admin", "admin_gis")
def insert_gis_output_data():
    """
    Inserts the gis data into the database and redirects to the gis data page.

    Returns:
        flask.Response: A redirect response to the
        dagista page or a JSON response with an error message.
    """
    if request.method == 'POST':
        try:
            name = request.form.get('output_name')

            new_output = Output(name=name)
            session.add(new_output)
            session.commit()
            flash('Data inserted successfully')
            return redirect(url_for('gis_data.gis_data'))

        except Exception as e:
            session.rollback()
            return jsonify({'error': str(e)}), 400

        finally:
            session.close()


@gis_output_bp.route("/update_gis_output_data/<int:gis_output_data_id>",
                     methods=['POST'])
@login_required
@required_roles("admin", "admin_gis")
def update_gis_output_data(gis_output_data_id):
    """
    Updates the gis data into the database and redirects to the gis data page.

    Returns:
        flask.Response: A redirect response to the
        dagista page or a JSON response with an error message.
    """
    if request.method == 'POST':
        try:

            output = (session.query(Output)
                      .filter_by(id=gis_output_data_id)
                      .first())
            if output:
                output.name = request.form.get('output_name')

                session.commit()
                flash('Data updated successfully')
                return redirect(url_for('gis_data.gis_data'))

        except Exception as e:
            session.rollback()
            return jsonify({'error': str(e)}), 400

        finally:
            session.close()


@gis_output_bp.route("/delete_gis_output_data/<int:gis_output_data_id>")
@login_required
@required_roles("admin", "admin_gis")
def delete_gis_output_data(gis_output_data_id):
    """
    Deletes the gis data from the database and redirects to the gis data page.

    Returns:
        flask.Response: A redirect response to the
        dagista page or a JSON response with an error message.
    """
    try:
        output = session.query(Output).filter_by(id=gis_output_data_id).first()
        if output:
            session.delete(output)
            session.commit()
            flash('Data deleted successfully')
            return redirect(url_for('gis_data.gis_data'))

    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400

    finally:
        session.close()
