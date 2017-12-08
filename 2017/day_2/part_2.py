import csv

spreadsheet = []
with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        new_row = [int(col) for col in row]
        spreadsheet.append(new_row)

division_results = []
for row in spreadsheet:
    breaking = False
    for index, col in enumerate(row):
        if breaking:
            break
        
        for index_2, col_2 in enumerate(row):
            if breaking:
                break
                
            if index == index_2:
                continue
            
            if max([col, col_2]) % min([col, col_2]) == 0:
                division_result = max([col, col_2]) / min([col, col_2])
                division_results.append(division_result)
                breaking = True

print sum(division_results)
