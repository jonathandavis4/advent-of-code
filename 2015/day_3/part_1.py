LEFT = '<'
UP = '^'
RIGHT = '>'
DOWN = 'v'

houses = {
    0: {
        0: 1
    }
}

current_location = [0, 0]

with open('input.txt') as f:
    instructions = f.read().strip()
for instruction in instructions:
    if instruction == LEFT:
        current_location = [current_location[0] - 1, current_location[1]]
    elif instruction == UP:
        current_location = [current_location[0], current_location[1] - 1]
    elif instruction == RIGHT:
        current_location = [current_location[0] + 1, current_location[1]]
    elif instruction == DOWN:
        current_location = [current_location[0], current_location[1] + 1]

    if current_location[0] not in houses:
        houses[current_location[0]] = {}

    if current_location[1] not in houses[current_location[0]]:
        houses[current_location[0]][current_location[1]] = 1
    else:
        houses[current_location[0]][current_location[1]] += 1

count = 0
for x, data in houses.items():
    for y, visits in data.items():
        count += 1
print count
