
"""
Calculating the number of visible trophies on a shelf

Author: Oğuzhan Çölkesen
"""

def count_visible():
    """
    Computes the number of visible trophies on a shelf, given their heights
    in order.
    """
    heights = eval(input("Enter trophy heights: "))
    trophy_counter = 1
    loop_counter = 0
    number_smaller = 0
    
    for i in range(1, len(heights)):
        
        while loop_counter < i:
            if max(heights[loop_counter], heights[i]) == heights[i] and heights[loop_counter] != heights[i]:
                number_smaller += 1
            loop_counter += 1
        loop_counter = 0
          
        if number_smaller == i:
            trophy_counter += 1
        number_smaller = 0
                
    print(trophy_counter)