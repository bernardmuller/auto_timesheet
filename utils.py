import pandas as pd

# with pd.ExcelFile('timesheet.xls') as xls:
#     df1 = pd.read_excel(xls, 'Sheet1')
#     df2 = pd.read_excel(xls, 'Sheet2')

table = {
    'project': ["week1", "week2", "week3", "week4"],
    'description of work': [['desc1', 'desc1.1', 'desc1.2', 'desc1.3'], 'desc2', 'desc3', 'desc4'],
    'office use': ['use1', 'use2', 'use3', 'use4'],
}

timesheet = pd.DataFrame(table)
print(timesheet)