import sys

import cowsay

char = input('Enter your character: ')

# Check if the character exists in cowsay module
if char in dir(cowsay):
    # Use getattr to call the corresponding function dynamically
    func = getattr(cowsay, char)
    func("Hello, World!")
else:
    print(f"No such function '{char}' found!")


