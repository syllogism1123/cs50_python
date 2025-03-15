def hello(to="World"):
    print("Hello", to)


def main():
    name = input("What is your name?").strip().title()
    num = int(input("What is your number?"))
    first, last = name.split()
    print(f"{name}")
    print(f"{first}")
    hello(name)
    print(square(num))


def square(n):
    return pow(n, 2)


# comments
# name = name.capitalize()

main()
