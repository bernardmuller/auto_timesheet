from datetime import datetime
from threading import Timer
import application

hour = 22
minute = 24
x=datetime.today()
y=x.replace(day=x.day+1, hour=hour, minute=minute, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def Run():
    application.Run()
    #...

t = Timer(secs, Run)
t.start()