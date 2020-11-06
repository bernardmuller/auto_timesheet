import smtplib
import user_data
from datetime import date
import time
from cal import Months


def get_year():
    today = date.today()
    year_num = today.year
    return str(year_num)

def get_day():
    today = date.today()
    day_num = today.day
    return str(day_num)


def get_prev_month():
    today = date.today()
    month_num = today.month
    if month_num == 1:
        month_num = 12
        month_name = Months[str(month_num)]
    else:
        month_name = Months[str(month_num-1)]
    return str(month_name)

# CHANGE THE FOLLOWING TO ENV VARIABLES
user = user_data.extract_data()
username = user['name']
user_mail = user['email']

EMAIL_ADDRESS = "autotimesheet.bot@gmail.com"
EMAIL_PASSWORD = "AT1234!@#"

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = f"{get_prev_month()}{get_year()} Timesheet"
    body = f"Hi {username}," \
           f"\n" \
           f"\nPlease find attached your timebook updated to {get_prev_month()}{get_year()}."
           f"\n This email serves the purpose as a notification and backup for your monthly timesheet." \
           f"\n" \
           f"\nRegards" \
           f"\nAuto Timesheet Bot"


    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, f"{user_mail}", msg)