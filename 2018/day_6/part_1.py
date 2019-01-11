def load_coordinates(input_data):
    coordinates = []
    coord_id_as_int = ord('A')
    for item in input_data:
        x = int(item.split(', ')[0])
        y = int(item.split(', ')[1])
        coord_id_as_int += 1
        coordinates.append((chr(coord_id_as_int), x, y))

    xs = [coordinate[1] for coordinate in coordinates]
    ys = [coordinate[2] for coordinate in coordinates]

    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)
    
    return coordinates, min_x, min_y, max_x, max_y

def make_empty_grid(min_x, min_y, max_x, max_y):
    grid = {}
    for x in range(min_x, max_x + 1):
        if x not in grid:
            grid[x] = {}
        for y in range(min_y, max_y + 1):
            if y not in grid[x]:
                grid[x][y] = '.'
    return grid

def manhattan_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def coordinates_contains(x, y, coordinates):
    for coord_id, x2, y2, in coordinates:
        if x == x2 and y == y2:
            return True
    return False

def plot_nearest_coordinate(x, y, coordinates, grid):
    data = {}
    for coord in coordinates:
        if coordinates_contains(x, y, coordinates):
            continue
        data[coord[0]] = manhattan_distance(x, y, coord[1], coord[2])
    min_distance = 9999
    for coord, distance in data.items():
        if distance < min_distance:
            min_distance = distance
    matching_coords = []
    
    for coord, distance in data.items():
        if distance == min_distance:
            matching_coords.append(coord)
            
    if len(matching_coords) == 1:
        grid[x][y] = matching_coords[0]
    return grid

def draw(grid):
    for x, ys in grid.items():
        print ''.join(value for y, value in ys.items() if value is not None)

def get_letters(grid):
    letters = set()
    for x, ys in grid.items():
        for y, letter in ys.items():
            letters.add(letter)
    letters.remove('.')
    return letters

def count_letter(letter, grid):
    count = 0
    for x, ys in grid.items():
        for y, letter2 in ys.items():
            if letter == letter2:
                count += 1
    return count

def main():
    with open('input.txt') as f:
        input_data = f.read().strip().split('\n')
    coordinates, min_x, min_y, max_x, max_y = load_coordinates(input_data)
    grid = make_empty_grid(min_x, min_y, max_x, max_y)
    for coord_id, x, y in coordinates:
        grid[x][y] = coord_id
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            grid = plot_nearest_coordinate(x, y, coordinates, grid)
    # draw(grid)
    letters = get_letters(grid)
    letter_counts = []
    for letter in letters:
        letter_counts.append((letter, count_letter(letter, grid)))
    print sorted(letter_counts, key=lambda x: x[1], reverse=True)

main()
