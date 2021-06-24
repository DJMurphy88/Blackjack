import csv
from os import write

def load_money():
    money = []
    with open("money.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            money.append(row)
        return money

def save_money(money):
    with open("money.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(money)