import sys

if len(sys.argv) < 2:
    #    raise IndexError("Invalid number of arguments")
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is ", arg)
