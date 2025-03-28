import re

name = input("Enter your name: ").strip()

if matches := re.search(r"^(.+),\s*(.+)$", name):
    last, first = matches.groups()
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
