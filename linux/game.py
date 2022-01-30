import pygame
import io
import pygame.display
pygame.display.init()

pygame.init()
output = io.StringIO
j = pygame.joystick.Joystick(0)
j.init()
hats = j.get_numhats()
class Controller(object):

    def __init__(self):
        print('controller inits')

    def check_input(self):
        input_sequence = ""
        while j.get_button(9)!=True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.JOYBUTTONDOWN:
                    if j.get_button(2):
                        input_sequence+="B"
                    elif j.get_button(1):
                        input_sequence+="A"
                hat = j.get_hat(0)
                if hat[1] == 1 and event.type==pygame.JOYHATMOTION:
                    input_sequence+="Up"
                elif hat[1] == -1 and event.type==pygame.JOYHATMOTION:
                    input_sequence+="Down"
                elif hat[0] == -1 and event.type==pygame.JOYHATMOTION:
                    input_sequence+="Left"
                elif hat[0] == 1 and event.type==pygame.JOYHATMOTION:
                    input_sequence+="Right"
        return input_sequence
