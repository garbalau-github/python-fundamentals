import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column are {row}')
            line_count += 1
        else:
            print(f'- {row[0]} is {row[1]}')
            line_count += 1
    print(f'Processed {line_count} lines.')
