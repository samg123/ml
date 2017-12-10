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

class tic_tac_toe():

    def __init__(self):

        self.board = np.zeros(9)
        self.save_file = 'game_data.txt'
        self.moves = np.zeros(9)
        self.turn_count = 0

        self.position_map = {1: (0.5,2.5),
                        2: (1.5,2.5),
                        3: (2.5,2.5),
                        4: (0.5,1.5),
                        5: (1.5,1.5),
                        6: (2.5,1.5),
                        7: (0.5,0.5),
                        8: (1.5,0.5),
                        9: (2.5,0.5)}

    def print_board(self):

        if self.turn_count > 1:
            plt.clf()

        x1, y1 = np.linspace(0,3,4), np.linspace(0,3,4)
        x2, y2 = np.ones(4), np.ones(4)
        x3, y3 = np.ones(4)*2, np.ones(4)*2

        plt.plot(x1,y2,'k-')
        plt.plot(x1,y3,'k-')
        plt.plot(x2,y1,'k-')
        plt.plot(x3,y1,'k-')

        for i in self.position_map.keys():
            if self.board[i-1] == 1:
                plt.text(self.position_map[i][0],self.position_map[i][1],'o',fontsize=40)
            elif self.board[i-1] == -1:
                plt.text(self.position_map[i][0],self.position_map[i][1],'x',fontsize=40)

        plt.axis('off')
        plt.show()

    def ask_for_first_move(self):

        choice = input('would you like to go first? (y/n)')

        if choice == 'y':
            factor = 1
        else:
            factor = -1

        self.turn = np.zeros(9)
        for i in range(9):
            self.turn[i] = factor*(-1)**i

    def move(self):

        if self.turn[self.turn_count] == 1:
            choice = int(input('Choose position 1-9'))-1
        else:
             choice = int(input('Choose position 1-9 for the computer'))-1

        if self.board[choice] == 0:
            self.moves[self.turn_count] = choice
            self.board[choice] = self.turn[self.turn_count]
            self.print_board()
            self.turn_count = self.turn_count +  1
        else:
            print('Can\'t go there!')
            self.move()


    def check_winner(self):

        board = self.board.reshape((3,3))
        winner = 0

        for i in range(3):
            if np.sum(board[i,:]) == 3 or np.sum(board[:,i]) == 3:
                winner = 1
            elif np.sum(board[i,:]) == -3 or np.sum(board[:,i]) == -3:
                winner = -1

            if np.sum(np.diag(board)) == 3 or np.sum(np.diag(board[::-1])) == 3:
                winner = 1

            elif np.sum(np.diag(board)) == -3 or np.sum(np.diag(board[::-1])) == -3:
                winner = -1

        return winner


    def play(self):
        self.ask_for_first_move()
        for i in range(9):
            self.move()
            time.sleep(1)
            winner = self.check_winner()
            if np.abs(winner) == 1 and i < 8:
                if winner == 1:
                    print('The user has won!')
                elif winner == -1:
                    print('The computer has won!')
                else:
                    print('It\'s a draw')
                break

game = tic_tac_toe
