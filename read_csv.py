import csv

def read_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

# Panggil fungsi dengan file CSV yang diberikan
read_csv('username.csv')