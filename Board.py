# position for the squre in the chess
class Point(object):

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return 'x: %d, y: %d' % (self.x, self.y)

# create m*n Board with initial character on the board
class Board(object):
  # create board based on num of rows and columns,default is 3*3 
  def __init__(self, numRows=3, numCols=3, initChar='x'):
    self.initChar  = initChar
    self.numRows = numRows 
    self.numCols = numCols
    self._rows = [[initChar for i in range(numCols)] for j in range(numRows)]

  def __getitem__(self, point):
    return self._rows[point.y][point.x]
  
  def __setitem__(self, point, letter):
    self._rows[point.y][point.x] = letter

  def __str__(self):
    '''
      Display the board with borders
    '''
    return 'Board:\n' + '\n'.join(['|'.join(row) for row in self._rows])

  def isEmpty(self, point):
    '''
      Determine whether the space is isEmpty

      Args: 
        point: position for the space on the board with row and column

      Return:
        True if the space in this point is empty 

    '''
    return self._rows[point.y][point.x] == self.initChar

  def IsValid(self, point):
    """Determine whether a point is valid.

    Args:
      point: position for the space on the board with row and column

    Returns:
      True if the position exist in the board
    """
    return (point.x >= 0 and point.x < self.numCols and
            point.y >= 0 and point.y < self.numRows)

