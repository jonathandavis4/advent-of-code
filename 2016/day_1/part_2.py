import sys

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

visited_locations = []
current_location = (0, 0)
facing = 'n'
movement_counts = {
    'n': 0,
    'e': 0,
    's': 0,
    'w': 0
}

# Main

with open('input.txt') as f:
    instructions = f.read().strip().split(', ')

for instruction in instructions:
    turn, blocks = instruction[0], instruction[1:]

    if turn == 'L':
        turn_left()
    else:
        turn_right()

    for count in xrange(int(blocks)):
        if facing == 'n':
            current_location = (current_location[0], current_location[1] - 1)
        elif facing == 'e':
            current_location = (current_location[0] + 1, current_location[1])
        elif facing == 's':
            current_location = (current_location[0], current_location[1] + 1)
        else:
            current_location = (current_location[0] - 1, current_location[1])

        movement_counts[facing] += 1

        if current_location in visited_locations:
            horizontal_movement = abs(movement_counts['e'] - movement_counts['w'])
            vertical_movement = abs(movement_counts['n'] - movement_counts['s'])
            print horizontal_movement + vertical_movement
            sys.exit(0)

        visited_locations.append(current_location)
