"""
Implementation of a Connect-4 Player class

Author: Camden Bertucci and Oğuzhan Çölkesen
Time spent: 5 hours
"""

from random import choice

class Player:
    
    def __init__(self, side, ply, is_random):
        """
        Constructs a Player object of the specified side (e.g. "X" or "O"),
        ply (i.e. how many moves does it look ahead), and is_random
        (i.e. breaks ties randomly or deterministically) attributes.

        Parameters:
            side - a string, which defines the side of the player in the
                   Connect 4 game. ("X" or "O")
            ply - an integer, which sets how many moves ahead that the
                  player evaluates before making a move
            is_random - a boolean variable, which designates if the player
                        breaks ties between moves randomly or deterministically
                        by picking the first column. (True = randomly, False =
                        deterministically)
        
        Returns:
            None.
        """
        self.side = side
        self.ply = ply
        self.is_random = is_random
        
    def __str__(self):
        """
        Generates and returns a string representation of this board object

        Returns:
            A string containing an ASCII representation of the player objects's
            features, such as its side, ply level, and how it breaks ties.
        """
        if self.is_random == True:
            return ("Player for " + self.side + ", ply = " + str(self.ply) +
                ", breaks ties randomly")
        
        return ("Player for " + self.side + ", ply = " + str(self.ply) +
                ", breaks ties deterministically")
    
    def opponent(self):
        """
        This method returns the string representation of the opposite side
        to the player object.

        Returns:
            A string containing the representation of the opposite side to
            the player object. If the player's side is "X", the function
            returns "O" and vice versa.
        """
        if self.side == "X":
            return "O"
        
        return "X"
    
    def evaluate_board(self, board):
        """
        This method takes in an object of Board class and returns an integer,
        depending on the current status of the game on the Connect 4 Board.
        The method returns whether the current board position represents a
        win, a loss, or a tie for the player's side.

        A player wins by getting four-of-a-kind of their own peg type in a
        row. This can happen either horizontally, vertically or diagonally.
        This method checks whether any of these conditions has been met for
        the player or its opponent.

        Parameters:
            board - a Board class objects, which represents a Connect 4
                    board whose current status is being tested.

        Returns:
            An integer value. If the player wins in the current position of
            the board, the method returns 100. If it's a loss for the player,
            the method returns 0. If neither is true (i.e. there is a tie in
            the current position of the board), the method returns 50.
        """
        WIN = 100
        LOSS = 0
        TIE = 50
        
        if board.win_for(self.side):
            return WIN
        
        elif board.win_for(self.opponent()):
            return LOSS
        
        return TIE
    
    def score_columns(self, board):
        """
        This method takes in an object of Board class and recursively places
        a tentative piece on the board to use the evaluate_board method,
        so that the scores for every possible move are calculated and returned
        in a list. The AI plays on the board object to evaluate the scores of
        the moves by creating another Player object belonging to the opposite
        side. The method is run recursively with respect to the "ply"
        parameter of the player, which means that the AI evaluates "ply"
        moves ahead of the current position of the board.
        
        The method implements a Minimax algorithm.

        Parameters:
            board - a Board class objects, which represents a Connect 4
                    board whose current status is used to determine
                    the scores of the possible moves.

        Returns:
            A list, which contains the scores of every possible move on the
            current board object for the player.
        """
        WIN = 100
        LOSS = 0
        TIE = 50
        FULL = -1
        
        scores = [TIE] * board.width
        
        for col in range(len(scores)):
            
            if self.evaluate_board(board) == WIN:
                scores[col] = WIN
            #Base case: if player wins in the current situation, we don't want
            #to continue recursion. Thus, we set every element in scores to WIN.
            
            elif self.evaluate_board(board) == LOSS:
                scores[col] =  LOSS
            #Base case: if player loses in the current situation, we don't want
            #to continue recursion. Thus, we set every element in scores to LOSS.
            
            elif not board.allows_move(col):
                scores[col] = FULL
            #Base case: if the current column is full, we don't want to continue
            #recursion. Thus, we set the score of this column to FULL, which is
            #lower than every other possible score.  
                
            elif self.ply == 0:
                scores[col] =  TIE
            #Base case: if the player object looks 0 moves ahead, every move
            #has the same value for the player. Thus, we set every columns
            #score to TIE.
                
            else:
                board.add_move(col, self.side)
                recursive_ply = self.ply - 1
                
                #creating a new player object
                opponent = Player(self.opponent(), recursive_ply, self.is_random)
                
                #recursive statement
                opponent_scores = opponent.score_columns(board)
                
                scores[col] = WIN - max(opponent_scores)
                #maximum of opponent scores is subtracted, because we want to
                #consider the best case for the opponent to assign the current
                #player's scores.
                
                board.delete_move(col)
                #the added move is deleted so the board returns back to
                #its original position.
        
        return scores
    
    def best_move(self, scores):
        """
        This method calculates and returns the index position of the largest
        element in an integer list. Depending on the "is_random" attribute
        of the Player object, the method breaks ties either randomly or
        deterministically by choosing the smalles index position among the
        tied indeces.
        
        Parameters:
            scores - a list, which contains integers. This list is going to be
                     used to find the index of the largest element in it.

        Returns:
            An integer, which represents the index of the largest element in
            the scores list. If there is a tie and "is_random" is True,
            the method returns one of the indeces randomly, and if "is_random"
            is False, it returns the smalles index among the tied indeces.
        """
        maximum_value = max(scores)
        random_index_list = []
        
        if self.is_random:
            for i in range(len(scores)):
                if scores[i] == maximum_value:
                    random_index_list.append(i)
            
            return choice(random_index_list)
        
        else:
            for i in range(len(scores)):
                if scores[i] == maximum_value:
                    return i
    
    def next_move(self, board):
        """
        This method is basically a wrapper method, which merges the
        score_columns and best_move methods. It uses a board object
        to get a scores list with respect to the current position on the
        board and possible moves. Then, it uses that scores list to
        return the index (i.e. column number) of the best move using the
        best_move method.

        Parameters:
            board - a Board class objects, which represents a Connect 4
                    board whose current status is used to determine
                    the scores of the possible moves.

        Returns:
            An integer, which is the best move for the Player to play
            under the current conditions of the board object.
        """
        scores_list = self.score_columns(board)
        
        return self.best_move(scores_list)