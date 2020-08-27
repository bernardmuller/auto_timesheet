import smtplib

# CHANGE THE FOLLOWING TO ENV VARIABLES
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = ""

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = "Auto Timesheet Mail Bot"
    body = "Hi,\n\nThis is a test mail.\n\nRegards\nAuto Timesheet Bot"




    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, " ", msg)
    auto