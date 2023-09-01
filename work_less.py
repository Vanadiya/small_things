import datetime
import os

os.system("cls")
dt_now = datetime.datetime.now()
start_date = datetime.datetime(year=2023, month=8, day=28, hour=0, minute=0, second=0)
count_day = dt_now - start_date
count_day = str(count_day)
day_list = count_day.split(' days, ')

print(f'Мои безработные дни уже составляют: {day_list[0]}')
