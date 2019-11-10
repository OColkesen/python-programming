
"""
Calculating the average scrabble score of the words in a file

Author: Oğuzhan Çölkesen
"""

def scrabble_score_file(filename):
    """Returns the average Scrabble score of the words in a given file

    This function opens the supplied file and computes the average
    Scrabble score of every word in the file. A "word" is defined to
    be a non-empty sequence of characters that contains no spaces.
    When scoring words, only lower-case letters of the alphabet are
    scored; all other characters receive a score of 0. If the given
    file does not exist or cannot be opened, then a value of -1.0 is
    returned.

    Args:
        filename - a string containing the name of the file to be scored

    Returns:
        The average Scrabble score of all the words in the file
    """
    TILE_SCORES = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
                   "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
                   "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
                   "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
                   "y": 4, "z": 10}
    try:
        with open(filename, "r") as in_file:
            words = []
            for line in in_file:
                line_words = line.split()
                for word in line_words:
                    words.append(word)
    
    except FileNotFoundError:
        print("File not found!")
        return -1.0
    
    word_score_list = []
    
    for i in range(len(words)):
        word_score = 0
        for j in range(len(words[i])):
            if words[i][j] in TILE_SCORES:
                word_score += TILE_SCORES[words[i][j]]
        word_score_list.append(word_score)
    
    total_word_score = 0
    
    for score in word_score_list:
        total_word_score += score
    
    return total_word_score/len(word_score_list)

def main():
    """ Tester function """
    # Testing scrabble_score_file
    print("Testing scrabble_score_file")
    print(scrabble_score_file("hello.txt")) # should print 4.0
    print(scrabble_score_file("one-word.txt")) # should print 5.0
    print(scrabble_score_file("non-existent-file")) # should print -1.0
    print(scrabble_score_file("moby-dick.txt")) # should print 7.4415...

if __name__ == "__main__":
    main()