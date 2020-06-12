import math

""""
1.  Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included).
    The numbers obtained should be printed in a comma-separated sequence on a single line.
"""


def get_valid_numbers(range_start=None, range_stop=None):
    try:
        if range_start is None or range_stop is None:
            raise ValueError

        if not isinstance(range_start, int) or not isinstance(range_stop, int):
            raise TypeError

        valid_nums = []
        range_start = int(range_start)
        range_stop = int(range_stop)

        for num in range(range_start, range_stop + 1):
            if num % 7 == 0 and num % 5 != 0:
                valid_nums.append(num)

        print(*valid_nums, sep=', ')

    except ValueError:
        print(f"Please provide input values {ValueError}")

    except TypeError:
        print(f"Please provide valid input number {TypeError}")


get_valid_numbers(2000, 3200)

"""
2.  Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order 
    with a space between first name and last name.
"""


def get_name_reverse_order():
    name = list()

    first_name = input('Please enter first name: ').strip()
    last_name = input('Please enter last name: ').strip()

    name.extend([first_name, last_name])
    rev_name = [i[::-1] for i in name]

    print("\nReverse First and Last name's letters is: " + " ".join(rev_name))
    print("Reverse First and Last Name is: " + " ".join(name[::-1]))
    print("Reverse First and Last Name's with letters is: " + " ".join(rev_name[::-1]))


get_name_reverse_order()

"""
3.  Write a Python program to find the volume of a sphere with diameter 12 cm.
    Formula: V=4/3 * π * r 3
"""


def get_sphere_volume(diameter=None):
    try:
        if diameter is None:
            raise ValueError

        radius = diameter / 2
        volume = (4 / 3) * math.pi * (radius ** 3)
        print(f"Sphere's volume is: {volume:.3f} cm\u00b3")

    except ValueError:
        print(f"Please provide diameter value {ValueError}")

    except TypeError:
        print(f"Please provide valid input number for diameter {TypeError}")


get_sphere_volume(12)
