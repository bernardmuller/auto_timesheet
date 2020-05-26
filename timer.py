import schedule
import time

def job(t):
    print ("I'm working...", t)
    return

schedule.every().minute.at(":30").do(job,'It is one minute later.')

while True:
    schedule.run_pending()
    time.sleep(1) # wait one minute