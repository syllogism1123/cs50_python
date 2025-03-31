class Student:
    def __init__(self, name, house, patronus):
        self.name = name
        self.house = house
        self.patronus = patronus

    @classmethod
    def get(cls):
        name = input("Please enter your name: ")
        house = input("Please enter your house: ")
        patronus = input("Please enter your patronus: ")
        return cls(name, house, patronus)

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐎"
            case "Otter":
                return "🦦"
            case "Jack Russel terrier":
                return "🐶"
            case _:
                return "🪄"

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Student house is invalid")
        self._house = house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Student name is required")
        self._name = name


def main():
    student = Student.get()
    #student._house = "Number Four, Privet Drive"
    print(student)
    print("Expecto Patronum!")
    print(student.charm())


if __name__ == "__main__":
    main()
