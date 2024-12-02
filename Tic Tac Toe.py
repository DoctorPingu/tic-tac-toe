from Components import intro, display_board, place_marker, player_marker, check_win, check_full_board, replay

def main():
    while True:
        board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        intro()
        player1_marker, player2_marker = player_marker()
        
        if player1_marker == 'X':
            turn = 'Player 1'
        else:
            turn = 'Player 2'
        
        game_on = True
        
        while game_on:
            if turn == 'Player 1':
                display_board(board)
                print("\nIt is Player 1's turn.\n")
                place_marker(board, player1_marker, position=0)
                
                if check_win(board, player1_marker):
                    display_board(board)
                    print("Congratulations! Player 1 has won the game!")
                    game_on = False
                else:
                    if check_full_board(board):
                        display_board(board)
                        print("The game is a tie!")
                        break
                    else:
                        turn = 'Player 2'
                        
            else:
                display_board(board)
                print("\nIt is Player 2's turn.\n")
                place_marker(board, player2_marker, position=0)
                
                if check_win(board, player2_marker):
                    display_board(board)
                    print("Congratulations! Player 2 has won the game!")
                    game_on = False
                else:
                    if check_full_board(board):
                        display_board(board)
                        print("The game is a tie!")
                        break
                    else:
                        turn = 'Player 1'

        if not replay():
            print("Thanks for playing Tic Tac Toe! Goodbye!")
            break

