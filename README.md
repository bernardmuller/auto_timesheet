#Auto Timesheet 2.0

# Description:
- "Auto Timesheet" is a automation program that helps the employee with the submission and tracking of said employee's timesheet - 
    A document that is submitted to admin at the end of each month containing descriptions of work the employee has worked on everyday.

# How it works: 
- The program creates a excel file that accumulates all timesheets in a Timebook of each year.
- It automatically launches on Windows Startup.
- On the initial launch of the program it stores user data that will be user to help fill in the timesheets and writing of monthly emails.
- At 16h00 everyday, a popup window will appear to submit that day's work description.
	- IMPORTANT NOTE: For those that like to enter more detailed descriptions, I have added the ability to submit multi-line
			  descriptions. Simply add a semicolon ";" after every line.
			  			  
			  e.g. "Bed Beach Villa sections ;Main Lodge pool details"
- Each line with more that 40 characters including symbols and spaces will automatically be split and appended.
- Use the 'Review' button to open the excel sheet .
- You can Find your timesheets in 'Documents\Timesheets\'

# Requirements: 
- Always have the "timesheet_template.xlsx" file in the templates folder.
- Keep "auto.exe" in it's directory.
- Do NOT rename anything!

# Set up:
- Move AutoTimesheet 2.0 folder to Program Files.
- Run auto.exe and enter name and surname along with email if you intend to use the autotime mailbot.(optional) 	

# Newest Features:
- Startup initializer automated
- Autotime bot intigration
    - bot will email you the latest updated timebook on the 1st of each month. This is for backup purposes.
- User data stored in json file. No need to enter you name again other than the first time you run the program.
- Timesheets saves to Documents.
- Auto Timesheet Logo.

# Future features: 
- For now I will terminate work on Auto Timesheet, but I will still fix found bugs and provide users the latest version.

# Known bugs: 
- Sometimes App wont terminate on Exit.
  
# Note:
In the even of a lost or corrupted file: Copy the template file from "/templates"
    and rename it, if you want to start from scratch, or check your latest email from Timesheet Bot.
 If you find any new bugs,or have any suggestions to improve the program please notify me.

#
Thank you for using Auto Timeheet!
# 
made by grizzly
