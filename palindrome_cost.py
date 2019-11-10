
"""
Calculating the minimum number of changes required to modify a string into
a palindrome

Author: Oğuzhan Çölkesen
"""

def min_cost_palindrome(string_to_change, o_cost, x_cost):
    """Returns the minimum cost of transforming str into a palindrome

    This function accepts a string consisting of only xs, os and ?s and
    reports the minimum cost of transforming this string into a palindrome
    by replacing every occurrence of a ? with either an x or an o. If the
    input string cannot be transformed into a palindrome, then a value of
    -1 is returned.

    Args:
        string_to_change - string whose transformation cost we're computing
        o_cost - the cost of replacing a ? with an o (an int)
        x_cost - the code of replacing a ? with an x (an int)

    Returns:
        The minimum cost of transforming the input string into a palindrome
        given o_cost and x_cost. If it is not possible to transform s into
        a palindrome, then a value of -1 is returned.
    """
    list_to_change = list(string_to_change)
    first_half = list_to_change[:(len(list_to_change)//2)]
    second_half_reversed = list_to_change[:((len(list_to_change)//2)-1):-1]
    
    min_cost_count = 0
    x_count = 0
    o_count = 0
    exception = False
    
    for i in range(len(first_half)):
        if first_half[i] == "?":
            if second_half_reversed[i] == "x":
                x_count += 1
            elif second_half_reversed[i] == "o":
                o_count += 1
            else:
                min_cost_count += 1
                
        if second_half_reversed[i] == "?":
            if first_half[i] == "x":
                x_count += 1
            elif first_half[i] == "o":
                o_count += 1
            else:
                min_cost_count += 1
        
        if (second_half_reversed[i] == "x" and first_half[i] == "o") or (second_half_reversed[i]
                                                                       == "o"and first_half[i] == "x"):
            exception = True
    
    double_change_cost = min(o_cost, x_cost) * min_cost_count
    total_cost = (x_cost * x_count) + (o_cost * o_count) + double_change_cost
    
    if exception:
        total_cost = -1
        
    return total_cost
    
def main():
    """ Tester function """
    print("Testing min_cost_palindrome")
    print(min_cost_palindrome("oxo?xox?", 3, 5))  # should print 8
    print(min_cost_palindrome("x??x", 9, 4))  # should print 8
    print(min_cost_palindrome("ooooxxxx", 12, 34))  # should print -1
    print(min_cost_palindrome("oxoxooxxxxooxoxo", 7, 4))  # should print 0

if __name__ == "__main__":
    main()