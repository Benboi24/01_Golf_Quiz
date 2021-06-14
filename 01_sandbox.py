import csv

with open('golf_v3.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    for row in reader:
        print(row[1])

print(data)

