from sqlalchemy import Column, Date, Integer, PrimaryKeyConstraint, ForeignKey
from data.base import Base
from data.base import Session
from sqlalchemy.exc import SQLAlchemyError


class AccountProject(Base):
    __tablename__ = 'account_project'
    __table_args__ = (PrimaryKeyConstraint('a_id', 'p_id'), )

    a_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    p_id = Column(Integer, ForeignKey('project.id'), primary_key=True)
    role = Column(Integer)
    join_date = Column(Date)
