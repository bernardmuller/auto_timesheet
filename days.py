import datetime
day_of_month = datetime.datetime.now().day
week_number = (day_of_month - 1) // 7 + 1

print(week_number)