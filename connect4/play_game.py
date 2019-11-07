def play_game(self, x_player, o_player):
    """Modified wrapper method that manages a game of Connect-4 between two
    players, each of whom can either be an AI or a human

    This is a modified version of the host_game method that allows for
    one or both of the players to be AI agents (i.e., instances of the
    Player class). When an AI agent is chosen, then that agent's next_move
    method is used to generate moves for that player. When a human player
    is chosen, the terminal is used to solicit moves. To set a certain
    player to be an AI player, pass in a Player instance for that
    parameter; to make a player a human, pass in the string 'human' for
    that parameter.

    Args:
        x_player, o_player - the type of the 'X'/'O' player (either a Player
                             object or the string 'human')

    Returns:
        Nothing
    """
    current_side = "X"
    players = {"X": x_player, "O": o_player}
    while ((not self.win_for("X")) and
           (not self.win_for("O")) and
           (not self.is_full())):
        print()
        print(self)
        print()
        move = Board.INVALID_MOVE
        while not self.allows_move(move):
            if players[current_side] == "human":
                move = int(input(current_side + "'s move: "))
            else:
                move = players[current_side].next_move(self)
                print("Computer playing for " + current_side +
                      " plays at " + str(move))

        self.add_move(move, current_side)
        if current_side == "X":
            current_side = "O"
        else:
            current_side = "X"

    if self.win_for("X"):
        print("X wins --- congratulations!\n")
    elif self.win_for("O"):
        print("O wins --- congratulations!\n")
    else:
        print("Tied game!\n")

    print()
    print(self)
