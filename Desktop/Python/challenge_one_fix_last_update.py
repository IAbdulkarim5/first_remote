import numpy as np

screen_game = np.full([3, 3], " ")

def players():
    while True:
        player_take = input('Choose X or O to play: ').upper()
        if player_take == "X" or player_take == "O":
            return player_take
        else:
            print('Error, please choose X or O, xD can t read ?' )

def print_board(screen_game):
    for row in screen_game:
        print(" | ".join(row))
        print("--" * 5)

def check_winner(screen_game):
    for row in screen_game:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    
    for col in range(3):
        if screen_game[0][col] == screen_game[1][col] == screen_game[2][col] != " ":
            return screen_game[0][col]
    
    if screen_game[0][0] == screen_game[1][1] == screen_game[2][2] != " ":
        return screen_game[0][0]
    
    if screen_game[0][2] == screen_game[1][1] == screen_game[2][0] != " ":
        return screen_game[0][2]
    
    return None

def check_draw(screen_game):
    for row in screen_game:
        if " " in row:
            return False
    return True

player = players()

while True:
    print_board(screen_game)
    print(f"Player {player}'s turn")
    
    while True:
        try:
            row = int(input('Enter row (0, 1, 2): '))
            col = int(input('Enter column (0, 1, 2): '))
            
            if row < 0 or row > 2 or col < 0 or col > 2:
                print('Invalid row or column. Please enter values between 0 and 2.')
                continue
            
            if screen_game[row][col] == " ":
                screen_game[row][col] = player
                break
            else:
                print('The cell is full plz take another one , not plz u need to do that xD .')
        except (ValueError, IndexError):
            print('only steps > , why u put 3 !! ? do u think u r smart ?? (0, 1, 2).')
    
    winner = check_winner(screen_game)
    if winner:
        print_board(screen_game)
        print(f"Player {winner} wins!")
        break
    
    if check_draw(screen_game):
        print_board(screen_game)
        print("It's a draw!")
        break
    
    if player == "X":
        player = "O"
    else:
        player = "X"
