import random
# Game board values. Values are what appears on screen, and options_left are the integer forms used for later functions
values = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
options_left = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def game_board():
    """Creates the board on screen, using the values variable to determine what should be placed on screen"""
    vertical_lines = "   |   |   "
    horizontal_lines = "___________"
    print(vertical_lines)
    print(f" {values[0]} | {values[1]} | {values[2]}")
    print(vertical_lines)
    print(horizontal_lines)
    print(vertical_lines)
    print(f" {values[3]} | {values[4]} | {values[5]}")
    print(vertical_lines)
    print(horizontal_lines)
    print(vertical_lines)
    print(f" {values[6]} | {values[7]} | {values[8]}")
    print(vertical_lines)


def move(player, symbol):
    """If a human player, the program will require an input from the user and check if it's a valid choice
    Otherwise, if the computer player is playing, it will automatically pick from options_left"""
    if player == "human":
        user_input = input("Choose which square you would like to place your mark: ")
        if not user_input.isdigit() or int(user_input) < 1 or int(user_input) > 9:
            print("Invalid Entry! Try again")
        elif values[int(user_input) - 1] == "X" or values[int(user_input) - 1] == "O":
            print("That square is already occupied! Please select another")
        else:
            update_scoreboard(position=user_input, symbol=symbol)
    if player == "computer":
        computer_choice = random.choice(options_left)
        update_scoreboard(position=computer_choice, symbol=symbol)


def update_scoreboard(position, symbol):
    """Updates the values list with either an X or O at the correct position, and removes that from options_left"""
    values[int(position) - 1] = symbol
    options_left.remove(int(position))
    game_board()


def has_won():
    """Checks to see if a winning combination is on screen. If there is, True is returned"""
    winning_combo_found = False
    winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combo in winning_combos:
        items = [values[num] for num in combo]
        if items == ["X", "X", "X"] or items == ["O", "O", "O"]:
            winning_combo_found = True
    return winning_combo_found


def keep_playing():
    """Checks to see if the user wants to continue playing. If so, values, options_left, and is_choosing
    get set back to their initial values. Otherwise, is_playing gets switched to False, ending the program"""
    global is_playing, values, options_left, is_choosing
    user_wants = input("Would you like to play again? Type 'y' to keep playing, anything else to exit ")
    if user_wants.lower() != "y":
        print("Goodbye!")
        is_playing = False
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    options_left = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    is_choosing = True


def is_draw():
    """Returns True when there are no winning combinations left after the board is filled"""
    if not options_left:
        return True


def winning_dialogue(player):
    """Prints the correct dialogue depending on if the user or computer has won. """
    if player == "human":
        print("You win!")
    else:
        print("Computer Wins!")


player1 = ""
player2 = ""
is_playing = True
is_choosing = True

print("Welcome to Tic Tac Toe!")
user_options = ["1", "2"]
while is_playing:
    while is_choosing:
        player_order = input("Would you like to go first or second? Type '1' to go first, or '2' to go second: ")
        if player_order not in user_options:
            print("Invalid Entry! Try again")
        else:
            if player_order == "1":
                player1 = "human"
                player2 = "computer"
            elif player_order == "2":
                player1 = "computer"
                player2 = "human"
            is_choosing = False
    game_board()
    move(player=player1, symbol="X")
    if has_won():
        game_board()
        winning_dialogue(player1)
        keep_playing()
    elif is_draw():
        game_board()
        print("It's a draw!")
        keep_playing()
    else:
        move(player=player2, symbol="O")
        if has_won():
            game_board()
            winning_dialogue(player2)
            keep_playing()
