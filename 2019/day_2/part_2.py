from sys import exit
from copy import copy

with open('input.txt') as f:
    program = f.read().strip().split(',')
    program = map(int, program)

def run_program():
    global program
    index = 0
    while(run_instruction(index)):
        index += 4
    return program[0]

def run_instruction(index):
    global program

    instruction = program[index]

    if instruction == 99:
        return False
    else:
        location_1 = program[index + 1]
        value_1 = program[location_1]
        location_2 = program[index + 2]
        value_2 = program[location_2]
        result_location = program[index + 3]
        program[result_location]
        if instruction == 1:
            program[result_location] = value_1 + value_2
        elif instruction == 2:
            program[result_location] = value_1 * value_2
        return True

initial_program = copy(program)
for noun in range(100):
    for verb in range(100):
        program[1] = noun
        program[2] = verb
        if run_program() == 19690720:
            print(100 * noun + verb)
            exit()
        else:
            # Reset for the next time.
            program = copy(initial_program)
