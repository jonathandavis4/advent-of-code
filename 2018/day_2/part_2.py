import sys


def distance(a, b):
    distance = 0
    for index, letter in enumerate(a):
        if b[index] != letter:
            distance += 1
    return distance


def common_letters(a, b):
    common_letters = []
    for index, letter in enumerate(a):
        if b[index] == letter:
            common_letters.append(letter)
    return ''.join(common_letters)


with open('input.txt') as f:
    input_data = f.read().strip()
box_ids = input_data.split('\n')

for box_id_1 in box_ids:
    for box_id_2 in box_ids:
        if distance(box_id_1, box_id_2) == 1:
            print common_letters(box_id_1, box_id_2)
            sys.exit()
