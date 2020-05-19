from openpyxl import *
import os, os.path
from  datetime import  date
from cal import Months

## there should always be a template file in the templates directory ##
def locate_template(directory):
    program_dir = directory   
    template_path = program_dir + '/templates/timesheet_template.xlsx'
    return template_path 



program_dir = 'C:/Users/Bernard/Dropbox/Personal/python/auto_timesheet'
temp_wb = load_workbook(str(locate_template(program_dir))) #timesheet_template.xlsx