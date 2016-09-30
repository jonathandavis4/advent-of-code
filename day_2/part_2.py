def length_for_wrapping(length, width, height):
    dimension_1, dimension_2 = sorted([length, width, height])[:2]
    return dimension_1 * 2 + dimension_2 * 2

def length_for_bow(length, width, height):
    return length * width * height

def total_length(present_size):
    return length_for_bow(*present_size) + length_for_wrapping(*present_size)

total_ribbon = 0
with open('input.txt') as f:
    for line in f:
        present_size = [int(n) for n in line.strip().split('x')]
        total_ribbon += total_length(present_size)
print total_ribbon
