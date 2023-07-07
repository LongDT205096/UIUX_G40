from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.exc import SQLAlchemyError

from data.base import Base
from data.base import Session

from modal.account import Account


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)

    o_id = Column(Integer, ForeignKey('organization.id'))
    organization = relationship('Organization', back_populates='projects', lazy='subquery')

    members = relationship('Account', secondary='account_project', back_populates='projects', lazy='subquery')

    title = Column(String)
    join_code = Column(String)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)

    tasks = relationship('Task', back_populates='project', lazy='subquery')


def find_by_account_id(account_id):
    try:
        session = Session()
        result = session.query(Project).join(Project.members).filter(Account.id == account_id).all()

        session.close()

        return result
    except SQLAlchemyError as e:
        print("An error occurred:", str(e))


def find_by_id(id):
    try:
        session = Session()
        result = session.query(Project).filter(Project.id == id).first()

        session.close()

        return result
    except SQLAlchemyError as e:
        print("An error occurred:", str(e))
