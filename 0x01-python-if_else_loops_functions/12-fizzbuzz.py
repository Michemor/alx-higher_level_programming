#!/usr/bin/python3
def fizzbuzz():
    """
    function prints 1-100, multiples of 3 Fizz of 5 Buzz and of
    both FizzBuzz
    Output: prints
    """
    for n in range(1, 101):
        if n % 3 == 0:
            print("Fizz", end=" ")
        elif n % 5 == 0:
            print("Buzz", end=" ")
        elif n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz", end=" ")
        elif n == 100:
            print("Buzz")
        else:
            print("{}".format(n), end=" ")
