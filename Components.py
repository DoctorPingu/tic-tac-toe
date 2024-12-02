def intro():
    welcome_message()

    while True:
        user_input = input("Would you like to view the rules? Type either 'yes' or 'no'\nAnswer: ")
        if user_input.lower() == "yes":
            rules()
            break
        elif user_input.lower() == "no":
            break
        else:
            print("Invalid input.")

def welcome_message():
        tic_tac_toe = """
         _______ _        _______           _______ 
        |__   __(_)      |__   __|         |__   __| 
           | |   _  ___     | | __ _  ___     | | ___   ___ 
           | |  | |/ __|    | |/ _` |/ __|    | |/ _ \\ / _ \\
           | |  | | (__     | | (_| | (__     | | (_) |  __/ 
           |_|  |_|\\___|    |_|\\__,_|\\___|    |_|\\___/ \\___| 
        """
        print(f"{tic_tac_toe}\nWelcome to Tic Tac Toe!\n")

def rules():
    print("\n1. The game is played on a grid that's 3 squares by 3 squares (3x3).\n"
          "2. Players take turns putting their marks in empty squares.\n"
          "3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.\n"
          "4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game results in a tie.")

def display_board(board):
    print("\n")
    print("     |     |     ")
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}  ")
    print("     |     |     ")
    print("\n")

def player_marker():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("\nBefore we begin, Player 1 must choose their marker. Pick between 'X' or 'O'. \nAnswer: ")

    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    print(f"\nConfirmed. \nPlayer 1 will be {player1} and Player 2 will be {player2}.\n")
    return (player1, player2)

def place_marker(board, marker, position):
    while True:
        try:
            position = int(input("Where would you like to place your mark on the board? Enter an integer between 1 and 9: "))
            if position not in range(1, 10):
                print("\nInvalid position. Please choose a position between 1 and 9.")
            elif board[position] != ' ':
                print("\nThat position is already taken. Please choose a different position.")
            else:
                board[position] = marker
                break
        except ValueError:
            print("\nInvalid input. Please enter an integer.")

def check_win(board, mark):
    win_combinations = [
        (7, 8, 9), (4, 5, 6), (1, 2, 3),  # Horizontal
        (7, 4, 1), (8, 5, 2), (9, 6, 3),  # Vertical
        (7, 5, 3), (9, 5, 1)]             # Diagonal
    
    
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] == mark:
            return True
    return False

def check_full_board(board):
    return ' ' not in board[1:]

def replay():
    while True:
        choice = input("\nWould you like to play again? Enter 'yes' or 'no': ").lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
