with open('input.txt') as f:
    sequence = f.read().strip()

repeated_digits = []

for index, digit in enumerate(sequence):
    index_to_check = (index + (len(sequence) / 2)) % len(sequence)
    
    if index == len(sequence) - 1:
        if sequence[index_to_check] == digit:
            repeated_digits.append(int(digit))
    elif sequence[index_to_check] == digit:
        repeated_digits.append(int(digit))

print sum(repeated_digits)
