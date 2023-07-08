from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import relationship

from data.base import Base
from data.base import Session

from modal.account import Account


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    type = Column(Integer)
    status = Column(Integer)
    score = Column(Integer)

    p_id = Column(Integer, ForeignKey('project.id'))
    project = relationship('Project', back_populates='tasks', lazy='subquery')

    due_to = Column(Date)

    members = relationship('Account', secondary='account_task', back_populates='tasks', lazy='subquery')


def find_by_project_id(project_id):
    try:
        session = Session()
        result = session.query(Task).filter(Task.p_id == project_id).all()

        session.close()

        return result
    except SQLAlchemyError as e:
        print("An error occurred:", str(e))


def find_by_account_id(account_id):
    try:
        session = Session()
        result = session.query(Task).join(Task.members).filter(Account.id == account_id).all()

        session.close()

        return result
    except SQLAlchemyError as e:
        print("An error occurred:", str(e))


def find_by_id(id):
    try:
        session = Session()
        result = session.query(Task).filter(Task.id == id).first()

        session.close()

        return result
    except SQLAlchemyError as e:
        print("An error occurred:", str(e))