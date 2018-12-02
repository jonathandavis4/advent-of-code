import operator as op

with open('input.txt') as f:
    input_data = f.read().strip()
frequency_changes = input_data.split('\n')

current_frequency = 0

for frequency_change in frequency_changes:
    operator = frequency_change[0]
    operator_map = {
        '+': op.add,
        '-': op.sub
    }
    operator = operator_map[operator]

    value = int(frequency_change[1:])

    current_frequency = operator(current_frequency, value)

print current_frequency
