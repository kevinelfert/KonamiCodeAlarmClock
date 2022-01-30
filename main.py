# needed to format times
from datetime import datetime
# needed for sleep function
from time import sleep
#needed to play sound
from playsound import playsound
# needed to send process to Alarm
import multiprocessing
# from multiprocessing import Process
# needed to instantiate alarm
# from alarm import Alarm


# alarm = Alarm()

x = 0 

while x==0:
    sleep(1)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    alarm_time = "19:38:00"
    if current_time == alarm_time:
        print("alarm on, playing sound")
        # playsound('Alarm.mp3')
        p = multiprocessing.Process(target=playsound, args=("Alarm.wav",))
        p.start()
        # # r = alarm.start_alarm()
        # # if(r == 1):
        # #     p.terminate()
        # #     playsound(None)
        # #     x = 1
        input("press ENTER to stop playback")
        p.terminate()
        

