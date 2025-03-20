# name = input("What's your name? ")
#
# with open("name.csv", "a") as file:
#     file.write(f"{name}\n")


# with open("name.csv", "r") as file:
#     for line in file: #iterable
#         print("Hello,", line.rstrip())
#
# names = []
# with open("name.csv") as file:
#     for line in file:
#         names.append(line.rstrip())
#
#
# for name in sorted(names):
#     print(name)

with open("name.csv", "r") as file:
    for line in sorted(file, reverse=True):  # iterable
        print("Hello,", line.rstrip())
