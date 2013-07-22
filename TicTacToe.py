# given the player, 'x' or 'o', check whether the player is win or not in Tic Tac Toe game
class Board(object):
  def __init__(self):
    self.n = 3
    self.board = [['','',''] for i in range(3)]

  def HasWon(self, player):
    """Whether the given 'player' has won."""
    # check all the items in each row
    for row in self.board:
      if all(item == player for item in row):
        return True
    # check all the items in each column
    for c in range(self.n):
      if all(self.board[r][c] == player for r in range(self.n)):
        return True
    # check the '/'-style diagonal
    if all(self.board[i][i] == player for i in range(self.n)):
      return True
    # check the '\'-style diagonal
    if all(self.board[i][self.n -1 - i] == player for i in range(self.n)):
      return True   

b = Board()
b.board = [['x','x','x'],['x','o','x'],['x','x','o']]
print b.HasWon('x')