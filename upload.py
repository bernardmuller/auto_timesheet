import ezsheets
from datetime import date
import os

def get_year():
    today = date.today()
    year_num = today.year
    return str(year_num)

def upload_timebook():
    timesheets_directory = 'timesheets'
    file_name = get_year() + '_timebook.xlsx'
    ezsheets.upload(os.path.join(timesheets_directory, file_name))
    print(f'{file_name} Uploaded to drive.')
