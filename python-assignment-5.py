"""
1.  Write a function to compute 5/0 and use try/except to catch the exceptions.
"""


# Definition to Get Quotient Value
def get_quotient_value(dividend=None, divisor=None):
    try:
        if dividend is None or divisor is None:
            raise ValueError

        if not isinstance(dividend, int) or not isinstance(divisor, int):
            raise TypeError

        else:
            quotient = dividend / divisor
            print(quotient)
            return quotient

    except ValueError:
        print('Please provide Dividend and Divisor')

    except TypeError:
        print('Please provide number for Dividend and Divisor')

    except ZeroDivisionError:
        print(f"Divisor can't be Zero {ZeroDivisionError}")


get_quotient_value(5, 0)

"""
2.  Implement a Python program to generate all sentences where subject is in ["Americans", "Indians"] 
    and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].

    Hint: Subject,Verb and Object should be declared in the program as shown below.

    subjects=["Americans ","Indians"] 
    verbs=["play","watch"] 
    objects=["Baseball","Cricket"]
    
    Output should come as below:
        Americans play Baseball.
        Americans play Cricket.
        Americans watch Baseball.
        Americans watch Cricket.
        Indians play Baseball.
        Indians play Cricket.
        Indians watch Baseball.
        Indians watch Cricket.
"""


# Definition to Get Sentences
def get_sentences():
    subjects = ["Americans ", "Indians"]
    verbs = ["play", "watch"]
    objects = ["Baseball", "Cricket"]

    sentence = [subject + ' ' + verb + ' ' + obj + '.\n' for subject in subjects for verb in verbs for obj in objects]

    print(*sentence, sep='')


get_sentences()
