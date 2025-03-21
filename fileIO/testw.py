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

with open("test.csv", "w") as file:
    file.write("name,house,patronus\n")  # Write the header row
    for _ in studentsList:
        file.write(f"{_['name']},{_['house']},{_['patronus']}\n")
