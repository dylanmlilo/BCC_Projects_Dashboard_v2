from sqlalchemy import Column, Integer, String, Text, Date, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from models.projects import ProjectManagers
from models.base import Base
from models.engine.database import session


class StrategicTask(Base):
    __tablename__ = 'strategic_tasks'

    task_id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String(255))
    priority = Column(String(255))
    deadline = Column(String(255))
    task = Column(Text)
    description = Column(Text)
    assigned_to = Column(Integer, ForeignKey('project_managers.id'))
    deliverables = Column(Text)
    percentage_done = Column(DECIMAL(10, 2))
    fixed_cost = Column(DECIMAL(10, 2))
    estimated_hours = Column(DECIMAL(10, 2))
    actual_hours = Column(DECIMAL(10, 2))

    def __init__(self, status, priority, deadline, task, description,
                 assigned_to, deliverables, percentage_done, fixed_cost,
                 estimated_hours, actual_hours) -> None:
        self.status = status
        self.priority = priority
        self.deadline = deadline
        self.task = task
        self.description = description
        self.assigned_to = assigned_to
        self.deliverables = deliverables
        self.percentage_done = percentage_done
        self.fixed_cost = fixed_cost
        self.estimated_hours = estimated_hours
        self.actual_hours = actual_hours

    def __repr__(self) -> str:
        """Returns a string representation of the StrategicTask object."""
        return (
            f"<StrategicTask("
            f"task='{self.task}', "
            f"description='{self.description}', "
            f"assigned_to='{self.assigned_to}'"
            f")>"
        )

    @classmethod
    def strategic_tasks_to_dict_list(cls) -> list:
        try:
            query = (
                session.query(cls, ProjectManagers.name,
                              ProjectManagers.section)
                .join(ProjectManagers, cls.assigned_to == ProjectManagers.id)
            )
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
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
