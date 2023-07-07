from sqlalchemy import Column, Date, Integer, PrimaryKeyConstraint, ForeignKey
from data.base import Base
from data.base import Session
from sqlalchemy.exc import SQLAlchemyError


class AccountTask(Base):
    __tablename__ = 'account_task'
    __table_args__ = (PrimaryKeyConstraint('a_id', 't_id'), )

    a_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    t_id = Column(Integer, ForeignKey('task.id'), primary_key=True)
    role = Column(Integer)
