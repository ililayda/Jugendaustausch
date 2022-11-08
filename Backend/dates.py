import datetime
import sqlite3
from sqlite3 import Error

current_date = datetime.datetime.now()
today = datetime.date.today()
fourteen_days = datetime.timedelta(days=14)
fourteen_days_ago = today - fourteen_days
current_day = current_date.day
current_month = current_date.month
current_year = current_date.year
next_year = current_year + 1
three_years_ago = current_year - 3
current_table_name = 'participants_' + str(current_year)
next_year_table_name = 'participants_' + str(next_year)
three_years_ago_table_name = 'participants_' + str(three_years_ago)