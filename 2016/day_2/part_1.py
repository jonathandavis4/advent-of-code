with open('input.txt') as f:
    instructions = f.read().strip()

lines = instructions.split('\n')

current_number = 5

UP = 'U'
RIGHT = 'R'
DOWN = 'D'
LEFT = 'L'

def move(direction):
    # 1 2 3
    # 4 5 6
    # 7 8 9
    global current_number
    if direction == UP:
        if current_number in [1, 2, 3]:
            return
        else:
            current_number -= 3
    elif direction == RIGHT:
        if current_number in [3, 6, 9]:
            return
        else:
            current_number += 1
    elif direction == DOWN:
        if current_number in [7, 8, 9]:
            return
        else:
            current_number += 3
    elif direction == LEFT:
        if current_number in [1, 4, 7]:
            return
        else:
            current_number -= 1

for line in lines:
    for instruction in line:
        move(instruction)
    print current_number
