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

column = "problem"  # "language"

with open('csv/favorites.csv') as file:
    csv_reader = csv.DictReader(file)
    counts = {}
    for row in csv_reader:
        favorite = row[column]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

favorite = input("Favorite: ")
if favorite in counts:
    print(f"{favorite}: {counts[favorite]}")
