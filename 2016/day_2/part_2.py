with open('input.txt') as f:
    instructions = f.read().strip()

lines = instructions.split('\n')

current_position = (2, 2)  # horizontal, vertical

UP = 'U'
RIGHT = 'R'
DOWN = 'D'
LEFT = 'L'

KEYPAD = [
    [None, None, '1', None, None],
    [None, '2', '3', '4', None],
    ['5', '6', '7', '8', '9'],
    [None, 'A', 'B', 'C', None],
    [None, None, 'D', None, None]
]

MAX_X = len(KEYPAD[0]) - 1
MAX_Y = len(KEYPAD) - 1

def move(direction):
    global current_position
    if direction == UP:
        if current_position[0] == 0:
            return
        else:
            if KEYPAD[current_position[0] - 1][current_position[1]] is None:
                return
            current_position = (current_position[0] - 1, current_position[1])
    elif direction == RIGHT:
        if current_position[1] == MAX_X:
            return
        else:
            if KEYPAD[current_position[0]][current_position[1] + 1] is None:
                return
            current_position = (current_position[0], current_position[1] + 1)
    elif direction == DOWN:
        if current_position[0] == MAX_Y:
            return
        else:
            if KEYPAD[current_position[0] + 1][current_position[1]] is None:
                return
            current_position = (current_position[0] + 1, current_position[1])

    elif direction == LEFT:
        if current_position[1] == 0:
            return
        else:
            if KEYPAD[current_position[0]][current_position[1] - 1] is None:
                return
            current_position = (current_position[0], current_position[1] - 1)


for line in lines:
    for instruction in line:
        move(instruction)
    print KEYPAD[current_position[0]][current_position[1]]
