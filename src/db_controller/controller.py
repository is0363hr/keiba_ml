# # #
# データベース管理(レース日程の全件取得、挿入)
# # #

from pprint import pprint
from domain.race_schedule import RaceSchedule
from db_controller.db_init import session
from datetime import datetime


class DBFunc:
    def __init__(self) -> None:
        pass        


    # レース日程をデータベースから取得する処理
    def get_all(self):
        race_schedules = session.query(RaceSchedule).all()
        data = []
        for race_schedule in race_schedules:
            data.append(
                {
                    "race_id": race_schedule.race_id,
                    "race_date": race_schedule.race_date,
                    "race_name": race_schedule.race_name,
                    "race_detail_link": race_schedule.race_detail_link,
                    "race_grade": race_schedule.race_grade,
                    "race_city": race_schedule.race_city,
                    "race_distance": race_schedule.race_distance,
                    "race_terms": race_schedule.race_terms,
                    "race_weight": race_schedule.race_weight,
                    "register_date": race_schedule.register_date,
                }
            )
        return data
    
    
    # レース日程をデータベースに挿入する処理
    def bulk_insert_data(self, data_list):
        now = datetime.now()
        race_list = []
        for d in data_list:
            race_list.append(
                RaceSchedule(
                    race_id = d['race_id'],
                    race_date = d['race_date'],
                    race_name = d['race_name'],
                    race_detail_link = d['race_detail_link'],
                    race_grade = d['race_grade'],
                    race_city = d['race_city'],
                    race_distance = d['race_distance'],
                    race_terms = d['race_terms'],
                    race_weight = d['race_weight'],
                    register_date = None,
                )
            )
        try:
            session.add_all(race_list)
            session.commit()
        except Exception as e:
            log = "{}: データベース追加失敗".format(now)
            print(log)
            print(e)
        else:
            log = "{}：追加完了".format(now)
            print(log)
        return


def main():
    db = DBFunc()
    pprint(db.get_all())


if __name__ == "__main__":
    main()
