GO_UP = '('
GO_DOWN = ')'


current_floor = 0
with open('input.txt') as f:
    instructions = f.read().strip()
for instruction_number, instruction in enumerate(instructions):
    if instruction == GO_UP:
        current_floor += 1
    elif instruction == GO_DOWN:
        current_floor -= 1
    if current_floor == -1:
        print instruction_number + 1
        break
