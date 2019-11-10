
"""
Printing out a multiplication table

Author: Oğuzhan Çölkesen
"""


def print_multiplication_table():
    """
    Prints out the multiplication table for 13, up to 13 x 20.
    """
    number = 13
    product = 0
    for i in range (1, 21):
        product = number * i
        print (number, "times", i, "=", product)