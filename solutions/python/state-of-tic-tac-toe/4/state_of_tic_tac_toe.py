'''Tic-tac-toe game state checker.'''

def check_win(board, who):
    '''Return True if the player has three in a row, column, or diagonal.'''
    if all(board[index][index] == who for index in range(3)):
        return True
    if all(board[index][2-index] == who for index in range(3)):
        return True 

    if any(row == who * 3 for row in board):
        return True

    if any(all(board[row][column] == who for row in range(3)) for column in range(3)):
        return True
    return False


def gamestate(board):
    '''Return game state: 'win', 'draw', or 'ongoing'.    
    Raise ValueError if board violates game rules (wrong turn order, continued after win).'''
    
    board = [row.upper() for row in board]
    all_x = sum(row.count('X') for row in board)
    all_o = sum(row.count('O') for row in board)
    if all_o > all_x:
        raise ValueError('Wrong turn order: O started')
    if all_x > all_o +1:
        raise ValueError('Wrong turn order: X went twice')
    x_wins = check_win(board, 'X')
    o_wins = check_win(board, 'O')

    if x_wins and all_x == all_o:
        raise ValueError('Impossible board: game should have ended after the game was won')
    
    if o_wins and all_x == all_o + 1: 
        raise ValueError('Impossible board: game should have ended after the game was won')
    
    if x_wins or o_wins:
        return 'win'
    if all_x + all_o == 9:
        return 'draw'   
    return 'ongoing'