import os
import sys
from datetime import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from repository.get_race_g1 import get_race_schedule
from db_controller.controller import DBFunc


def main():
    db_func = DBFunc()
    data_list = get_race_schedule()
    for d in data_list:
        db_func.insert_data(
            race_date = d['race_date'],
            race_name = d['race_name'],
            race_detail_link = d['race_detail_link'],
            race_grade = d['race_grade'],
            race_city = d['race_city'],
            race_distance = d['race_distance'],
            race_terms = d['race_terms'],
            race_weight = d['race_weight'],
        )
        # db_func.insert_sample_data(
        #     # race_date = d['race_date'],
        #     race_name = d['race_name'],
        #     race_detail_link = d['race_detail_link'],
        #     race_grade = d['race_grade'],
        #     race_city = d['race_city'],
        #     # race_distance = d['race_distance'],
        #     # race_terms = d['race_terms'],
        #     # race_weight = d['race_weight'],
        # )
        # db_func.insert_sample_sql(
        #     race_date = d['race_date'],
        #     race_name = d['race_name'],
        #     race_detail_link = d['race_detail_link'],
        #     race_grade = d['race_grade'],
        #     race_city = d['race_city'],
        #     race_distance = d['race_distance'],
        #     race_terms = d['race_terms'],
        #     race_weight = d['race_weight'],
        # )
    # db_func.bulk_insert_data(data_list)


if __name__ == '__main__':
    main()