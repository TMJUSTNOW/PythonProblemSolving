#!/usr/bin/env python

# placeing n queens on n*n chessboard on two queens attack each other
# the solution requires that no two queens share the same row, column, or diagonal
from Board import *

import unittest


class QueenBoard(Board):

  def __init__(self, numQueens=8):
    super(QueenBoard,self).__init__(
        numRows=numQueens, numCols=numQueens, initChar=' ')

  @property
  def numQueens(self):
    return self.numRows

  def canPlaced(self, point):
    '''
      Determine whetheer the queen can be put on this space
      
      Args: 
        point: row and column position on the chess board
      
      Returns:
        True if a queen can be placed on that position.
    '''
    if not self.IsValid(point):
      return False
    # whether there are queens in the same row, column and diagonal
    # get all the position for the queens
    for y in range(self.numRows):
      for x in range(self.numCols):
        if self[Point(x, y)] != 'Q':
          continue
        if (y == point.y or x == point.x or
            abs((y - point.y) / (x - point.x)) == 1):
          return False
    return True

  def Solver(self):
    '''
    
    '''

    pass


def main():
  q = QueenBoard(8)
  pos = Point(2,3)
  q.placeQueen(pos)
  print q
  # for qu in q.posQueens:
  #   print qu

if __name__ == "__main__":
  main()
