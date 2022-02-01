from sys import platform

class Alarm:
    def __init__(self):
        print("clock inits")

    def start_alarm(self):
        correct_sequence = "UpUpDownDownLeftRightLeftRightBA"
        print("Alarm on")
        input_sequence=''
        try:
            # use a ps4 controller
            if platform == "linux" or platform == "linux2":
                # linux
                from linux.controller import Controller
            elif platform == "darwin":
                # OS X
                from mac.controller import Controller
            elif platform == "win32":
                #windows
                from windows.controller import Controller

            controller = Controller()
            input_sequence = controller.check_input()
            # if the input sequence does 
            # not equal the correct sequence,
            # the program continues to output times
            #
            # the program should notify the user that the 
            # input sequence is wrong and allow the user
            # to input another sequence
            #
            # currently does not work

            # this print is printing none
        except:
            #use the computer keyboard
            from keybaord import Keyboard

            keyboard = Keyboard()
            input_sequence = keyboard.check_input()

        print(input_sequence)
        if input_sequence == correct_sequence:
            print("Alarm Off")
            return 1

if __name__ == '__main__':
    alarm = Alarm()
    alarm.start_alarm()