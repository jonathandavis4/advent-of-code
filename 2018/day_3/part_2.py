import re


with open('input.txt') as f:
    input_data = f.read().strip()

claimed_inches = {}

for claim in input_data.split('\n'):
    claim_id, x_min, y_min, width, height = re.match('^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$',
        claim).groups()
    claim_id, x_min, y_min, width, height = int(claim_id), int(x_min), int(y_min), int(width), int(
        height)
    
    for x in range(x_min, x_min + width):
        for y in range(y_min, y_min + height):
            if x in claimed_inches:
                if y in claimed_inches[x]:
                    claimed_inches[x][y] += 1
                else:
                    claimed_inches[x][y] = 1
            else:
                claimed_inches[x] = {y: 1}

smallest_x = min(claimed_inches.keys())
largest_x = max(claimed_inches.keys())

smallest_y = 9999
largest_y = 0
for x, y_data in claimed_inches.items():
    for y, _ in y_data.items():
        if y < smallest_y:
            smallest_y = y
        if y > largest_y:
            largest_y = y

duplicates = 0
for x in range(smallest_x, largest_x + 1):
    for y in range(smallest_y, largest_y + 1):
        if y not in claimed_inches[x]:
            continue
        if claimed_inches[x][y] > 1:
            duplicates += 1

for claim in input_data.split('\n'):
    claim_id, x_min, y_min, width, height = re.match('^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$', claim).groups()
    claim_id, x_min, y_min, width, height = int(claim_id), int(x_min), int(y_min), int(width), int(height)
    
    overlaps = False
    
    for x in range(x_min, x_min + width):
        for y in range(y_min, y_min + height):
            if x in claimed_inches:
                if y in claimed_inches[x]:
                    if claimed_inches[x][y] > 1:
                        overlaps = True
    
    if not overlaps:
        print claim_id
