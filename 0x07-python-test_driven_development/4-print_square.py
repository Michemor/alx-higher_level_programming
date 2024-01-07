#!/usr/bin/python3
def print_square(size):
    """
    print_square - prints square based on given charaters according to size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for n in range(size):
            for m in range(size):
                print("#", end="")
            print("")
