from sqlalchemy import Column, String, Integer
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import relationship

from data.base import Base
from data.base import Session

from modal.account_organization import AccountOrganization
from modal.account_project import AccountProject
from modal.account_task import AccountTask


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    password = Column(String)

    organizations = relationship('Organization', secondary='account_organization', back_populates='members',
                                 lazy='subquery')
    projects = relationship('Project', secondary='account_project', back_populates='members', lazy='subquery')
    tasks = relationship('Task', secondary='account_task', back_populates='members', lazy='subquery')


def find_by_username(username):
    try:
        session = Session()
        account = session.query(Account).filter(Account.username == username).first()
        session.close()
        return account
    except SQLAlchemyError as e:
        print(e)


def find_by_id(id):
    try:
        session = Session()
        account = session.query(Account).filter(Account.id == id).first()
        session.close()
        return account
    except SQLAlchemyError as e:
        print(e)
