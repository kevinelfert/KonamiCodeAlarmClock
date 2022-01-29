"""
January 28 2021
Kevin Elfert

Konami Alarm Clock
an alarm clock that is turned off by inputting the konami code
"""
from sys import platform
from sys import platform
if platform == "linux" or platform == "linux2":
    # linux
    pass
elif platform == "darwin":
    # OS X
    from mac.game import Controller
elif platform == "win32":
    from windows.game import Controller

# need to handle error when controller is not plugged in
try:
    controller = Controller()
except:
    pass

input_sequence = controller.input_sequence
correct_sequence = "UpUpDownDownLeftRightLeftRightBA"
print(input_sequence)


if input_sequence == correct_sequence:
    print("Alarm Off")