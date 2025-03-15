from calculator import square


def main():
    test_square()


def test_square():
    assert square(5) == 25
    assert square(3) == 9


if __name__ == '__main__':
    main()
