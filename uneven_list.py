"""
Demonstrates that lists of lists do not have to be
perfecly squared. Fix the program to print the whole
list of lists.

Author: Oğuzhan Çölkesen
"""

def display_uneven_list():
    uneven_list = [ [1,2,3], [10,20,30,40] ]

    height = len(uneven_list)
    width = len(uneven_list[0])

    for row in range(height):
        cur_width = len(uneven_list[row])
        
        for col in range(cur_width):
            print(uneven_list[row][col], end=" ")
        print()
