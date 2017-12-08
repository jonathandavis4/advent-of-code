import csv

spreadsheet = []
with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        new_row = [int(col) for col in row]
        spreadsheet.append(new_row)

differences = []
for row in spreadsheet:
    differences.append(max(row) - min(row))

checksum = sum(differences)
print checksum
