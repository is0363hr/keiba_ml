from datetime import datetime

race_year = '2022'
str_race_date = '01/05(水)'
race_date = datetime.strptime(race_year + '/' + str_race_date.split('(')[0], '%Y/%m/%d')

print(race_date)