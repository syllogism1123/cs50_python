import csv

students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)
#
#
# def get_name(student):
#     return student["name"]
#
#
# def get_house(student):
#     return student["house"]
#
#
# for student in sorted(students, key=get_name, reverse=True):
#     print(student)
#
# print("*************************************************")
#
# for student in sorted(students, key=lambda student:student["name"], reverse=True):
#     print(student)

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "house": row["house"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(student)
