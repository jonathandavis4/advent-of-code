LEFT = '<'
UP = '^'
RIGHT = '>'
DOWN = 'v'

houses = {
    0: {
        0: 2
    }
}

current_location = {
    0: [0, 0],
    1: [0, 0]
}
current_santa = 1

with open('input.txt') as f:
    instructions = f.read().strip()
for instruction in instructions:
    current_santa = 0 if current_santa == 1 else 1
    if instruction == LEFT:
        santa_location = [current_location[current_santa][0] - 1, current_location[current_santa][1]]
    elif instruction == UP:
        santa_location = [current_location[current_santa][0], current_location[current_santa][1] - 1]
    elif instruction == RIGHT:
        santa_location = [current_location[current_santa][0] + 1, current_location[current_santa][1]]
    elif instruction == DOWN:
        santa_location = [current_location[current_santa][0], current_location[current_santa][1] + 1]
    current_location[current_santa] = santa_location

    if current_location[current_santa][0] not in houses:
        houses[current_location[current_santa][0]] = {}

    if current_location[current_santa][1] not in houses[current_location[current_santa][0]]:
        houses[current_location[current_santa][0]][current_location[current_santa][1]] = 1
    else:
        houses[current_location[current_santa][0]][current_location[current_santa][1]] += 1

count = 0
for x, data in houses.items():
    for y, visits in data.items():
        count += 1
print count
