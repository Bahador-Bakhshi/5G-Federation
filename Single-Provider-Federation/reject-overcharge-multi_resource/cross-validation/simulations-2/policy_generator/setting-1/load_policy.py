import csv

policy = {}

with open('policy.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        elif len(row) > 0:
            line_count += 1
            key = (row[0], row[1], row[2], row[3], row[4], row[5])
            policy[key] = row[6]


print(policy)


