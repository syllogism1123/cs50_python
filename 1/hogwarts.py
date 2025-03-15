students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

# for _ in students:
#     print(_)

for k in students:
    print(k, students[k])

studentsList = [
    {
        "name": "Hermione",
        "house": "Gryffindor",
        "patronus": "Otter",

    },
    {
        "name": "Harry",
        "house": "Gryffindor",
        "patronus": "Stag",

    },
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronus": "Jack Russel terrier",

    },
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronus": None,

    }
]

for _ in studentsList:
    print(_["name"], _["house"], _["patronus"], sep=", ")
