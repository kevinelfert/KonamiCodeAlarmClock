import pygame
import io

pygame.init()
output = io.StringIO

# https://stackoverflow.com/questions/15057114/pygame-does-not-detect-joystick?noredirect=1&lq=1
j = pygame.joystick.Joystick(0)
j.init()
hats = j.get_numhats()
class Controller(object):
    input_sequence = ""
    while j.get_button(6)!=True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                if j.get_button(0):
                    input_sequence+="A"
                elif j.get_button(1):
                    input_sequence+="B"
                elif j.get_button(11):
                    input_sequence+="Up"
                elif j.get_button(12):
                    input_sequence+="Down"
                elif j.get_button(13):
                    input_sequence+="Left"
                elif j.get_button(14):
                    input_sequence+="Right"

