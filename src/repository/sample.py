from datetime import datetime, date

race_year = '2022'
str_race_date = '01/05(水)'
race_date = date(
    int(race_year), int(str_race_date.split('(')[0].split('/')[0]), int(str_race_date.split('(')[0].split('/')[1])
)

# race_date = date(2018, 2, 1)
print(race_date)