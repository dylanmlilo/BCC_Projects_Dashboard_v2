from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
from models.base import Base


class Users(Base, UserMixin):
    """
    Represents a table for users with the following columns:
    - id (Integer): The primary key of the user.
    - name (String): The name of the user.
    - username (String): The username of the user (unique).
    - password (String): The password of the user.
    - email (String): The email of the user (unique).
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    surname = Column(String(100))
    username = Column(String(50), unique=True)
    password = Column(String(50))
    email = Column(String(50), unique=True)
    role = Column(String(50))

    def __init__(self, name, surname, username, password, email, role) -> None:
        """Initialising a new user"""
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
        self.email = email
        self.role = role

    def __repr__(self) -> str:
        """Returns a string representation of the User object."""
        return (
            f"<Users("
            f"name='{self.name}', "
            f"surname='{self.surname}', "
            f"username='{self.username}', "
            f"email='{self.email}'"
            f"role='{self.role}'"
            f")>"
        )
    
    def has_role(self, role):
        return self.role == role