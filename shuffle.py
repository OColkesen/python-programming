
"""
Shuffling a list

Author: Oğuzhan Çölkesen
"""

def shuffle():
    """
    Performs a perfect shuffle of a user-supplied list.
    """
    deck = eval(input("Enter list: "))

    deck_left_half = deck[:(len(deck)//2)]
    deck_right_half = deck[(len(deck)//2):]
    deck_shuffled = []
    
    for i in range(len(deck_right_half)):
        deck_shuffled.append(deck_left_half[i])
        deck_shuffled.append(deck_right_half[i])
        
    print (deck_shuffled)