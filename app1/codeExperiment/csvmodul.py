import csv

with open ("app1/codeExperiment/weather.csv", 'r') as file:
    print("data")
    data = list(csv.reader(file))

city = input("enter city: " ).lower()

for row in data[1:]:
    if row[0] == city:
        print(row[1])

