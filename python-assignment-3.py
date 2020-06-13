"""
1.1 Write a Python Program to implement your own myreduce() function
    which works exactly like Python's built-in function reduce()
"""


def my_reduce(func, list_values):
    result = list_values[0]

    for list_value in list_values[1:]:
        result = func(result, list_value)

    return result


"""
1.2 Write a Python program to implement your own myfilter() function 
    which works exactly like Python's built-in function filter()
"""


def my_filter(func, list_values):
    result = []

    for list_value in list_values:
        if func(list_value):
            result.append(list_value)

    return result


"""
2.  Implement List comprehensions to produce the following lists. 
    Write List comprehensions to produce the following Lists
    
    ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
    ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
    [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
    [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
    [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
"""

"""
get_list_one
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
"""


def get_list_one(list_one=None, iteration=None):
    try:
        if list_one is None or iteration is None:
            raise ValueError

        if not isinstance(list_one, list) or not isinstance(iteration, int):
            raise TypeError

        else:
            return [col * row for col in list_one for row in range(1, iteration + 1)]

    except ValueError:
        print(f'Please provide arguments {ValueError}')

    except TypeError:
        print(f'Please provide valid arguments {TypeError}')


print(get_list_one(['x', 'y', 'z'], 4))


"""
get_list_two
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
"""


def get_list_two(list_two=None, iteration=None):
    try:
        if list_two is None or iteration is None:
            raise ValueError

        if not isinstance(list_two, list) or len(list_two) == 0 or not isinstance(iteration, int):
            raise TypeError

        else:
            return [list_two[col] * row for row in range(1, iteration + 1) for col in range(len(list_two))]

    except ValueError:
        print(f'Please provide arguments {ValueError}')

    except TypeError:
        print(f'Please provide valid arguments {TypeError}')


print(get_list_two(['x', 'y', 'z'], 4))


"""
get_list_three
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
"""


def get_list_three(start=None, iteration=None):
    try:
        if start is None or iteration is None:
            raise ValueError

        if not isinstance(start, int) or not isinstance(iteration, int):
            raise TypeError

        else:
            return [[row + col] for row in range(iteration) for col in range(start, iteration + start)]

    except ValueError:
        print(f'Please provide arguments {ValueError}')

    except TypeError:
        print(f'Please provide valid arguments {TypeError}')


print(get_list_three(2, 3))

"""
get_list_four
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
"""


def get_list_four(start=None, iteration=None):
    try:
        if start is None or iteration is None:
            raise ValueError

        if not isinstance(start, int) or not isinstance(iteration, int):
            raise TypeError

        else:
            return [[col+row for col in range(start, iteration + start)] for row in range(iteration)]

    except ValueError:
        print(f'Please provide arguments {ValueError}')

    except TypeError:
        print(f'Please provide valid arguments {TypeError}')


print(get_list_four(2, 4))

"""
get_list_five
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
"""


def get_list_five(list_five=None):
    try:
        if list_five is None:
            raise ValueError

        if not isinstance(list_five, list) or len(list_five) == 0:
            raise TypeError

        else:
            iteration = len(list_five) + 1
            return [(col, row) for row in range(1, iteration) for col in range(1, iteration)]

    except ValueError:
        print(f'Please provide arguments {ValueError}')

    except TypeError:
        print(f'Please provide valid arguments {TypeError}')


print(get_list_five([1, 2, 3]))
