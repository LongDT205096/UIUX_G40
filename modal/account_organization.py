from sqlalchemy import Column, Date, Integer, PrimaryKeyConstraint, ForeignKey
from data.base import Base


class AccountOrganization(Base):
    __tablename__ = 'account_organization'
    __table_args__ = (PrimaryKeyConstraint('a_id', 'o_id'), )

    a_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    o_id = Column(Integer, ForeignKey('organization.id'), primary_key=True)
    role = Column(Integer)
    join_date = Column(Date)
