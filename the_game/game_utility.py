import random


def check_winner(board):
    """
    takes a player and the board then it will check the winning conditions 
    and the reverse of those since we are checking both sides 
    it will return 
    0 - means still no winner so keep the game going 
    1 -  player one won stop the game and set it as complete
    2 -  player two won stop the game and set it as complete
    3 -  Tie if board is full
    TODO  check for Tie  return 3
    """
    coulmn_count = 7
    row_count = 7
    reversed_board = []
    merged_board = []
    for row in board:
        row = list(reversed(row))
        reversed_board.append(row)
    # horizontal check
    for r in range (row_count):
        for c in range(coulmn_count-3):
            if board[r][c] == 1 and board[r][c+1] == 1 and board[r][c+2] == 1 and board[r][c+3] == 1:
                return 1
            elif reversed_board[r][c] == 1 and reversed_board[r][c+1] == 1 and reversed_board[r][c+2] == 1 and reversed_board[r][c+3] == 1:
                return 1
            elif board[r][c] == 2 and board[r][c+1] == 2 and board[r][c+2] == 2 and board[r][c+3] == 2:
                return 2
            elif reversed_board[r][c] == 2 and reversed_board[r][c+1] == 2 and reversed_board[r][c+2] == 2 and reversed_board[r][c+3] == 2:
                return 2
    # vertical check
    for r in range (row_count-3):
        for c in range(coulmn_count):
            if board[r][c] == 1 and board[r+1][c] == 1 and board[r+2][c] == 1 and board[r+3][c] == 1:
                return 1
            elif reversed_board[r][c] == 1 and reversed_board[r+1][c] == 1 and reversed_board[r+2][c] == 1 and reversed_board[r+3][c] == 1:
                return 1
            elif board[r][c] == 2 and board[r+1][c] == 2 and board[r+2][c] == 2 and board[r+3][c] == 2:
                return 2
            elif reversed_board[r][c] == 2 and reversed_board[r+1][c] == 2 and reversed_board[r+2][c] == 2 and reversed_board[r+3][c] == 2:
                return 2
    # diagonal / check
    for r in range (row_count-3):
        for c in range(coulmn_count-3):
            if board[r][c] == 1 and board[r+1][c+1] == 1 and board[r+2][c+2] == 1 and board[r+3][c+3] == 1:
                return 1
            elif reversed_board[r][c] == 1 and reversed_board[r+1][c+1] == 1 and reversed_board[r+2][c+2] == 1 and reversed_board[r+3][c+3] == 1:
                return 1
            elif board[r][c] == 2 and board[r+1][c+1] == 2 and board[r+2][c+2] == 2 and board[r+3][c+3] == 2:
                return 2
            elif reversed_board[r][c] == 2 and reversed_board[r+1][c+1] == 2 and reversed_board[r+2][c+2] == 2 and reversed_board[r+3][c+3] == 2:
                return 2
    # diagonal \ check
    for r in range (2,row_count):
        for c in range(coulmn_count-3):
            if board[r][c] == 1 and board[r-1][c+1] == 1 and board[r-2][c+2] == 1 and board[r-3][c+3] == 1:
                return 1
            elif reversed_board[r][c] == 1 and reversed_board[r-1][c+1] == 1 and reversed_board[r-2][c+2] == 1 and reversed_board[r-3][c+3] == 1:
                return 1
            elif board[r][c] == 2 and board[r-1][c+1] == 2 and board[r-2][c+2] == 2 and board[r-3][c+3] == 2:
                return 2
            elif reversed_board[r][c] == 2 and reversed_board[r-1][c+1] == 2 and reversed_board[r-2][c+2] == 2 and reversed_board[r-3][c+3] == 2:
                return 2
    # check for tie
    for l in board:
        merged_board += l
    for cell in merged_board:
        if cell == 0:
            return 0
    return 3


def is_turn(game, player):
    '''
    determines if it is the player's turn or not
    input: normal connect 4 board defined above, player -> 1 or 2
    output: true if it is the players turn
    since we always start with player_1 so depending on the number or peicecs 
    starts at 0 if the number is even that means its player_1's turn if its odd then its player_2's turn
    '''
    if game.game_complete:
        return False
    board = game.game_state
    number_of_pieces_on_board = 0
    for col in board:
        for piece in col:
            if not piece == 0:
                number_of_pieces_on_board += 1
            else:
                pass
    return number_of_pieces_on_board % 2 == player - 1 # returns boolean



def bot_move(game,player):
    player = player
    sides = ['Right','Left']
    while True:
        row = random.randint(0, 6)
        side = random.choice(sides)
        if game.try_move(player,row,side):
            return True
        
        
    