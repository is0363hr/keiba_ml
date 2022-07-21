import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from repository.get_race_g1 import get_race_schedule
from db_controller.controller import DBFunc


def main():
    db_func = DBFunc()
    data_list = get_race_schedule()
    db_func.bulk_insert_data(data_list)


if __name__ == '__main__':
    main()