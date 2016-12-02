# Functions

def turn_left():
    global facing
    facing = {
        'n': 'w',
        'e': 'n',
        's': 'e',
        'w': 's'
    }[facing]

def turn_right():
    global facing
    facing = {
        'n': 'e',
        'e': 's',
        's': 'w',
        'w': 'n'
    }[facing]

# Data storage.

movement_counts = {
    'n': 0,
    'e': 0,
    's': 0,
    'w': 0
}
facing = 'n'

# Main

with open('input.txt') as f:
    instructions = f.read().strip().split(', ')

for instruction in instructions:
    turn, blocks = instruction[0], instruction[1:]

    if turn == 'L':
        turn_left()
    else:
        turn_right()

    movement_counts[facing] += int(blocks)

horizontal_movement = abs(movement_counts['e'] - movement_counts['w'])
vertical_movement = abs(movement_counts['n'] - movement_counts['s'])

print horizontal_movement + vertical_movement
