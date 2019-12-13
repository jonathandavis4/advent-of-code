with open('input.txt') as f:
    wires = f.read().strip().split('\n')

data = {
    0: {
        0: '+'
    }
}
for symbol, wire in zip(['-', '|'], wires):
    current_x = 0
    current_y = 0

    other_symbol = '-' if symbol == '|' else '|'

    sections = wire.split(',')
    for section in sections:
        direction = section[0]
        distance = int(section[1:])

        for _ in range(distance):
            if direction == 'D':
                current_y -= 1
            elif direction == 'U':
                current_y += 1
            elif direction == 'L':
                current_x -= 1
            elif direction == 'R':
                current_x += 1

            if current_x in data:
                if current_y in data[current_x]:
                    if data[current_x][current_y] == other_symbol:
                        data[current_x][current_y] = '+'
                else:
                    data[current_x][current_y] = symbol
            else:
                data[current_x] = {}
                data[current_x][current_y] = symbol

manhattan_distance = lambda x, y: abs(x) + abs(y)

pairs = []
for x in data.keys():
    for y, value in data[x].items():
        if data[x][y] == '+':
            if x == 0 and y == 0:
                continue
            pairs.append([x, y])
distances = [manhattan_distance(x, y) for x, y in pairs]
print(min(distances))
