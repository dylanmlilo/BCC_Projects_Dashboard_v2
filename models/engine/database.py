from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, select, join
from models.projects import ProjectsData, ProjectManagers
from models.strategic import StrategicTask
from dotenv import load_dotenv
import os

load_dotenv()

db_connection_string = os.getenv("db_connection_string")

engine = create_engine(db_connection_string)

Session = sessionmaker(bind=engine)

session = Session()


def project_managers_to_dict_list(section_name=None):
    """
    Convert SQLAlchemy query results into a list of dictionaries.
    Exclude the _sa_instance_state attribute.
    
    Args:
        section_name (str, optional): Name of the section to filter project managers. Defaults to None.
    
    Returns:
        list: A list of dictionaries containing project managers.
    """
    try:
        if section_name:
            project_managers = session.query(ProjectManagers).filter(ProjectManagers.section == section_name).all()
        else:
            project_managers = session.query(ProjectManagers).all()
    except:
        session.rollback()
    finally:
        session.close()
    
    result_list = []
    for row in project_managers:
        result_dict = {}
        for column in row.__table__.columns:
            result_dict[column.name] = getattr(row, column.name)
        result_list.append(result_dict)
    
    return result_list


def projects_data_to_dict_list(contract_type_id=None):
    """
    Convert SQLAlchemy query results into a list of dictionaries.
    Exclude the _sa_instance_state attribute.
    
    Args:
        contract_type_id (str, optional): Filter results by contract_type_id.
        Defaults to None.
    
    Returns:
        list: A list of dictionaries containing projects data with related data
        from ContractType, ProjectManagers, and Section.
    """
    try:
        query = session.query(ProjectsData) \
        .join(ProjectsData.contract_type) \
        .join(ProjectsData.project_manager) \
        .join(ProjectsData.section)
    except:
        session.rollback()
    finally:
        session.close()
    
    if contract_type_id:
        query = query.filter(ProjectsData.contract_type_id == contract_type_id)
    
    projects_data = query.all()
    
    result_list = []
    for row in projects_data:
        result_dict = {}
        for column in row.__table__.columns:
            result_dict[column.name] = getattr(row, column.name)
        
        result_dict['contract_type'] = row.contract_type.name
        result_dict['project_manager'] = row.project_manager.name
        result_dict['section'] = row.section.name
        
        result_list.append(result_dict)
    
    sorted_result_list = sorted(result_list, key=lambda x: x["id"])
    return sorted_result_list


def contract_type_data_dict(contract_type_id):
    """
    Filters and returns project data for a specific contract type id.

    Args:
      contract_type_id (int): The contract type id to filter by.

    Returns:
      list: A list of dictionaries containing project data for the specified contract type,
        or an empty list if no data is found.
    """ 

    servicing_data = projects_data_to_dict_list()
    filtered_data = [row for row in servicing_data if 'contract_type_id' in row and row['contract_type_id'] == contract_type_id]
    return filtered_data

def strategic_tasks_to_dict_list():
    try:
        query = session.query(StrategicTask, ProjectManagers.name, ProjectManagers.section).join(ProjectManagers, StrategicTask.assigned_to == ProjectManagers.id)
    except:
        session.rollback()
    finally:
        session.close()

    results = query.all()
    
    task_list = [
        {
            'task_id': task.StrategicTask.task_id,
            'status': task.StrategicTask.status,
            'priority': task.StrategicTask.priority,
            'deadline': task.StrategicTask.deadline,
            'task': task.StrategicTask.task,
            'description': task.StrategicTask.description,
            'assigned_to': task.StrategicTask.assigned_to,
            'project_manager': task.name,
            'section': task.section,
            'deliverables': task.StrategicTask.deliverables,
            'percentage_done': task.StrategicTask.percentage_done,
            'fixed_cost': task.StrategicTask.fixed_cost,
            'estimated_hours': task.StrategicTask.estimated_hours,
            'actual_hours': task.StrategicTask.actual_hours
        }
        for task in results
    ]

    return task_list