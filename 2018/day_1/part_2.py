import operator as op

with open('input.txt') as f:
    input_data = f.read().strip()
frequency_changes = input_data.split('\n')

current_frequency = 0
frequencies_reached = set()

breaking = False

while not breaking:
    for frequency_change in frequency_changes:
        operator = frequency_change[0]
        operator_map = {
            '+': op.add,
            '-': op.sub
        }
        operator = operator_map[operator]

        value = int(frequency_change[1:])

        current_frequency = operator(current_frequency, value)

        if current_frequency in frequencies_reached:
            print current_frequency
            breaking = True
            break

        frequencies_reached.add(current_frequency)