from sqlalchemy import Column, Integer, String, Text, Date, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from models.engine.database import session


class Section(Base):
    __tablename__ = 'section'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Section({self.name})"


class ProjectManagers(Base):
    __tablename__ = 'project_managers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    section = Column(String(100))

    def __init__(self, name, section):
        self.name = name
        self.section = section

    def __repr__(self):
        return f"ProjectManagers({self.name}, {self.section})"

    @classmethod
    def project_managers_to_dict_list(cls, section_name=None):
        """
        Convert SQLAlchemy query results into a list of dictionaries.
        Exclude the _sa_instance_state attribute.

        Args:
            section_name (str, optional): Name of the section to
            filter project managers. Defaults to None.

        Returns:
            list: A list of dictionaries containing project managers.
        """
        try:
            query_filter = (cls.section == section_name if section_name
                            else True)
            project_managers = session.query(cls).filter(query_filter).all()
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
        finally:
            session.close()

        result_list = []
        for row in project_managers:
            result_dict = {}
            for column in row.__table__.columns:
                result_dict[column.name] = getattr(row, column.name)
            result_list.append(result_dict)
        return result_list


class ContractType(Base):
    __tablename__ = 'contract_type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"ContractType({self.name})"

    @classmethod
    def contract_type_data_dict(cls, contract_type_id: int) -> list[dict]:
        """
        Filters and returns project data for a specific contract type id.

        Args:
            contract_type_id: The contract type id to filter by.

        Returns:
            A list of dictionaries containing project data
            for the specified contract type.
            If no data is found, an empty list is returned.
        """
        if not isinstance(contract_type_id, int) or contract_type_id <= 0:
            raise ValueError("Invalid contract_type_id")

        try:
            data = projects_data_to_dict_list()
        except Exception as e:
            print(f"Error retrieving data: {e}")
            return []

        filtered_data = [
            row
            for row in data
            if row.get('contract_type_id') == contract_type_id
        ]
        return filtered_data


class ProjectsData(Base):
    __tablename__ = 'projects_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    contract_number = Column(String(50), nullable=False)
    contract_name = Column(Text)
    contract_type_id = Column(Integer, ForeignKey('contract_type.id'))
    project_manager_id = Column(Integer, ForeignKey('project_managers.id'))
    section_id = Column(Integer, ForeignKey('section.id'))
    contractor = Column(Text)
    year = Column(String(20))
    date_contract_signed = Column(Date)
    date_contract_signed_by_bcc = Column(Date)
    early_start_date = Column(Date)
    contract_duration_weeks = Column(DECIMAL(10, 2))
    contract_duration_months = Column(DECIMAL(10, 2))
    early_finish_date = Column(Date)
    extension_of_time = Column(Date)
    project_status = Column(String(50))
    contract_value_including_ten_percent_contingency = Column(DECIMAL(20, 2))
    performance_guarantee_value = Column(DECIMAL(20, 2))
    performance_guarantee_expiry_date = Column(Date)
    advance_payment_value = Column(DECIMAL(20, 2))
    advance_payment_guarantee_expiry_date = Column(Date)
    total_certified_interim_payments_to_date = Column(DECIMAL(20, 2))
    financial_progress_percentage = Column(DECIMAL(10, 2))
    roads_progress = Column(DECIMAL(10, 2))
    water_progress = Column(DECIMAL(10, 2))
    sewer_progress = Column(DECIMAL(10, 2))
    storm_drainage_progress = Column(DECIMAL(10, 2))
    public_lighting_progress = Column(DECIMAL(10, 2))
    physical_progress_percentage = Column(DECIMAL(10, 2))
    tax_clearance_validation = Column(String(50))
    link = Column(String(255))

    contract_type = relationship("ContractType")
    project_manager = relationship("ProjectManagers")
    section = relationship("Section")


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
        query = (
            session.query(ProjectsData)
            .join(ProjectsData.contract_type)
            .join(ProjectsData.project_manager)
            .join(ProjectsData.section)
        )
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
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
