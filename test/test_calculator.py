import pytest

from calculator import square


def main():
    test_square()


def test_square():
    assert square(5) == 25
    assert square(3) == 9


def test_str():
    with pytest.raises(TypeError):
        square("cat")


if __name__ == '__main__':
    main()
