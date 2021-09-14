"""
* @Author: Samarth BM.
* @Date: 2021-09-14 10:35  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-14 10:35 
* @Title: :To simulate tic tac toe game where player 1 is computer and player 2 is user.
"""

current_player = 'O'
board = [ " " for x in range(10)]
winner = None
game = True

def create_board():
    """
    Description:
        This function is to create an empty tic tac toe board.
        The board has 3 rows and 3 columns.

    """  
    print("-------------")
    print("|" , board[1] ,  "|" , board[2] , "|" , board[3] , "|")
    print("-------------")
    print("|" , board[4] ,  "|" , board[5] , "|" , board[6] , "|")
    print("-------------")
    print("|" , board[7] ,  "|" , board[8] , "|" , board[9] , "|")
    print("-------------")

def choose_position(player):
    """
    Description:
        This function is to allow the player to choose a position in empty board.

    Args:
        player: Player 1 asked to choose a position.
    """    
    try:
        print("Its your turn now: ", player)
        position = int(input("Choose a position from 1-9 "))
        position != 0

        if " " in board[position]:
            board[position] = player
        else:
            print("This position is occupied, please choose other")

    except Exception as e:
        print("Enter a valid position ", e)
    create_board()

def switch_player():
    """
    Description:
        This function is to switch the players i.e computer and user.

    """    

    global current_player
    if current_player == 'X':
        current_player = 'O'

    elif current_player == 'O':
        current_player = 'X'

def winner_check():
    """
    Description:
        This function is to decide and winner.

    Returns: Winner i.e X or O
        
    """    
    global winner
    global game

    # Checking for row 
    if board[1] == board[2] == board[3] != ' ': 
        game=False
        return board[1]
    elif board[4] == board[5] == board[6] != ' ': 
        game=False
        return board[4]
    elif board[7] == board[8] == board[9] != ' ':
        game=False
        return board[7]

    # Checking for column
    elif board[1] == board[4] == board[7] != ' ': 
        game=False
        return board[1]
    elif board[2] == board[5] == board[8] != ' ': 
        game=False
        return board[2]
    elif board[3] == board[6] == board[9] != ' ': 
        game=False
        return board[3]

    # Checking for diagonal
    elif board[1] == board[5] == board[9] != ' ':
        game=False
        return board[1]
    elif board[3] == board[5] == board[7] != ' ': 
        game=False
        return board[3]
    return False

def draw_check():
    """
    Description:
        This function is used to check for draw condition.

    Returns: True if are no empty space in board .
    
    """    
    global game

    if " " not in board:
        game = False
        return True
    else:
        return None 

def print_winner():
    """
    Description:
        This function is to print the winners i.e X or O.
        If neither of is winner then its a draw.

    """    
    global game
    winner = winner_check()

    if winner == 'X' or winner == 'O':
        game = False
        print("Winner for this game is: ",winner)

    elif winner == None:
        print("OOPS!! Its a draw")


if __name__ == "__main__":
    create_board()

    while game:
        choose_position(current_player)
        winner_check()
        switch_player()
        print_winner()
        draw_check()








