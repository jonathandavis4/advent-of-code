with open('input.txt') as f:
    instructions = f.read().strip()


def is_possible(a, b, c):
    return a + b > c and b + c > a and c + a > b

lines = instructions.split('\n')
lengths = [line.split() for line in lines]
lengths_int = [map(int, length) for length in lengths]
lengths_possible_bool = [is_possible(*length) for length in lengths_int]
lengths_possible = [possible for possible in lengths_possible_bool if possible]

print len(lengths_possible)
