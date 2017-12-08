with open('input.txt') as f:
    sequence = f.read().strip()

repeated_digits = []
for index, digit in enumerate(sequence):
    if index == len(sequence) - 1:
        if sequence[0] == digit:
            repeated_digits.append(int(digit))
    elif sequence[index + 1] == digit:
        repeated_digits.append(int(digit))

print sum(repeated_digits)
