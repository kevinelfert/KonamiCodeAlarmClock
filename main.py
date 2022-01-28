"""
January 28 2021
Kevin Elfert

Konami Alarm Clock
an alarm clock that is turned off by inputting the konami code
"""

from game import Controller

# need to handle error when controller is not plugged in
try:
    controller = Controller()
except:
    pass

input_sequence = controller.input_sequence
correct_sequence = "UpUpDownDownLeftRightLeftRightBA"


if input_sequence == correct_sequence:
    print("Alarm Off")