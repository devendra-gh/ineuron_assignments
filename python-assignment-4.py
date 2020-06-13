
"""
1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    Function to take the length of the sides of triangle from user should be defined in the parent class
    and function to calculate the area should be defined in subclass.
"""


# Definition for Triangle Class
class Triangle:
    # Initialized initial state for Triangle
    def __init__(self, side_a, side_b, side_c):
        self.a = side_a
        self.b = side_b
        self.c = side_c

    # Get method for get semi perimeter
    def get_semi_perimeter(self):
        return (self.a + self.b + self.c) / 2


# Definition for Area Class
class Area(Triangle):
    # Initialized parent state to child class
    def __init__(self, *args):
        super().__init__(*args)

    # Get method for getting triangle area
    def get_triangle_area(self):
        s = self.get_semi_perimeter()
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

        return f"Area of the triangle is: {area} unit\u00b2"


triangle_area = Area(3, 4, 5)
print(triangle_area.get_triangle_area())


"""
1.2 Write a function filter_long_words() that takes a list of words and an integer n 
    and returns the list of words that are longer than n.
"""


# Definition for Filter long words function
def filter_long_words(words_list=None, n=None):
    try:
        if words_list is None or n is None:
            raise ValueError

        if not words_list or not isinstance(words_list, list) or not isinstance(n, int):
            raise TypeError

        else:
            return list(filter(lambda word: len(word) > n, words_list))

    except ValueError:
        print(f'Please provide argument {ValueError}')

    except TypeError:
        print(f'Please provide valid argument {TypeError}')


print(filter_long_words(['a', 'aa', 'aaa', 'aaaa', 'aaaaa'], 3))

"""
2.1 Write a Python program using function concept that maps list of words into a list of integers
    representing the lengths of the corresponding words.
    Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as
    [2,3,4] Here 2,3 and 4 are the lengths of the words in the list.
"""


# Definition for Get List of word's length function
def get_list_of_words_length(array=None):
    try:
        if array is None:
            raise ValueError

        if not array or not isinstance(array, list):
            raise TypeError

        else:
            return [len(word) for word in array]

    except ValueError:
        print(f'Please provide argument {ValueError}')

    except TypeError:
        print(f'Please provide valid argument {TypeError}')


print(get_list_of_words_length(['ab', 'cde', 'erty']))

"""
2.2 Write a Python function which takes a character (i.e. a string of length 1) 
    and returns True if it is a vowel, False otherwise.
"""


# Definition for is vowel function
def is_vowel(char=None):
    char = char.strip()

    try:
        if char is None:
            raise ValueError

        if not char or not isinstance(char, str):
            raise TypeError

        else:
            char = char[0].lower()
            vowel = ['a', 'e', 'i', 'o', 'u']

            if char in vowel:
                return True
            return False

    except ValueError:
        print(f'Please provide argument {ValueError}')

    except TypeError:
        print(f'Please provide valid argument {TypeError}')


print(is_vowel('S'))
