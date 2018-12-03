with open('input.txt') as f:
    input_data = f.read().strip()
box_ids = input_data.split('\n')

box_ids_2_letters = set()
box_ids_3_letters = set()

for box_id in box_ids:
    for letter in box_id:
        if box_id.count(letter) == 2:
            box_ids_2_letters.add(box_id)
        if box_id.count(letter) == 3:
            box_ids_3_letters.add(box_id)

checksum = len(box_ids_2_letters) * len(box_ids_3_letters)
print checksum
