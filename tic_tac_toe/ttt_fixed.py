import numpy as np
import matplotlib.pyplot as plt
import time

def tic_tac_toe_fixed_ai(board):

    rows = [[0,1,2],[3,4,5],[6,7,8]]
    cols = [[0,3,6],[1,4,7],[2,5,8]]
    diags = [[0,4,8],[2,4,6]]

    if board == np.zeros(9):
        starting = [1,3,5,7]
        for i in range(4):
            if np.random.rand(1) > 0.5:
                choice = starting[i]
            if np.random.rand(1) > difficulty:
                choice = choice + 1

    for i in range(3):
        if np.abs(np.sum(board[rows[i]])) == 2:
            choice = rows[i][board[rows[i]]==0]
            break

        elif np.abs(np.sum(board[cols[i]])) == 2:
            choice = rows[i][board[cols[i]]==0]
            break

        elif i < 3 and np.abs(np.sum(board[diags[i]])) == 2:
            choice = rows[i][board[cols[i]]==0]
            break

    if not choice:
        a = np.random.shuffle([1,2,3,4,5,6,7,8,9])

        for i in range(9):
            if board[a[i]] == 1:







                
