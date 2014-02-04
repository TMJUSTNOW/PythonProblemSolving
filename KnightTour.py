#!/usr/bin/env python

'''
A knight's tour is a sequence of moves of a knight on a chessboard
such that the knight visits every square exactly once. 
If the knight ends on a square that is one knight's move 
from the beginning square (so that it could tour the board again 
immediately, following the same path), the tour is closed, otherwise it is open.

warnsdorff's rule 
move the knight to the squere whose next move has fewest onward moves.
'''
from Board import *
import sys
import unittest

VERBOSE = True

# next moves for the knight
MOVES = [{'x':-2, 'y':-1},{'x':-1,'y':-2},{'x':1,'y':-2},{'x':2,'y':-1},
  {'x':2,'y':1},{'x':1,'y':2},{'x':-1,'y':2},{'x':-2,'y':1}]

class KnightsTourBoard(Board):
  '''
    create board for knight tour including the rule for solving knight tour game
  '''
  def __init__(self, num_rows=8, num_cols=8):
    super(KnightsTourBoard, self).__init__(
        num_rows=num_rows, num_cols=num_cols, init_char=" ")

  def canPlaced(self,point):
    '''
    check whether the knight can place here if it is not visited before
    '''
    return self[point] != 'K'

  def nextMoves(self,point):
    '''
      given the current position for the knight, return the available next moves
    '''
    next_moves = []
    for move in MOVES:
      nextPos = Point(point.row + move['y'], point.col + move['x'])
      # print "%d,%d" % (nextPos.row, nextPos.col)
      print nextPos
      if self.isValid(nextPos) and self.canPlaced(nextPos):
        next_moves.append(nextPos)
    return next_moves

  def knightTour(self,path,move):
    '''
      Determine whether there is a path for the knight to traverse the board

      Args:
        path: valid moves for the knight
        move: the current move

      Return: 
        True if there is a solution for the knight
    '''
    if VERBOSE:
      print self
    maxSteps = self.numRows * self.numCols
    # Check if we're done and return True.
    if all([all(c == "K" for c in row) for row in self._rows]):
      return True
    if VERBOSE:
      print "I'm at: %s" % move
    # Calculate the next moves.
    nexts = self.nextMoves(move)
    if VERBOSE:
      print "nexts: %s" % ["%s" % m for m in nexts]
    if not nexts:
      return False
   
    # Order moves by most-restrictive first.
    for next in sorted(nexts, key=lambda x: len(self.nextMoves(x))):
      path.append(next)
      # mark the position that knight visited
      self[next] = 'K'
      if self.knightTour(path, next):
        return True
      else:
        if VERBOSE:
          print "Backtracking!"
        self[next] = 'x'
        path.pop()

    return False

# print the kight path
# Args: path which consist of all Point instance
def printPath(path):
  print "%s" % ", ".join([str(p) for p in path])
    
def main():
  # number of rows and columns for the board
  # initiate the board
  B = KnightsTourBoard(6, 6)
  # knight path
  path = []
  # starting position for the knight
  start = Point(2, 2)
  B[start] = "K"

  if not B.knightTour(path,start):
    print "solution doesn't exist"
  else: 
    printPath(path)

main()
