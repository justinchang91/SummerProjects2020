class Board:

    def __init__(self):
        self.row_a = [" ", " ", " "]
        self.row_b = [" ", " ", " "]
        self.row_c = [" ", " ", " "]

    def __str__(self):
        dividers = "  -----"
        # Make rows into strings
        string_row_a = ""
        for i in self.row_a:
            string_row_a += i
        string_row_a = "|".join(string_row_a)

        string_row_b = ""
        for i in self.row_b:
            string_row_b += i
        string_row_b = "|".join(string_row_b)

        string_row_c = ""
        for i in self.row_c:
            string_row_c += i
        string_row_c = "|".join(string_row_c)

        return "  0 1 2" + "\n" + "A " + string_row_a + "\n" + dividers + "\n" + "B " + string_row_b + "\n" + \
               dividers + "\n" + "C " + string_row_c

    def place_move(self, choice, symbol):
        """
        Places the move of the player
        :param choice: The move of the player
        :param symbol: The symbol of the player
        :return: None
        """
        if choice[0] == "A":
            print("hi")
            if choice[1] == "0":
                self.row_a[0] = symbol
            elif choice[1] == "1":
                self.row_a[1] = symbol
            elif choice[1] == "2":
                self.row_a[2] = symbol

        elif choice[0] == "B":
            if choice[1] == "0":
                self.row_b[0] = symbol
            elif choice[1] == "1":
                self.row_b[1] = symbol
            elif choice[1] == "2":
                self.row_b[2] = symbol

        elif choice[0] == "C":
            if choice[1] == "0":
                self.row_c[0] = symbol
            elif choice[1] == "1":
                self.row_c[1] = symbol
            elif choice[1] == "2":
                self.row_c[2] = symbol

    def is_won(self, symbol):
        """
        check if the game has been won
        :return: True or False
        """
        # Win in rows
        if self.row_a[0] == symbol and self.row_a[1] == symbol and self.row_a[2] == symbol:
            return True
        elif self.row_b[0] == symbol and self.row_b[1] == symbol and self.row_b[2] == symbol:
            return True
        elif self.row_c[0] == symbol and self.row_c[1] == symbol and self.row_c[2] == symbol:
            return True

        # Win in columns
        elif self.row_a[0] == symbol and self.row_b[0] == symbol and self.row_c[0] == symbol:
            return True
        elif self.row_a[1] == symbol and self.row_b[1] == symbol and self.row_c[1] == symbol:
            return True
        elif self.row_a[2] == symbol and self.row_b[2] == symbol and self.row_c[2] == symbol:
            return True

        # Win in diagonals
        elif self.row_a[0] == symbol and self.row_b[1] == symbol and self.row_c[2] == symbol:
            return True
        elif self.row_a[2] == symbol and self.row_b[1] == symbol and self.row_c[0] == symbol:
            return True
        else:
            return False


def play_game():
    print("Tic Tac Toe")
    print("-------------------------------------------------------------------------------------------------------")
    print("Welcome to Tic Tac Toe! The object of the game is to get three in a row. "
          "You play on a three by three \ngame board. The first player is known as X and the second is O. Players "
          "alternate placing Xs and Os on \nthe game board until either opponent has three in a row. Enter your move by"
          " typing in the row (A, B, C) \nfollowed by the column (0, 1, 2). Ex. A0.")
    print("-------------------------------------------------------------------------------------------------------")

    # Initialize board
    board = Board()

    # Get the player characters
    player1_sym = input("Player 1, enter your symbol (X/O): ")  # Add functionality later if user puts in wrong input
    if player1_sym == "X":
        player2_sym = "O"
    else:
        player2_sym = "X"

    # Run the game
    print(board)
    number_of_moves = 0
    if player1_sym == "X":
        player1_move = input("Player 1, please enter your move: ")
        board.place_move(player1_move, player1_sym)
        number_of_moves += 1
        print(board)

    game_over = False
    while not game_over and number_of_moves < 9:
        # Player 2 move
        player2_move = input("Player 2, please enter your move: ")
        board.place_move(player2_move, player2_sym)
        number_of_moves += 1
        print(board)
        if board.is_won(player2_sym):
            print("Player 2 has won!")
            game_over = True

        # Player 1 move
        if not game_over and number_of_moves < 9:
            user_move = input("Player 1, please enter your move: ")
            board.place_move(user_move, player1_sym)
            number_of_moves += 1
            print(board)
            if board.is_won(player1_sym):
                print("Player 1 has won!")
                game_over = True

        if number_of_moves == 9:
            print("Tie game!")


play_game()

