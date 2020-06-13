"""
1.  Create the below pattern using nested for loop in Python.
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
"""


# Definition for Get Pyramid function
def get_Pyramid(columns=None):
    try:
        if columns is None:
            raise ValueError

        columns = int(columns)
        if not isinstance(columns, int) or columns <= 0:
            raise TypeError

        pattern_top = list()
        pattern_bottom = list()

        for row in range(columns):
            for col in range(row):
                pattern_top.append('* ')
            pattern_top.append('\n')

            for col in range(columns - row):
                pattern_bottom.append('* ')
            pattern_bottom.append('\n')

        print(*(pattern_top + pattern_bottom), sep='')

    except ValueError:
        print(f"Please provide value for Columns {ValueError}")

    except TypeError:
        print(f"Please provide valid number of Columns {TypeError}")


get_Pyramid(5)

"""
2.  Write a Python program to reverse a word after accepting the input from the user.
    Sample Output:
    Input word: ineuron 
    Output: norueni
"""


# Definition for Get Reverse Word function
def get_reverse_word():
    while True:
        input_word = input("Please enter a word: ").strip()

        if input_word == '':
            continue
        else:
            print(f"Reverse word is: {input_word[::-1]}")
            break


get_reverse_word()
