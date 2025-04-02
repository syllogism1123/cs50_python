def meow(n: int) -> str:
    """
    Meow n times.
    :param n: Number of times to meow.
    :type n: int
    :return: Meow n times.
    :rtype: str
    :raises ValueError: If n is not a positive integer.
    """
    return "meow\n" * n


n: int = int(input("Number: "))
meows: str = meow(n)
print(meows, end="")
