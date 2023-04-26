import csv

# with open('csv/employee_birthday.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column are {row}')
#             line_count += 1
#         else:
#             print(f'- {row[0]} is {row[1]}')
#             line_count += 1
#     print(f'Processed {line_count} lines.')

with open('csv/favorites.csv') as file:
    csv_reader = csv.DictReader(file)
    scratch, c, python = 0, 0, 0
    for row in csv_reader:
        favorite = row["language"]
        if favorite == "Scratch":
            scratch += 1
        elif favorite == "C":
            c += 1
        elif favorite == "Python":
            python += 1

print(f"Scratch: {scratch}")
print(f"C: {c}")
print(f"Python: {python}")
