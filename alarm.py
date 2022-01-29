from datetime import datetime
from time import sleep
from playsound import playsound

x = 0 

while x==0:
    sleep(1)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    alarm_time = "21:10:00"
    if current_time == alarm_time:
        print("alarm on, playing sound")
        playsound('Alarm.wav')
        x = 1

    


