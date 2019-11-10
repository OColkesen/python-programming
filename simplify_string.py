
"""
Simplfying a string with a complex English sentence that misses
"that" statements to make it more understandable

Author: Oğuzhan Çölkesen
"""

def simplify(phrase):
    """Returns a straightforward version of the input phrase.

    For example, 'the cat the dog worried' --> 'the dog that worried the cat'

    Parameters:
        phrase - a string containing a nested phrase.

    Returns:
        A string containing a more straightforward rewrite of the given
        phrase.
    """
    list_phrase = phrase.split()
    
    first_noun = list_phrase[0:2]
    first_verb = list_phrase[-1]
    rest_list_phrase = list_phrase [2:-1]
    
    rest_phrase = phrase[len(first_noun[0] + first_noun[1]) + 2 :
                         (-1 * len(first_verb)) - 1]
    #We calculate the length of the first two words and add 2 for the
    #number of spaces to start from the beginning of the rest of the phrase
    #and end at the beginning of the space before the last word by
    #subtracting the length of the last word by 1.
    
    #This is done because we are dealing with lists and strings concurrently.
    
    if len(rest_phrase) == 0:
        return first_noun[0] + " " + first_noun[1]
    
    return (simplify(rest_phrase) + " that " + first_verb + " " +
            first_noun[0] + " " + first_noun[1])


def main():
    """ Tester function. """
    print("Testing simplify")
    print(simplify("the roach the pirate killed"))
    print(simplify("the rat the cat the dog worried killed"))
    print(simplify("the dog"))
    print(simplify("the rat the cat the dog the boy the girl saw owned " +
                   "chased bit"))

if __name__ == "__main__":
    main()