# # #
# レース日程のドメイン
# # #

from sqlalchemy import Column, Integer, String, DateTime
from db_controller.db_init import Base

class RaceSchedule(Base):
    __tablename__ = "RACE_SCHEDULE"
    
    race_id = Column(Integer, primary_key=True, autoincrement=True)
    race_date = Column(DateTime)
    race_name = Column(String(30), nullable=False)
    race_detail_link = Column(String(100), nullable=False)
    race_grade = Column(String(30), nullable=False)
    race_city = Column(String(30), nullable=False)
    race_distance = Column(String(30), nullable=False)
    race_terms = Column(String(30), nullable=False)
    race_weight = Column(String(30), nullable=False)
    register_date = Column(DateTime)
    