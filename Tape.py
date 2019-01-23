"""This class controls and stores the inputs on the tape, it can move the head,
    read, write and return the tape"""


class Tape:
    def __init__(self, head_position, input_string):
        blank_symbol = "#"
        self.input_string = input_string
        self.tape = []
        self.head_position = head_position
        for c in self.input_string:
            if c == "<":
                self.tape += c
                self.head_position += 1
            else:
                self.tape += c
        self.tape += blank_symbol

    def move_head(self, action):
        if action == "R":
            self.head_position += 1
        elif action == "L":
            self.head_position -= 1
        else:
            return

    def get_tape(self):
        return self.tape

    def current(self):
        return self.tape[self.head_position]

    def read(self):
        return self.tape[self.head_position]

    def write(self, char):
        self.tape[self.head_position] = char


