import datetime
import os
import os.path
from datetime import date

from openpyxl import *
from openpyxl.styles import *

from cal import Months



class Clock:   


    def get_day(self):
        today = date.today()
        day_num = today.day
        #month_name = Months[str(month_num)]
        return str(day_num)
    

    def get_month(self):
        today = date.today()
        month_num = today.month
        month_name = Months[str(month_num)]
        return str(month_name)


    def get_year(self):
        today = date.today()
        year_num = today.year    
        return str(year_num)


    def get_week_of_month(self):
        day_of_month = datetime.datetime.now().day
        week_number = (day_of_month - 1) // 7 + 1
        return week_number



class TimebookSetup:

    def Save(self):
        directory_to = 'timesheets'
        file_name = Clock.get_year() + '_timeheets.xlsx'
        if not os.path.isdir(directory_to):
            os.makedirs(directory_to)
        wb.save(os.path.join(directory_to, file_name))
        print('File Saved')

    ## there should always be a template file in the templates directory ##
    def locate_template(self, directory):
        program_dir = directory    
        template_path = program_dir + '/templates/timesheet_template.xlsx'
        return template_path    


    def locate_timebook(self, directory):
        program_dir = directory
        file_name = Clock.get_year() + '_timeheets.xlsx'
        file_path = program_dir + '/timesheets/' + file_name
        return file_path    


    def Create(self, program_dir):
        directory_to = 'timesheets'
        file_name = Clock.get_year() + '_timeheets.xlsx'
        if not os.path.isdir(directory_to):
            os.makedirs(directory_to)
        tb_exists = os.path.exists(program_dir + '/timesheets/' + file_name )
        if tb_exists == True:
            ## Prompt if file already exists , override? ##
            print('Timebook for ' + Clock.get_year() + ' already exists')
            prompt= input('Override? Y/N :')
            if prompt in ['Y', 'y']:
                temp_wb.save(os.path.join(directory_to, file_name)) 
                print('Timebook for ' + Clock.get_year() + ' created')
            else:
                print()                    
        else:
            temp_wb.save(os.path.join(directory_to, file_name)) 
            print('Timebook for ' + Clock.get_year() + ' created')      

            
    
class TimesheetSetup: 

    def Create(self):
        if 'Sheet1' in wb.sheetnames:
            self.rename_Sheet1()              
        else: 
            pass      
        if Clock.get_month() in wb.sheetnames:
            pass
        else:     
            print('Sheet ' + Clock.get_month() + ' added in workbook')   
            wb.create_sheet(Clock.get_month())
            self.copy_from_template() 
            # TimebookSetup.Save()
        #self.EnterCredentials()



    def rename_Sheet1(self):
        sheet = wb['Sheet1']
        sheet.title = 'Template' 


    def copy_from_template(self):
        temp_sheet = wb['Template']
        active_sheet = wb[Clock.get_month()]
        for i in range(1, 7):
            for j in range(1, 4):
                active_sheet.cell(row=i, column=j).value = temp_sheet.cell(row=i, column=j).value


    def EnterCredentials(self):
        active_sheet = wb[Clock.get_month()]
        username = active_sheet['B4'].value
        current_month =  str(Clock.get_month())
        if active_sheet['B3'].value == current_month:
            pass
        else:
            active_sheet['A7'].value = current_month
        if username.isalpha:
            pass
        else:
            new_user = input('Please enter your name: ')
            username = new_user
            print('username saved')



    

class Editor:

    def day_Entry(self):

        desc_value = input('Description: ')
        day_list = [(str(Clock.get_day()), desc_value, '*')] 
        for d in day_list:                           
            active_sheet.append(d)
        print(f'Description for {Clock.get_day()} {Clock.get_month()} submitted.')


    def curr_week(self):
        week = Clock.get_week_of_month()
        curr_week = 'Week' + str(week)  
        return str(curr_week)  
      
    ## following appends work descriptions to excel file
    def month_Entries(self):      
        current_week = self.curr_week()
        if date.today().weekday() == 0:
            if active_sheet.cell(row=active_sheet.max_row,column=1).value == Clock.get_day():
                print('Daily Entry Satisfied')
            elif active_sheet.cell(row=active_sheet.max_row,column=1).value == 'PROJECT':
                active_sheet.cell(row=active_sheet.max_row+1,column=1).value = current_week 
                self.day_Entry()                    
            else:
                if active_sheet.cell(row=active_sheet.max_row,column=1).value == current_week:                    
                    self.day_Entry()
                else:                    
                    active_sheet.cell(row=active_sheet.max_row+1,column=1).value = current_week           
                    self.day_Entry()
        elif not date.today().weekday() == 0 or 5 or 6:
            if active_sheet.cell(row=active_sheet.max_row,column=1).value == Clock.get_day():
                print('Daily Entry Satisfied')
            elif active_sheet.cell(row=active_sheet.max_row,column=1).value == 'PROJECT':
                active_sheet.cell(row=active_sheet.max_row+1,column=1).value = current_week
                self.day_Entry()               
            else:
                self.day_Entry()


class Styler:

    def Column_sizes(self):
        active_sheet = wb[Clock.get_month()]
        active_sheet.column_dimensions['A'].width = 17
        active_sheet.column_dimensions['B'].width = 48
        active_sheet.column_dimensions['C'].width = 17


    def Borders(self):
        active_sheet = wb[Clock.get_month()]
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")

        for i in range(1, 4):
            active_sheet.cell(row=6,column=i).border = Border(top=thin, left=thin, right=thin, bottom=double)

        for i in range(7, active_sheet.max_row+1):
            for j in range(1, 4):
                active_sheet.cell(row=i,column=j).border = Border(top=thin, left=thin, right=thin, bottom=thin)

    def Headers(self):
        active_sheet = wb[Clock.get_month()]
        medium_font = Font(name='Calibri', bold=True, size= 16)
        center_align = Alignment(horizontal='center')
        right_align = Alignment(horizontal='right')
        large_font = Font(name='Calibri', bold=True, size= 18)


        #---Timesheet---#
        active_sheet['A1'].value = 'TIMESHEET'
        active_sheet['A1'].font = large_font

        active_sheet['B1'].value = 'CNR'
        active_sheet['C1'].value = '.Architects'
        active_sheet['B1'].font = Font(name='Bauhaus 93', size=16, bold=True)
        active_sheet['C1'].font = Font(name= 'New Times Roman', size=16, bold=False)
        active_sheet['B1'].alignment = Alignment(horizontal='right')


        for i in range(1, 4):
            active_sheet.cell(row=6, column=i).font = medium_font
            active_sheet.cell(row=6, column=i).alignment = center_align


    def style(self):
        self.Column_sizes()
        self.Borders()
        self.Headers()


  
    
if __name__ == "__main__":

#---------Directory----------#
    ## Add in Options box in GUI ##
    program_dir = 'C:/Users/Bernard/PycharmProjects/auto_timesheet'


#--------Class_Objects-------#
    Clock = Clock() 
    TimebookSetup = TimebookSetup()
    TimesheetSetup = TimesheetSetup()
    # GUI window 2 
    Editor = Editor()
    Style = Styler()


#----------template----------#    
    temp_wb = load_workbook(str(TimebookSetup.locate_template(program_dir)))


#------------Run-------------#
    TimebookSetup.Create(program_dir)
    wb = load_workbook(str(TimebookSetup.locate_timebook(program_dir)))    
    TimesheetSetup.Create()
    active_sheet = wb[Clock.get_month()]
    Editor.month_Entries()
    Style.style()


    # for i in range(7, active_sheet.max_row):
    #         for j in range(1, 4):
    #             active_sheet.cell(row=i,column=j).border = Border(left=Side(border_style='Thick Outside Border', color='FF000000')
    #

#-----------Save-------------#    
    TimebookSetup.Save()

