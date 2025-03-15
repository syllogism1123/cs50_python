name = input("Enter your name: ")

match name:
    case "python":
        print("python")

    case _:
        print(name)
