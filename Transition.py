"""This class defines and stores the transitions"""


class Transition:
    def __init__(self, current, next_state, current_char, next_char, action):
        self.current = current
        self.next = next_state
        self.current_char = current_char
        self.next_char = next_char
        self.action = action
        self.transition = [self.current, self.current_char, self.next, self.next_char, self.action]

# this returns a list of the transitions
    def get_trans(self):
        return self.transition
