import re

email = input("Enter your email: ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.|edu|org|com|io$", email, re.IGNORECASE):
    # "^\w+@\w+\.edu$" same as "^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$"
    print("Valid")
else:
    print("Invalid")
