# needed to format times
from datetime import datetime
# needed for sleep function
from time import sleep
# needed to play sound
from pygame import mixer
# needed to send process to Alarm
import multiprocessing
# from multiprocessing import Process
# needed to instantiate alarm
from alarm import Alarm

mixer.init()
alarm = Alarm()

x = 0

while x == 0:
    sleep(1)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    alarm_time = "13:33:00"

    if current_time == alarm_time:
        print("alarm on, playing sound")
        mixer.music.load('Alarm.mp3')
        mixer.music.play()
        r = alarm.start_alarm()
        print(r)
        if(r == 1):
            print(r)
            mixer.music.stop()
            x = 1
