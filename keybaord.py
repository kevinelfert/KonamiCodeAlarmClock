class Keyboard():

    def __init__(self):
        print('keyboard inits')

    def check_input(self):
        input_sequence = ""
        user_input = input('')
        input_sequence = ''
        for char in user_input:
            if char == 'u' or char == 'U':
                input_sequence += 'Up'
            elif char == 'd' or char == 'D':
                input_sequence += 'Down'
            elif char == 'l' or char == 'L':
                input_sequence += 'Left'
            elif char == 'r' or char == 'R':
                input_sequence += 'Right'
            elif char == 'b' or char == 'B':
                input_sequence += 'B'
            elif char == 'a' or char == 'A':
                input_sequence += 'A'
        return input_sequence
