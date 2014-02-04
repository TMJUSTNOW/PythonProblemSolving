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
            abs(row - point.row) == abs(col - point.col)):
          return False
    return True

  def solver(self, col=0, solutions=None):
    '''
      Solve the n queeen problem
      Looping throught the rows

      Args: 
        col: Which column we are looking to place a queen in.
        solutions: An optional array to collect solutions in.
          If not given, only the first solution will be returned.
          If given, all solutions will be put into this array.

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
    if col == self.num_rows:
      print "Solved!"
      if solutions is not None:
        solutions.append(str(self))
        return False
      else:
        print self
        return True
    for row in range(self.num_rows):
      current = Board.Point(row, col)
      if self.placed(current):
        self[current] = 'Q'
        if self.solver(col=col + 1, solutions=solutions):
          return True
        else:
          self[current] = ' '
    return False

    
def main():
  q = QueenBoard(8)
  # pos = Point(2,3)
  solutions = []
  print q.solver(solutions=solutions)
  print "Got %d solutions:" % len(solutions)
  for solution in solutions:
    print solution
  # for qu in q.posQueens:
  #   print qu

if __name__ == "__main__":
  main()
