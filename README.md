#|------Auto Timesheet 1.3------|


# Requirements: 
- Always have the "timesheet_template.xlsx" file in the templates folder.
- Keep "AutoTimesheet.exe" in it's directory.
- Do NOT rename anything!

# Set up automatic startup: 
- Move AutoTimesheet 1.3 folder to My Documents.
- Run program once by double clicking "auto.exe" and close. This allows the program to save its directory.
- Right click on "initialize.bat" and click edit.
- Copy contents of "directory.txt" to "initialize.bat", followed by "\auto.exe". Save and close. Don't delete 'START' in the .bat file	
- Press Win + R.
- Type "shell:startup", click 'Ok'.
- Create a shortcut of "initialize.bat" file and copy it into the startup folder.
- Restart computer.			

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
- The ability to set a custom scheduled time for daily submission.
- The ability for the program to email you your current month's timesheet at the end of each month. This is a bit tricky for security reasons.

# Known bugs: 
- Program won't create a timebook on its own like in prototype version. To avoid this, always have a 
  .xlsx file in the timesheets directory with the name correlating to the current year. For example:
  "2020_timesheets.xlsx". 
  
	- Note: If your file were to be corrupted or lost. Copy the template file from "/templates"
	        and rename it.

#
Thank you for using AutoTimeheet! If you find any new bugs,or have any suggestions to improve the program PLSSS let me know!       pls...


#|-------made by grizzly--------|
