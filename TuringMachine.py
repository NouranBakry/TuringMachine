from Tape import Tape
from Transition import Transition

no_states = int(input("Enter the number of states:\n"))
alphabets = input("Enter alphabets in the form (alphabet,alphabet....):\n")
print(alphabets)
alpha = alphabets.split(",")
print(alpha)
no_alphabets = 0
for i in alpha:
    if i != "<":
        no_alphabets += 1

no_transitions = no_states * no_alphabets
print("Enter the transition function:\n")
all_trans = []



# user can enter use case
start_state = ""
for i in range(no_transitions):
    current_state = input("current state:\n")
    current_char = input("current input char:\n")
    next_state = input("new_state:\n")
    next_char = input("new state character: \n")
    action = input("action [Left(L), Right(R), Yes(Y), No(N)]:\n")
    new_transition = Transition(current_state, next_state, current_char, next_char, action)
    all_trans += [new_transition.get_trans()]
    if i == 0:
        start_state = current_state
print(all_trans)

head_position = int(input("Enter the position of the head:\n"))
tape_input = input("Enter the input on tape:\n")
# check if any undefined character on tape
for i in tape_input:
    if i not in alpha:
        print("Undefined character on tape")
        exit()

tape = Tape(head_position, tape_input)
t = tape.get_tape()
state = start_state
decision = ""
print("Tape: ", t)
while tape.head_position != len(t)-1:
    for trans in all_trans:
        char = tape.current()
        if trans[0] == state and trans[1] == char:
            print("Current state:", state)
            print("Currently on tape: ", char)
            state = trans[2]
            action = trans[4]
            if trans[3] != trans[1]:
                print("Write operation on tape ", trans[1], " is replaced by ", trans[3])
                tape.write(trans[3])
                print(trans)
                if action == "R" or action == "L":
                    print("Head position moved on action ", action)
                    tape.move_head(action)
                elif action == "Y":
                    decision = action
                    print("Decision: ", decision, " Your string is accepted")
                    print("Tape: ", tape.get_tape(), "\n")
                    print("Head position: ", tape.head_position, " at char:'", tape.current(), "'")
                    exit()
                else:
                    decision = action
                    print("Decision: ", decision, " Your string is rejected")
                    exit()
            elif trans[3] == trans[1]:
                print(trans)
                print("Read input on tape\n")
                if action == "R" or action == "L":
                    print("Head position moved on action ", action)
                    tape.move_head(action)
                elif action == "Y":
                    decision = action
                    print("Decision:", decision, " Your string is accepted\n")
                    print("Tape: ", tape.get_tape(), "\n")
                    print("Head position: ", tape.head_position, " at char:'", tape.current(), "'")
                    exit()
                else:
                    decision = action
                    print("Decision:", decision, " Your string is rejected")
                    exit()


