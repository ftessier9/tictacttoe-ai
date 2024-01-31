"""
Tic Tac Toe Player
"""

import math
import copy
import collections

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for row in board:
        for tile in row:
            if tile != None:
                count += 1
    if count % 2 == 0:
        return X
    return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    hashset = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                hashset.add((i, j))
    return hashset


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copied_board = copy.deepcopy(board)
    row, col = action
    if copied_board[row][col] is not None:
        raise ValueError
    else:
        copied_board[row][col] = player(copied_board)
    
    return copied_board

def win_condition(winPaths):
    """
    Returns true if there's only one element in the set which mean's there's a winner
    """
    try:
        return "".join(winPaths) if len(winPaths) == 1 else None
    except:
        return None
    

def check_winner(winPaths):
    """
    Check if there's a winner in the col, row or diagonal
    """
    for i in range(3):
        winner = win_condition(winPaths[i])
        if winner:
            return winner
    return None

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    row = collections.defaultdict(set)
    col = collections.defaultdict(set)
    diag = collections.defaultdict(set)

    for i in range(3):
        for j in range(3):
            row[i].add(board[i][j])
            col[j].add(board[i][j])
            if i == j: 
                diag[0].add(board[i][j])
            if i + j == 2:
                diag[1].add(board[i][j])
    return check_winner(row) or check_winner(col) or check_winner(diag)


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    for row in board:
        if None in row:
            return False

    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    def value(board, alpha, beta):
        if terminal(board):
            return utility(board), None

        best_action = None
        if player(board) == "X":
            v = float('-inf')
            for action in actions(board):
                v_new, _ = value(result(board, action), alpha, beta)
                if v_new > v:
                    v = v_new
                    best_action = action
                alpha = max(alpha, v)
                if beta <= alpha:
                    break
        else:
            v = float('inf')
            for action in actions(board):
                v_new, _ = value(result(board, action), alpha, beta)
                if v_new < v:
                    v = v_new
                    best_action = action
                beta = min(beta, v)
                if beta <= alpha:
                    break

        return v, best_action

    value, action = value(board, float('-inf'), float('inf'))
    return action






    

    

