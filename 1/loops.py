# i = 3
#
# while i > 0:
#     print("meow")
#     i = i - 1


for i in range(3):
    print(i)

print("python\n" * 3, end="")

while True:
    n = int(input("What is n?"))
    if n > 0:
        break

for _ in range(n):
    print("meow")
