#!/usr/bin/env python

import Board
import EightQueen
import unittest


class QueenBoardTestCase(unittest.TestCase):

  def setUp(self):
    self.board = EightQueen.QueenBoard(8)

  def testConstructor(self):
    self.assertEquals(8, self.board.numRows)
    self.assertEquals(8, self.board.numCols)
    self.assertEquals(8, self.board.numQueens)

  def testcanPlacedOnEmptyBoard(self):
    for y in range(self.board.numRows):
      for x in range(self.board.numCols):
        self.assertTrue(self.board.canPlaced(Board.Point(x, y)))

  def testcanPlacedOutOfBounds(self):
    self.assertFalse(self.board.canPlaced(Board.Point(-1, 0)))
    self.assertFalse(self.board.canPlaced(Board.Point(0, -1)))
    self.assertFalse(self.board.canPlaced(Board.Point(8, 6)))
    self.assertFalse(self.board.canPlaced(Board.Point(6, 8)))

  def testcanPlacedOnSpot(self):
    '''
      Places the queen at 'Q' and tests the 'x' points:
       | | | | | | | 
      x| | | |x| | | 
       |x|x|x| | | | 
       |x|Q|x| | | | 
       |x|x|x| | | | 
      x| | | |x| | | 
       | | | | | | | 
       | | | | | | | 
    '''
    point = Board.Point(2, 3)
    self.assertTrue(self.board.canPlaced(point))
    self.board[point] = "Q"
    print self.board

    # Test the eight points around that one.
    self.assertFalse(self.board.canPlaced(Board.Point(1, 2)))
    self.assertFalse(self.board.canPlaced(Board.Point(1, 3)))
    self.assertFalse(self.board.canPlaced(Board.Point(1, 4)))
    self.assertFalse(self.board.canPlaced(Board.Point(2, 2)))
    self.assertFalse(self.board.canPlaced(Board.Point(2, 4)))
    self.assertFalse(self.board.canPlaced(Board.Point(3, 2)))
    self.assertFalse(self.board.canPlaced(Board.Point(3, 3)))
    self.assertFalse(self.board.canPlaced(Board.Point(3, 4)))

    # Test four diagonal points.
    self.assertFalse(self.board.canPlaced(Board.Point(0, 1)))
    self.assertFalse(self.board.canPlaced(Board.Point(0, 5)))
    self.assertFalse(self.board.canPlaced(Board.Point(4, 1)))
    self.assertFalse(self.board.canPlaced(Board.Point(4, 5)))

    # Remove the queen.
    self.assertFalse(self.board.canPlaced(point))
    self.board[point] = ""
    self.assertTrue(self.board.canPlaced(point))
    self.board[point] = " "
    self.assertTrue(self.board.canPlaced(point))


if __name__ == "__main__":
  unittest.main()
