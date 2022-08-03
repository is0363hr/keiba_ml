# # #
# レース日程のドメイン
# # #
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from datetime import datetime
from sqlalchemy import Column, Integer, String, Date, Sequence, INT, TIMESTAMP
from db_controller.db_init import Base, ENGINE

class RaceSchedule(Base):
    __tablename__ = "RACE_SCHEDULE"
    
    # race_id = Column(Integer, Sequence('race_id_seq'), primary_key=True, autoincrement=True)
    race_id = Column(INT, primary_key=True, autoincrement=True)
    race_date = Column(String(30), nullable=True)
    race_name = Column(String(30), nullable=False)
    race_detail_link = Column(String(100), nullable=False)
    race_grade = Column(String(30), nullable=False)
    race_city = Column(String(30), nullable=False)
    race_distance = Column(String(30), nullable=False)
    race_terms = Column(String(30), nullable=False)
    race_weight = Column(String(30), nullable=False)

    
    
class Sample(Base):
    __tablename__ = "SAMPLE"
    
    race_id = Column(INT, primary_key=True, autoincrement=True)
    # race_date = Column(String(30), nullable=False)
    race_name = Column(String(30), nullable=False)
    race_detail_link = Column(String(100), nullable=False)
    race_grade = Column(String(30), nullable=False)
    race_city = Column(String(30), nullable=False)
    # race_distance = Column(String(30), nullable=False)
    # race_terms = Column(String(30), nullable=False)
    # race_weight = Column(String(30), nullable=False)
    

if __name__ == "__main__":
    # create table
    Base.metadata.create_all(ENGINE)