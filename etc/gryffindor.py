students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]
gryffindors = [
    student["name"]
    for student in students if student["house"] == "Gryffindor"
]

list_filter = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(list_filter, key=lambda student: student["name"]):
    print(gryffindor["name"])
