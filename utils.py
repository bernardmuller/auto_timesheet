from openpyxl import *
import os, os.path
from  datetime import  date
from cal import Months


## there should always be a template file in the templates directory ##
def locate_template(directory):
    program_dir = directory    
    template_path = program_dir + '/templates/timesheet_template.xlsx'
    return template_path    


def locate_file(directory):
    program_dir = directory
    file_name = str(get_year()) + '_timeheets.xlsx'
    file_path = program_dir + '/timesheets/' + file_name
    return file_path


def check_timebook(program_dir):
    file_name = str(get_year()) + '_timeheets.xlsx'
    tb_exists = os.path.exists(program_dir + '/timesheets/' + file_name )
    if tb_exists == True:
        print('file already exists')
    else:
        create_file()


def get_month():
    today = date.today()
    month_num = today.month
    month_name = Months[str(month_num)]
    return month_name


def get_year():
    today = date.today()
    year_num = today.year    
    return year_num


def create_file():
    directory_to = 'timesheets'
    if not os.path.isdir(directory_to):
        os.makedirs(directory_to)
    file_name = str(get_year()) + '_timeheets.xlsx'
    temp_wb.save(os.path.join(directory_to, file_name))   

        
# def check_timeheet():
#     if str(get_month()) in wb.sheetnames:
#         pass
#     else:
#         wb.add_sheet(book[str(get(month))])        
#         pass
   

if __name__ == "__main__": 
    ## user required to insert path to program ##
    program_dir = 'C:/Users/Bernard/Dropbox/Personal/python/auto_timesheet'
  
    ## current year workbook object ##
    wb = load_workbook(str(locate_file(program_dir)))

    ## checks if current years timebook exists, if not creates new ##
    check_timebook(program_dir)  
         
    
