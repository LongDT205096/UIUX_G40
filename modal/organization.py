from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.exc import SQLAlchemyError

from data.base import Base
from data.base import Session

from modal.account import Account


class Organization(Base):
    __tablename__ = 'organization'

    id = Column(Integer, primary_key=True)
    join_code = Column(String, unique=True)
    name = Column(String)

    projects = relationship('Project', back_populates='organization', lazy='subquery')

    members = relationship('Account', secondary='account_organization', back_populates='organizations', lazy='subquery')


def find_by_account_id(account_id):
    try:
        session = Session()
        result = session.query(Organization).join(Organization.members).filter(Account.id == account_id).all()

        session.close()

        return result
    except SQLAlchemyError as e:
        print("An error occurred:", str(e))


def find_by_id(id):
    try:
        session = Session()
        result = session.query(Organization).filter(Organization.id == id).first()

        session.close()

        return result
    except SQLAlchemyError as e:
        print("An error occurred:", str(e))
