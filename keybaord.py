class Keyboard():

    def __init__(self):
        print('keyboard inits')

    def check_input(self):
        input_sequence = ""
        user_input = input('')
        input_sequence = ''
        for char in user_input:
            if char == 'u':
                input_sequence += 'Up'
            elif char == 'd':
                input_sequence += 'Down'
            elif char == 'l':
                input_sequence += 'Left'
            elif char == 'r':
                input_sequence += 'Right'
            elif char == 'b':
                input_sequence += 'B'
            elif char == 'a':
                input_sequence += 'A'
        return input_sequence
