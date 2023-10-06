from tkinter import *
from db import get_puzzle_by_id, update_win_puzzle, get_all_puzzle
import time
from sudokuGame import SudokuGame

MARGIN = 20 
SIDE = 50 
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

def choose_game(gameID):
    game_start(gameID)

def init_list_games():
    puzzles = get_all_puzzle()
    games = [(puzzle[0],puzzle[10], str(f'Game: {puzzle[0]}\nCompleted: {puzzle[10] == 1}\nTime: {puzzle[11]}')) for puzzle in puzzles]

    for game in games:
        button = Button(root, text=game[2], command=lambda gameID=game[0]: choose_game(gameID), width= 19 , font=('Lato', 10), bg="#6A9C89" if game[1] == 0 else "#79AC78",
                        bd=0, fg="white", activebackground="#445D48", activeforeground="white", relief=FLAT)
        button.grid(row=game[0]//3, column=game[0] % 3, padx=10, pady=10)
    
class SudokuUI(Frame):
    def __init__(self, parent, game, gameID, start_time):
        self.game = game
        self.gameID = gameID
        self.start_time = start_time
        Frame.__init__(self, parent)
        self.parent = parent
        
        self.row = -1
        self.col = -1

        self.__initUI()

    def __initUI(self):
        self.parent.title("Sudoku")
        self.pack(fill=BOTH)
        self.canvas = Canvas(self, width=WIDTH, height=HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)
        
        clear_button = Button(self, text="Reset", command=self.__clear_answers, width= 25 , font=('Lato', 10), bg="#6A9C89",
                        bd=0, fg="white", activebackground="#445D48", activeforeground="white", relief=FLAT)
        clear_button.pack(side=LEFT, padx=10, expand=1)

        close_button = Button(self, text='Close', command=self.__close, width= 25 , font=('Lato', 10), bg="#6A9C89",
                        bd=0, fg="white", activebackground="#445D48", activeforeground="white", relief=FLAT)
        close_button.pack(side=RIGHT, padx=10, expand=1)

        self.__draw_grid()
        self.__draw_puzzle()

        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)

    def __draw_grid(self):
        for i in range(10):
            color = "black" if i % 3 == 0 else "gray"
            width=2 if i % 3 == 0 else 1
            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color, width=width)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill = color, width=width)
    
    def __draw_puzzle(self):
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                answer = self.game.puzzle[i][j]
                if answer != 0:
                    x = MARGIN + j * SIDE + SIDE/2
                    y = MARGIN + i * SIDE + SIDE/2
                    original = self.game.start_puzzle[i][j]
                    color = "black" if answer == original else "#952323"
                    self.canvas.create_text(x, y, text=answer, tags="numbers", fill=color, font=('Calibri 16 normal'))

    def __draw_cursor(self):
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = MARGIN + self.col * SIDE + 1
            y0 = MARGIN + self.row * SIDE + 1
            x1 = MARGIN + (self.col + 1) * SIDE -1
            y1 = MARGIN + (self.row + 1) * SIDE - 1
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="#5B9A8B", outline="", tags="cursor",  stipple="gray50")

            self.canvas.delete("highlight")
            for i in range(self.row):
                self.__highlight_cell(i, self.col)
            for i in range(self.row + 1, 9):
                self.__highlight_cell(i, self.col)
            for j in range(self.col):
                self.__highlight_cell(self.row, j)
            for j in range(self.col +1, 9):
                self.__highlight_cell(self.row, j)

   
    def __highlight_cell(self, row, col):
        if row >= 0 and col >= 0:
            x0 = MARGIN + col * SIDE + 1
            y0 = MARGIN + row * SIDE + 1
            x1 = MARGIN + (col + 1) * SIDE -1
            y1 = MARGIN + (row + 1) * SIDE -1

            self.canvas.create_rectangle(x0, y0, x1, y1, fill='#618264', outline="", tags="highlight", stipple="gray12")
    
    def __draw_victory(self, gameID, completed_time):
        x0 = y0 = MARGIN + SIDE *2
        x1 = y1 = MARGIN + SIDE *7
        
        text = f'You win!\nGame {gameID}\nCompleted time:\n{completed_time}'

        self.canvas.create_oval(x0,y0,x1,y1,tags="victory", fill="#A0C49D", outline="")

        x = y = MARGIN + 4 * SIDE + SIDE /2
        self.canvas.create_text(x,y, text=text, tags="victory", fill="white", font=("Calibri", 18), justify=CENTER)
      
    def __cell_clicked(self, event):
        if self.game.game_over:
            return
        
        x = event.x
        y = event.y

        if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
            self.canvas.focus_set()
            
            row = int((y - MARGIN)/SIDE)
            col = int((x - MARGIN)/SIDE)

            if (row == self.row and col == self.col):
                self.row = -1
                self.col = -1
            elif self.game.start_puzzle[row][col] == 0:
                self.row = row
                self.col = col

            self.canvas.delete("highlight")
            for i in range(9):
                for j in range(9):
                    if self.game.puzzle[i][j] == self.game.puzzle[row][col]:
                        self.__highlight_cell(i,j)
        
        self.__draw_cursor()

    def __key_pressed(self, event):
        if self.game.game_over:
            return
        if self.row >= 0 and self.col >= 0 and event.char in "1234567890":
            self.game.puzzle[self.row][self.col] = int(event.char)
            self.col = -1
            self.row = -1

            self.canvas.delete("highlight")

            self.__draw_puzzle()
            self.__draw_cursor()

            if self.game.check_win():
                current_time = time.time()
                complete_time = current_time - self.start_time
                format_time = time.strftime("%H:%M:%S", time.gmtime(complete_time))
                update_win_puzzle(self.gameID, format_time)
                self.__draw_victory(self.gameID, format_time)
    
    def __clear_answers(self):
        self.game.start()
        self.canvas.delete("victory")
        self.__draw_puzzle()

    def __close(self):
        self.parent.destroy()
        init_list_games()

def game_start(gameID):
    board_file = get_puzzle_by_id(gameID)
    game = SudokuGame(board_file)
    game.start()

    game_puzzle = Tk()
    start_time = time.time()
    SudokuUI(game_puzzle, game, gameID, start_time)

    game_puzzle.geometry("%dx%d"%(WIDTH, HEIGHT + 40))
    game_puzzle.mainloop()

if __name__ == '__main__':
    root = Tk()
    root.title('SUDOKU GAME')
    root.geometry('535x550')
    root['background']='#B0D9B1'
    
    init_list_games()

    root.mainloop()
