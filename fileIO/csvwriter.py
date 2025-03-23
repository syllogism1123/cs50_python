import csv

name = input("Enter your name: ")
house = input("Enter your house: ")
with open("csvwriter.csv", "a") as file:
    # writer = csv.writer(file)
    # writer.writerow([name, house])
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writerow({"name": name, "house": house})

