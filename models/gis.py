from sqlalchemy import Column, Integer, String, Text, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import select
from models.base import Base
from models.engine.database import session


class Output(Base):
    __tablename__ = "output"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Output(id={self.id}, name='{self.name}')"

    @classmethod
    def gis_output_data_to_dict_list(cls):
        """
        Queries the database for Output data and
        converts it to a list of dictionaries.

        Returns:
            list: A list of dictionaries containing output data.
        """
        output_list = []
        try:
            query = session.query(cls.id, cls.name).all()
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
        finally:
            session.close()

        for row in query:
            output_dict = {
                "output_id": row[0],
                "output_name": row[1]
            }
            output_list.append(output_dict)

        return output_list


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True)
    activity = Column(String(255), nullable=False)
    output_id = Column(Integer, ForeignKey("output.id"))
    responsible_person_id = Column(Integer, ForeignKey("responsiblepeople.id"))

    output = relationship("Output", backref="activities")
    responsible_person = relationship("ResponsiblePerson",
                                      backref="activities")

    def __init__(self, activity, output_id, responsible_person_id):
        self.activity = activity
        self.output_id = output_id
        self.responsible_person_id = responsible_person_id

    def __repr__(self) -> str:
        """Returns a string representation of the Activity object."""
        return (
            f"Activity("
            f"id={self.id}, "
            f"activity='{self.activity}', "
            f"output_id={self.output_id}, "
            f"responsible_person_id={self.responsible_person_id}"
            f")"
        )

    @classmethod
    def gis_activity_data_to_dict_list(cls):
        """
        Queries the database for Activity data and
        converts it to a list of dictionaries.
        Returns:
            list: A list of dictionaries containing activity data.
        """
        activity_list = []
        try:
            query = session.query(cls.id, cls.activity, cls.output_id,
                                  cls.responsible_person_id).all()
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
        finally:
            session.close()

        for row in query:
            activity_dict = {
                "activity_id": row[0],
                "activity_name": row[1],
                "output_id": row[2],
                "responsible_person_id": row[3]
            }
            activity_list.append(activity_dict)

        return activity_list


class ResponsiblePerson(Base):
    __tablename__ = "responsiblepeople"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    designation = Column(String(255), nullable=False)

    def __init__(self, name, designation):
        self.name = name
        self.designation = designation

    def __repr__(self) -> str:
        """Returns a string representation of the ResponsiblePerson object."""
        return (
            f"ResponsiblePerson("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"designation='{self.designation}'"
            f")"
        )

    @classmethod
    def gis_responsible_person_data_to_dict_list(cls):
        responsible_person_list = []
        try:
            query = session.query(cls.id, cls.name, cls.designation).all()
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
        finally:
            session.close()

        for row in query:
            responsible_person_dict = {
                "responsible_person_id": row[0],
                "responsible_person_name": row[1],
                "designation": row[2]
            }
            responsible_person_list.append(responsible_person_dict)

        return responsible_person_list


class Task(Base):
    """ Represents a task. """
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    activity_id = Column(Integer, ForeignKey("activities.id"))
    description = Column(Text, nullable=False)
    percentage_of_activity = Column(DECIMAL(5, 2), nullable=True)

    activity = relationship("Activity", backref="tasks")

    def __init__(self, activity_id, description, percentage_of_activity=None):
        """ Initializes a new Task object. """
        self.activity_id = activity_id
        self.description = description
        self.percentage_of_activity = percentage_of_activity

    def __repr__(self) -> str:
        """Returns a string representation of the Task object."""
        return (
            f"Task("
            f"id={self.id}, "
            f"activity_id={self.activity_id}, "
            f"description='{self.description}', "
            f"percentage_of_activity={self.percentage_of_activity}"
            f")"
        )

    @classmethod
    def gis_task_data_to_dict_list(cls):
        """
        Queries the database for GIS task data and
        converts it to a list of dictionaries.

        Returns:
            list: A list of dictionaries containing GIS task data.
        """
        task_list = []
        try:
            query = session.query(cls.id, cls.description,
                                  cls.percentage_of_activity,
                                  cls.activity_id).all()
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
        finally:
            session.close()

        for row in query:
            task_dict = {
                "task_id": row[0],
                "task_description": row[1],
                "percentage_of_activity": row[2],
                "activity_id": row[3]
            }
            task_list.append(task_dict)

        return task_list


def gis_data_to_dict_list():
    """
    Returns a list of dictionaries containing GIS data.

    This function queries the database to retrieve GIS data,
    including output information, activity details, responsible person
    information, and task descriptions. It then constructs a list of
    dictionaries, where each dictionary represents a single GIS data
    point. The function handles potential database errors and ensures
    that the session is properly closed.

    Returns:
        A list of dictionaries for GIS Data
    """
    try:
        query = select(
            Output.id,
            Output.name,
            Activity.activity,
            ResponsiblePerson.name,
            ResponsiblePerson.designation,
            Task.description,
            Task.percentage_of_activity
        ).select_from(
            Output
        ).outerjoin(
            Activity, Output.id == Activity.output_id
        ).outerjoin(
            ResponsiblePerson,
            Activity.responsible_person_id == ResponsiblePerson.id
        ).outerjoin(
            Task, Activity.id == Task.activity_id
        )
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()

    try:
        results = session.execute(query).fetchall()
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()

    gis_data = []
    for row in results:
        gis_dict = {
            "output_id": row[0],
            "output_name": row[1],
            "activity": row[2],
            "responsible_person": row[3],
            "designation": row[4],
            "task_description": row[5],
            "percentage_of_activity": row[6]
        }
        gis_data.append(gis_dict)

    return gis_data
