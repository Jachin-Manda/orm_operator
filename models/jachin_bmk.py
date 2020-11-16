__author__ = "Jachin Manda"
__copyright__ = "DevsBranch"
__date__ = "16/11/2020"

from sqlalchemy import (Integer, Column, String, Date)

from models.config import Base, db_engine


class BmkTable(Base):
    __tablename__ = 'bmk_table'
    __table_args__ = {'extend_existing': True}
    bmk_id = Column('bmk_id', Integer, primary_key=True)
    bmk_name = Column('bookmark_name', String(50))
    bmk_url = Column('bookmark_url', String(200))
    bmk_desc = Column('bookmark_description', String(50))
    date = Column(Date)

    def __init__(self, bmk_name, bmk_url, bmk_desc, date):
        self.bmk_name = bmk_name
        self.bmk_url = bmk_url
        self.bmk_desc = bmk_desc
        self.date = date

    def __repr__(self):
        return f"<Object name: {self.bmk_name}"


Base.metadata.create_all(db_engine)
