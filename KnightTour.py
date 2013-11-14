#!/usr/bin/env python

# A knight's tour is a sequence of moves of a knight on a chessboard
# such that the knight visits every square exactly once. 
# If the knight ends on a square that is one knight's move from the beginning square (so that it could tour the board again 
# immediately, following the same path), the tour is closed, otherwise it is open.

# warnsdorff's rule 
# move the knight to the squere whose next move has fewest onward moves.
from Board import *

import sys
import unittest

VERBOSE = True

# next moves for the knight
MOVES = [{'x':-2, 'y':-1},{'x':-1,'y':-2},{'x':1,'y':-2},{'x':2,'y':-1},
  {'x':2,'y':1},{'x':1,'y':2},{'x':-1,'y':2},{'x':-2,'y':1}]

class KnightsTourBoard(Board):
  def __init__(self, numRows=8, numCols=8):
    super(KnightsTourBoard, self).__init__(
        numRows=numRows, numCols=numCols, initChar=" ")

  # def __str__(self):
  #   return "%d,%d" % (self.row, self.col)

  # check whether the knight can place here if it is not visited before
  def canPlaced(self,point):
    return self[point] != 'K'

  # given the current position for the knight, return the available next moves
  def nextMoves(self,point):
    next_moves = []
    for move in MOVES:
      nextPos = Point(point.row + move['y'], point.col + move['x'])
      # print "%d,%d" % (nextPos.row, nextPos.col)
      print nextPos
      if self.IsValid(nextPos) and self.canPlaced(nextPos):
        next_moves.append(nextPos)
    return next_moves

  #knight tour map for all the moves
  def knightTour(self,path,move):
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
