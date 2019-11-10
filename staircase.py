
"""
Drawing a staircase with strings

Author: Oğuzhan Çölkesen
"""

def draw_staircase():
    """Prints a staircase composed of `*' signs with user-specified dimensions.

    Here's an example:

    height = 5, width = 3
    * * *
    . . * * *
    . . . . * * *
    . . . . . . * * *
    . . . . . . . . * * *
    """
    height = int(input("Enter the height of the staircase: "))
    width = int(input("Enter the width of the staircase: "))

    for i in range (height):
        for j in range (width):
            for k in range (i * (width - 1)):
                print (".", end = " ")
                i = 0
                # Setting i as 0 so that the loop only runs once inside the other loop.
            print("*", end = " ")
        print()