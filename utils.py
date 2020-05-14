from openpyxl import *
import os
from  datetime import  date
from cal import Months


def locate_template(directory):
    program_dir = directory
    template_dir = 'templates'
    if not os.path.isdir(template_dir):
            os.makedirs(template_dir)
    template_path = program_dir + '/templates/timesheet_template.xlsx'
    return template_path    


def get_month():
    today = date.today()
    month_num = today.month
    month_name = Months[str(month_num)]
    return month_name


def save():
    directory_to = 'timesheets'
    if not os.path.isdir(directory_to):
        os.makedirs(directory_to)
    file_name = str(get_month()) + '.xlsx'
    wb.save(os.path.join(directory_to, file_name))

    
if __name__ == "__main__":
    program_dir = 'C:/Users/Bernard/Dropbox/Personal/python/auto_timesheet'
    template_path = locate_template(program_dir)
    wb = load_workbook(template_path)
    save()
    pass
