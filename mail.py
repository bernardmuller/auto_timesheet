import smtplib
from datetime import date
from cal import Months
import os
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import user_data

def get_year():
    today = date.today()
    year_num = today.year
    return str(year_num)

file = os.getcwd() + "/timesheet/" + get_year() + '_timebook.xlsx'

def send_mail(files=file,
              server="127.0.0.1"):
    assert isinstance(send_to, list)


    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(body))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)


    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


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

user = user_data.extract_data()
username = user['name']

send_from = "autotimesheet.bot@gmail.com"
send_to = user['email']
EMAIL_PASSWORD = "AT1234!@#"
send_from = "autotimesheet.bot@gmail.com"
subject = f"{get_prev_month()}{get_year()} Timesheet"
body = f"Hi {username}," \
        f"\n" \
        f"\nPlease find attached your timebook updated to {get_prev_month()}{get_year()}."
        f"\n This email serves the purpose as a notification and backup for your monthly timesheet." \
        f"\n" \
        f"\nRegards" \
        f"\nAuto Timesheet Bot"
file = os.getcwd() + "/timesheet/" + get_year() + '_timebook.xlsx'