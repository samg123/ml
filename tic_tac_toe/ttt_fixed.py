import numpy as np
import matplotlib.pyplot as plt
import time

def tic_tac_toe_fixed_ai(board,difficulty=0.5):

    rows = [[0,1,2],[3,4,5],[6,7,8]]
    cols = [[0,3,6],[1,4,7],[2,5,8]]
    diags = [[0,4,8],[2,4,6]]

    corners = [0,2,6,8]
    edges = [1,3,5,7]
    center = 4

    if board == np.zeros(9):
        starting = edges
        if np.random.rand(1) > difficulty:
            choice = np.random.shuffle(np.append(corners,edges))[0]
        else:
            choice = center
    else:
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
            for i in np.random.shuffle(range(9)):
                if board[i] == 1:
                    if i in edges and np.random.rand(1) > difficulty:
                        choice = np.random.shuffle(corners)[0]
                    if i in corners and np.random.rand(1) > difficulty:
                        choice = np.random.shuffle(edges)[0]

            if not choice:
                choice = np.random.shuffle(range(9)[board==0])

    return choice


game = tic_tac_toe
