import csv

with open('golf.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print = (row[1])