import tkinter as tk
from time import strftime, sleep
from datetime import datetime
from turtle import width
from pygame import mixer
from alarm import Alarm


class App():

    def __init__(self):
        # main window
        self.main_window = tk.Tk()
        self.main_window.geometry('600x400')

        # main label
        self.main_lbl = tk.Label(
            self.main_window, text='Konami Code Alarm Clock', font=('calibri', 40, 'bold'))
        self.main_lbl.pack(anchor=tk.CENTER)

        # current time label
        self.time_lbl = tk.Label(
            self.main_window, text='Current Time', font=('calibri', 30, 'bold'))
        self.time_lbl.pack(anchor=tk.CENTER)

        # time label
        self.current_time_lbl = tk.Label(
            self.main_window, font=('calibri', 30, 'bold'))
        self.current_time_lbl.pack(anchor=tk.CENTER)

        # set alarm label
        self.set_alarm_lbl = tk.Label(
            self.main_window, text='Alarm Time', font=('calibri', 30, 'bold'))
        self.set_alarm_lbl.pack(anchor=tk.CENTER)

        # create frame for times
        self.frame = tk.Frame(self.main_window)
        self.frame.pack(anchor=tk.CENTER)

        # create option menu for hours
        self.hour = tk.StringVar(self.main_window)
        self.hours = ('01', '02', '03', '04', '05', '06', '07',
                      '08', '09', '10', '11', '12')
        self.hour.set(self.hours[0])

        self.hrs = tk.OptionMenu(self.frame, self.hour, *self.hours)
        self.hrs.configure(width=5, height=2, font=('calibri', 30))
        self.hrs.pack(side=tk.LEFT)

        # create option menu for minutes
        self.minute = tk.StringVar(self.main_window)
        self.minutes = ('00', '05', '10', '15', '20', '25', '30', '35','40', '45', '50', '55', '60')
        self.minute.set(self.minutes[0])

        self.mins = tk.OptionMenu(self.frame, self.minute, *self.minutes)
        self.mins.configure(width=5, height=2, font=('calibri', 30))
        self.mins.pack(side=tk.LEFT)

        # create radio buttons for AM or PM
        self.ampm = tk.StringVar()
        self.ante_meridian = tk.Radiobutton(
            self.frame, text='AM', variable=self.ampm, value='AM', indicatoron=False, font=('calibri', 10, 'bold'))
        self.ante_meridian.configure(height=3, width=5)

        self.post_meridian = tk.Radiobutton(
            self.frame, text='PM', variable=self.ampm, value='PM', indicatoron=False, font=('calibri', 10, 'bold'))
        self.post_meridian.configure(height=3, width=5)

        self.ante_meridian.pack()
        self.post_meridian.pack()

        # create a set alarm button
        self.set_alarm_btn = tk.Button(self.main_window, text='Set Alarm', command=lambda: self.set_alarm(
            self.hour.get(), self.minute.get(), self.ampm.get()))
        self.set_alarm_btn.pack(anchor=tk.CENTER)

        # start the main loop
        self.alarm_time_string = ''
        self.time()
        self.main_window.mainloop()

    def time(self):
        # need to:
        #   get current time and format it
        #   check if current time is equal to alarm time
        #       if it is, start alarm
        #   put that time on the time label
        #   update time every second
        self.current_time_string = strftime('%I:%M:%S %p')
        self.current_time_lbl.config(text=self.current_time_string)
        self.current_time_lbl.after(1000, self.time)
        # check current time string against set alarm string
        if(self.current_time_string == self.alarm_time_string):
            self.start_alarm()

    def set_alarm(self, hour, minute, ampm):
        self.alarm_time_string = '{hr}:{min}:00 {mer}'.format(
            hr=hour, min=minute, mer=ampm)
        self.alarm_time_string = self.alarm_time_string
        print(self.alarm_time_string)

    def start_alarm(self):
        # currently when I set the alarm time
        # the current time label is frozen
        mixer.init()
        alarm = Alarm()
        print("alarm on, playing sound")
        mixer.music.load('Alarm.mp3')
        mixer.music.play()
        r = alarm.start_alarm()
        if(r == 1):
            mixer.music.stop()
            self.main_window.destroy()
        else:
            self.start_alarm()


if __name__ == '__main__':
    app = App()
