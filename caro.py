import tkinter as tk
from tkinter import messagebox
size = 25
class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        # self.window.resizable(0, 0)
        self.board = [['' for _ in range(size)] for _ in range(size)]
        self.player_turn = 'X'

        self.buttons = [[tk.Button(self.window, text='', command=lambda row=i, col=j: self.click(row, col), height=1, width=3, 
            font=('Helvetica', '20'), bg='white') for j in range(size)] for i in range(size)]
        for i in range(size):
            for j in range(size):
                self.buttons[i][j].grid(row=i, column=j)

    def click(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.player_turn
            self.buttons[row][col]['text'] = self.player_turn

            if self.player_turn == 'X':
                self.buttons[row][col]['fg'] = 'red' 
            else:
                self.buttons[row][col]['fg'] = 'blue' 

            # self.buttons[row][col]['disabledforeground'] = 'black'
            self.buttons[row][col]['bg'] = 'lightgrey'
            self.player_turn = 'O' if self.player_turn == 'X' else 'X'

        winner = self.check_winner(row, col)
        if winner is not None:
            messagebox.showinfo("Game Over", f"'{winner}' has won!")
            self.window.destroy()
    def check_winner(self, row, col):
        #check_Row
        cntRow = cntCol = 1
        cA = cB = cC = cD = True
        if self.board[row][col] == '':
            return None 
        for i in range(1, 5):
            if cntRow == 5 or cntCol == 5 : return self.board[row][col]
            if cA : rA = row - i
            if cB : rB = row + i
            if cC : colC = col - i
            if cD : colD = col + i
            if rB > len(self.board) -1: cB = False
            if rA < 0 : cA = False
            if colD > len(self.board) -1: cD = False
            if colC < 0 : cC = False
            #Row
            if cA :
                if self.board[rA][col] == self.board[row][col] : cntRow += 1
                else : cA = False
            if cB :
                if self.board[rB][col] == self.board[row][col] : cntRow += 1
                else : cB = False
            #Col
            if cC :
                if self.board[row][colC] == self.board[row][col] : cntCol += 1
                else : cC = False
            if cD :
                if self.board[row][colD] == self.board[row][col] : cntCol += 1
                else : cD = False
            if cntRow == 5 or cntCol == 5 : return self.board[row][col]
        #check duong cheo phai
        cntRight = 1
        cntLeft= 1
        RightARow = True
        RightACol = True
        RightBRow = True
        RightBCol = True
        for i in range(1,5) :
            if cntRight == 5: return self.board[row][col]
            if RightARow : rAIdx = row - i
            if rAIdx < 0 : RightARow = False
            if RightACol : cAIdx = col + i 
            if cAIdx > len(self.board) - 1 : RightACol = False

            if RightBRow : rBIdx = row + i
            if RightBCol : cBIdx = col - i
            if cBIdx < 0 : RightBCol = False
            if rBIdx > len(self.board) - 1: RightBRow = False

            if RightACol and RightARow:
                if(self.board[rAIdx][cAIdx] == self.board[row][col]) : cntRight+=1
                else : 
                    RightACol = False
                    RightARow = False
            if RightBCol and RightBRow:
                if(self.board[rBIdx][cBIdx] == self.board[row][col]) : cntRight+=1
                else:
                    RightBCol = False
                    RightBRow = False

            if cntRight == 5: return self.board[row][col]
        #Check duong cheo trai
        LeftARow = True
        LeftACol = True
        LeftBRow = True
        LeftBCol = True
        for i in range(1,5) :
            if cntLeft == 5 : return self.board[row][col]
            if LeftARow : rAIdx = row - i
            if rAIdx < 0 : LeftARow = False
            if LeftACol : cAIdx = col - i 
            if cAIdx < 0 : LeftACol = False

            if LeftBRow : rBIdx = row + i
            if LeftBCol : cBIdx = col + i
            if cBIdx > len(self.board) - 1 : LeftBCol = False
            if rBIdx > len(self.board) - 1: LeftBRow = False

            if LeftACol and LeftARow:
                if(self.board[rAIdx][cAIdx] == self.board[row][col]) : cntLeft+=1
                else : 
                    LeftACol = False
                    LeftARow = False
            if LeftBCol and LeftBRow:
                if(self.board[rBIdx][cBIdx] == self.board[row][col]) : cntLeft+=1
                else:
                    LeftBCol = False
                    LeftBRow = False
            if cntLeft == 5 : return self.board[row][col]
    def run(self):
        self.window.mainloop()
if __name__ == "__main__":
    game = TicTacToe()
    game.run()