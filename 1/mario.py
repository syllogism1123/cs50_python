def print_column(height):
    for _ in range(height):
        print("#")


def print_row(width):
    print("# " * width)


def print_square(size):
    for i in range(size):
        for j in range(size):
            print("# ", end="")
        print()


def main():
    #    print_column(3)
    #    print_row(3)
    print_square(3)


main()
