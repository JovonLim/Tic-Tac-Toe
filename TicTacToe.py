import random
from tkinter import NSEW, Label, Button, Checkbutton, Tk, IntVar
import time
import math

class TicTacToe :
  def __init__(self):
    self.buttons = []
    self.board = [" "] * 9
    self.x_wins = 0        
    self.o_wins = 0

  def reset(self) : 
    global current_player
    for button in self.buttons :
      button['text'] = " "
    self.board = [" "] * 9
    current_player = "X"
    info.config(text="It is X's turn")

  def empty_squares(self) :
    return  " " in self.board 

  def available_moves(self) :
    return [i for i, spot in enumerate(self.board) if spot == " "]
  
  def check_win(self, square, letter) : 
    row_ind = math.floor(square / 3) 
    row = self.buttons[row_ind * 3 : (row_ind + 1) * 3]
    if all([spot['text'] ==  letter for spot in row]) :
      return True 

    col_ind = square % 3 
    col = [self.buttons[col_ind + i * 3] for i in range(3)]
    if all([spot['text'] == letter for spot in col]) :
      return True 
    
    if square % 2 == 0 :
      diagonal1 = [self.buttons[i] for i in [0, 4, 8]]
      if all([spot['text'] == letter for spot in diagonal1]) :
        return True 
      diagonal2 = [self.buttons[i] for i in [2, 4, 6]]
      if all([spot['text'] == letter for spot in diagonal2]) :
        return True 
  
    return False
  
  def update_status(self, player, is_win) :
    if is_win :
      info.config(text = f"{player} wins!")
      if player == "X" :
        self.x_wins += 1
      else : 
        self.o_wins += 1
      count.config(text = f'X: {game.x_wins}' +  f'\tO: {game.o_wins}')
    else :
      info.config(text = "It's a draw!")
    
    self.doUpdate(is_reset=True)
    

  def make_move(self, square, player) :
    button = self.buttons[square]
    if button['text'] == " " :
      button.config(text = player, font=("Calibri", 25))
      self.board[square] = player
      if self.check_win(square, player) :
        self.update_status(player, is_win= True)
        return
      elif not self.empty_squares() :
        self.update_status(player, is_win = False)
        return
      global current_player
      current_player = "O" if player == "X" else "X"
      self.is_ai_on(current_player)
      info.config(text= f"It is {current_player}\'s turn")
    else : 
      info.config(text= "Invalid square")
      self.doUpdate(is_reset=False)
      info.config(text = f"It is {player}\'s turn")
    
  def doUpdate(self, is_reset) :
    root.update()
    time.sleep(1)
    if is_reset :
      self.reset()
    
  def is_ai_on(self, player) :
    if ai_on_var.get() == 1 and player == "O" :
      self.make_move(random.choice(self.available_moves()), player)
      

root = Tk()
root.title("Tic-Tac-Toe")
root.resizable(False, False)

game = TicTacToe()
current_player = "X"

welcome = Label(root, text = "Welcome to Tic-Tac-Toe!", font= "Calibri")
welcome.grid(row=0, column=0, columnspan=3)

# Label used to display the current scores
count = Label(root, text = f'X: {game.x_wins}' +  f'\tO: {game.o_wins}', font= "Calibri")
count.grid(row=1, column=0, columnspan=3)

# Label used to give the user information
info = Label(root, text = "It is X's turn", font= "Calibri")
info.grid(row=2, column=0, columnspan=3)

# Create buttons
for square in range(9):
    temp_button = Button(root, text= " ", command=lambda s=square: game.make_move(s, current_player), fg='white', bg='grey')
    temp_button.grid(row=int(square / 3) + 3, column=(square % 3), sticky=NSEW)
    game.buttons.append(temp_button)

# Button for resetting the game
restart_button = Button(root, text = "Restart", command=game.reset, font= "Calibri", fg='white', bg='grey')
restart_button.grid(row=1, column=0)

# Checkbox for turning the AI on/off
ai_on_var = IntVar()
ai_on = Checkbutton(root, text="Turn on AI", variable=ai_on_var, font= "Calibri")
ai_on.grid(row=1, column=2)

root.columnconfigure(0, minsize=200)
root.columnconfigure(1, minsize=200)
root.columnconfigure(2, minsize=200)
root.rowconfigure(3, minsize=200)
root.rowconfigure(4, minsize=200)
root.rowconfigure(5, minsize=200)

# Start the GUI loop
root.mainloop()