#!/usr/bin/env python

# placeing n queens on n*n chessboard on two queens attack each other
# the solution requires that no two queens share the same row, column, or diagonal
import Board
import unittest

class QueenBoard(Board.Board):

  def __init__(self, num_queens=8):
    super(QueenBoard,self).__init__(
        num_rows=num_queens, num_cols=num_queens, init_char=' ') 
  @property
  def num_queens(self):
    return self.num_rows
  
  def placed(self, point):
    '''
      Determine whetheer the queen can be put on this space
      
      Args: 
        point: row and column position on the chess board
      
      Returns:
        True if a queen can be placed on that position.
    '''
    if not self.valid(point):
      return False
    # whether there are queens in the same row, column and diagonal
    # get all the position for the queens
    for row in range(self.num_rows):
      for col in range(self.num_cols):
        if self[Board.Point(row, col)] != 'Q':
          continue
        if (row == point.row or col == point.col or
            abs((row - point.row) / (col - point.col)) == 1):
          return False
    return True

  def solver(self,n):
    '''
      Solve the n queeen problem
      Looping throught the rows

      Args: 
        n: the number of rows of the board
      Return:
        list of all the solution
    '''
    # if n == 0:
    #   return [[]]
    # prev = self.solver(n-1)
    # solutions = []

    # for sol in prev:
    #   for col in range(self.num_cols):
    #     current = Board.Point(n, col)
    #     if self.placed(current):
    #       solutions.append(sol + [current])

    # return solutions
    
    pass
def main():
  q = QueenBoard(4)
  # pos = Point(2,3)
  print q.solver(4)
  # for qu in q.posQueens:
  #   print qu

if __name__ == "__main__":
  main()
