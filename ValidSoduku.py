# sudoku:
# Grid 9 * 9, each row and column have the 1-9 numbers occuring only once
# each row, each column, each 3*3 subblock must all the 1-9 but unique numbers 
# The cells which don't have numbers are filled with '.' 
# given a solution of sudoku, check whether it is valid

class Sudoku(object):
  def __init__(self):
    self.board_rows = [['.' for i in range(9)] for j in range(9)]
  
  def isSolved(self):
    '''Check whether the solution is valid sudoku

    for each row, each column, each 3*3 block, they only have 1-9 unique numbers
    with only appear once
    
    Returns:
      True or False whether the solution is valid sudoku
    '''
    validSet = set(['1','2','3','4','5','6','7','8','9'])
    # check all the rows
    for row in self.board_rows:
      if set(row) != validSet:
        return False
    # check all the columns
    for c in range(9):
      # column = [self.board_rows[r][c] for r in range(9)]
      if set([row[c] for row in self.board_rows]) != validSet:
        return False
    # check all the blocks
    # index = [0,3,6]
    for i in range(3):
      for j in range(3):
        block = []
        for plusi in range(3):
          for plusj in range(3):
            block.append(self.board_rows[3 * i + plusi][3 * j + plusj])   
        if set(block) != validSet:
          return False
    return True
