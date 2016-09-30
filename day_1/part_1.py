GO_UP = '('
GO_DOWN = ')'


# current_floor = 0
# with open('input.txt') as f:
#     instructions = f.read().strip()
# for instruction in instructions:
#     if instruction == GO_UP:
#         current_floor += 1
#     elif instruction == GO_DOWN:
#         current_floor -= 1
# print current_floor


with open('input.txt') as f:
    instructions = f.read().strip()
up_count = instructions.count(GO_UP)
down_count = instructions.count(GO_DOWN)
print up_count - down_count
