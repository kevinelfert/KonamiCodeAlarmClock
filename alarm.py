from sys import platform
from multiprocessing import Process
# if platform == "linux" or platform == "linux2":
#     # linux
#     from linux.game import Controller
# elif platform == "darwin":
#     # OS X
#     from mac.game import Controller
# elif platform == "win32":
#     from windows.game import Controller

# need to handle error when controller is not plugged in
class Alarm:
    def __init__(self):
        print("clock inits")

    def start_alarm(self):
        # if(type(p) == Process):
            print("Alarm on")
            try:
                if platform == "linux" or platform == "linux2":
                    # linux
                    from linux.game import Controller
                elif platform == "darwin":
                    # OS X
                    from mac.game import Controller
                elif platform == "win32":
                    from windows.game import Controller
                correct_sequence = "UpUpDownDownLeftRightLeftRightBA"
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
                print(input_sequence)
                if input_sequence == correct_sequence:
                    print("Alarm Off")
                    return 1
            except:
                pass


if __name__ == '__main__':
    alarm = Alarm()
    alarm.start_alarm()