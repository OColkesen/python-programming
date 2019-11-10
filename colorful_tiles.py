
"""
Calculating the minimum number of tiles to change to make the room as colorful
as possible

Author: Oğuzhan Çölkesen
"""

def min_tiles_to_change(room):
    """
    Returns the minimal number of tiles that need to be changed to make the
    given room as colorful as possible.

    The goal is to achieve a tile configuration where no two adjacent tiles are
    the same color.

    Parameters:
        room - a string containing the colors of the tiles in the room. The i^th
               character of room (one of 'R', 'G', 'B', or 'Y') is the color of
               the i^th tile.

    Returns:
        The minimum number of tiles that need to be changed so that no two
        neighboring tiles are the same color.
    """

    # Since there are 4 colors and a main tile and two adjacent tiles correspond to 3 tiles, specific colors are not important.
    # Instead, all we care about is how many pairs of the same colors are next to each other.
    # Therefore, if we change one of the pairs with a random available color, we will be getting rid of same adjacent colors.
    count = 0
    i = 0
    
    while i < len(room): #I preferred a while loop because I needed to skip the next letter if the two values are the same.
                         #(i.e. index 0 and 1 are equal in "RRRR" so they are one pair. I continue with index 3 to find a new pair.
        if i != len(room)-1: #the conditional is to get rid of the out of range error.
            if room[i] == room[i+1]:
                i += 2
                count += 1
            else:
                i += 1     
        else:
            i += 1
    
    return count
                
def main():
    """ Tester function. """
    print("Testing Colorful Tiles")
    tiles = min_tiles_to_change("RRRRRR")
    print("Test case 1:", tiles)

    tiles = min_tiles_to_change("BBBYYYYYY")
    print("Test case 2:", tiles)

    tiles = min_tiles_to_change("BRYGYBGRYR")
    print("Test case 3:", tiles)

    tiles = min_tiles_to_change("BBBGGRYY")
    print("Test case 4:", tiles)
    print()

if __name__ == "__main__":
    main()