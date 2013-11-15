#!/usr/bin/env python

import Board
import EightQueen
import unittest


class QueenBoardTestCase(unittest.TestCase):

  def setUp(self):
    self.board = EightQueen.QueenBoard(8)

  def testConstructor(self):
    self.assertEquals(8, self.board.num_rows)
    self.assertEquals(8, self.board.num_cols)
    self.assertEquals(8, self.board.num_queens)
    
  def testcanPlacedOnEmptyBoard(self):
    for row in range(self.board.num_rows):
      for col in range(self.board.num_cols):
        self.assertTrue(self.board.placed(Board.Point(col, row)))

  def testcanPlacedOutOfBounds(self):
    self.assertFalse(self.board.placed(Board.Point(-1, 0)))
    self.assertFalse(self.board.placed(Board.Point(0, -1)))
    self.assertFalse(self.board.placed(Board.Point(8, 6)))
    self.assertFalse(self.board.placed(Board.Point(6, 8)))

  def testcanPlacedOnSpot(self):
    '''
      Places the queen at 'Q' and tests the 'x' points:
       0 1 2 3 4 5 6
    0   | | | | | | | 
    1  x| | | |x| | | 
    2   |x|x|x| | | | 
    3   |x|Q|x| | | | 
    4   |x|x|x| | | | 
    5  x| | | |x| | | 
    6   | | | | | | | 

    '''
    point = Board.Point(2, 3)
    self.assertTrue(self.board.placed(point))
    self.board[point] = "Q"
    print self.board

    # Test the eight points around that one.
    self.assertFalse(self.board.placed(Board.Point(1, 2)))
    self.assertFalse(self.board.placed(Board.Point(1, 3)))
    self.assertFalse(self.board.placed(Board.Point(1, 4)))
    self.assertFalse(self.board.placed(Board.Point(2, 2)))
    self.assertFalse(self.board.placed(Board.Point(2, 4)))
    self.assertFalse(self.board.placed(Board.Point(3, 2)))
    self.assertFalse(self.board.placed(Board.Point(3, 3)))
    self.assertFalse(self.board.placed(Board.Point(3, 4)))

    # Test four diagonal points.
    self.assertFalse(self.board.placed(Board.Point(0, 1)))
    self.assertFalse(self.board.placed(Board.Point(0, 5)))
    self.assertFalse(self.board.placed(Board.Point(4, 1)))
    self.assertFalse(self.board.placed(Board.Point(4, 5)))

    # Remove the queen.
    self.assertFalse(self.board.placed(point))
    self.board[point] = ""
    self.assertTrue(self.board.placed(point))
    self.board[point] = " "
    self.assertTrue(self.board.placed(point))
  
  def testSolver(self):
    self.assertEquals([[]], self.board.placed(point))
    

if __name__ == "__main__":
  unittest.main()
