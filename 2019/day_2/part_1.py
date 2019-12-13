with open('input.txt') as f:
    program = f.read().strip().split(',')
    program = map(int, program)

def run_program():
    index = 0
    while(run_instruction(index)):
        index += 4

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
        if instruction == 1:
            program[result_location] = value_1 + value_2
        elif instruction == 2:
            program[result_location] = value_1 * value_2
        return True

program[1] = 12
program[2] = 2
run_program()
print program[0]