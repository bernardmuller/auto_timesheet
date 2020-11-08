#|------Auto Timesheet 2.0------|

# New Features:
- Startup initializer automated
- Autotime bot intigration
    - bot will email you the latest updated timebook on the 1st of each month. This is for backup purposes.
- User data stored in json file. No need to enter you name again other than the first time you run the program.

# Requirements: 
- Always have the "timesheet_template.xlsx" file in the templates folder.
- Keep "auto.exe" in it's directory.
- Do NOT rename anything!

# Set up:
- Move AutoTimesheet 2.0 folder to My Documents.
- Run auto.exe and enter name and surname along with email if you intend to use the autotime mailbot.(optional) 			

# How it works: 
- The program creates a excel file that accumulates all your timesheets in one Timebook.
- The program always runs in the background and at a specific time each day you will receive a popup to notify you of your daily submission,
  the program will open up on the Submission window where you can fill in your daily work description

	- IMPORTANT NOTE: For those that like to enter more detailed descriptions, I have added the ability to submit multi-line
			  descriptions. Simply add a semicolon ";" after every line.
			  
			  e.g. "Bed Beach Villa sections ;Main Lodge pool details ;Made Bernard some Coffee cause he cool guy! ;)"
	
	- Also: Each line with more that 40 characters including symbols and spaces will automatically be split and appended. So please review 
		your timesheet for any words that are being cut off, before sending it to Pam.

# Future features: 
- For now I will terminate work on Autotimesheet as I do not think it needs to be any more complicated.
- But I will still fix bugs when I find them and give users the latest version.

# Known bugs: 
- Program won't create a timebook on its own like in prototype version. To avoid this, always have a 
  .xlsx file in the timesheets directory with the name correlating to the current year. For example:
  "2020_timesheets.xlsx". 
  
	- Note: If your file were to be corrupted or lost. Copy the template file from "/templates"
	        and rename it.

#
Thank you for using AutoTimeheet! If you find any new bugs,or have any suggestions to improve the program PLSSS let me know!       pls...


#|-------made by grizzly--------|
