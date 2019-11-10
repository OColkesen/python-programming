
"""
Solving a minesweeper board

Author: Oğuzhan Çölkesen
"""

def pretty_print(board):
    """ Prints a Minesweeper board in a human-friendly format.

    If the input board is None, then no output is produced.

    Parameters:
        board - a list of strings representing the board to be printed.

    Returns:
        None.
    """
    if (board != None):
        for row in board:
            print(row)



def solve_board(board):
    """ Solves the given Minesweeper board.

    Solving a board involves replacing all occurrences of . in the original
    board description with a single digit between 0-8 indicating how many of
    that cell's neighbors contain mines.

    Parameters:
        board - a list of strings describing a Minesweeper board. Each string
                is made up of .s and *s, with the former indicating empty
                cells and the latter indicating mines.

    Returns:
        A list of strings, where each . in one of the original strings has
        been replaced with a digit between 0-8, denoting the number of
        adjacent cells that contain a mine.
    """
    index_manipulations_list = [[1, 1], [1, 0], [1, -1], [0, 1], [0, -1],
                                [-1, 1], [-1, 0], [-1, -1]]
    
    solved_board = [""] * len(board)
    
    for row in range(len(board)):
        for col in range(len(board[0])):
            count = 0
            
            if board[row][col] == ".":
                for index_manip in index_manipulations_list:
                    if (col + index_manip[1] >= 0) and (row + index_manip[0] >= 0):
                    #the if statement prevents to have negative indeces that python
                    #interprets as starting from the opposite side of the list/string
                        try:
                            if board[row + index_manip[0]][col + index_manip[1]] == "*":
                                count += 1
                        except IndexError:
                            count = count
                            
                solved_board[row] += str(count)
            
            else:
                solved_board[row] += "*"
                
    return solved_board


def main():
    """ Tester function. """
    print()
    print("Testing solve_board")
    print()
    solved = solve_board(["..",
                          ".*",
                          ".."])
    pretty_print(solved)
    print()

    solved = solve_board(["*.*.*",
                          "..*..",
                          "*****",
                          ".....",
                          "..**."])
    pretty_print(solved)
    print()


if __name__ == "__main__":
    main()