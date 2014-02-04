'''
  Base class Board for creating all the board applications 
'''
class Point(object):
  '''
    Position for the square on the board with row and column
  '''
  def __init__(self, row, col):
    self.row = row
    self.col = col

  def __str__(self):
    return 'row: %d, col: %d' % (self.row, self.col)

class Board(object):
  '''
    Create Board with initial character
  '''
  def __init__(self, num_rows=3, num_cols=3, init_char='x'):
    self.init_char  = init_char
    self.num_rows = num_rows
    self.num_cols = num_cols
    self._rows = [[init_char for i in range(num_cols)] for j in range(num_rows)]

  def __getitem__(self, point):
    return self._rows[point.row][point.col]

  def get_by_pos(self,row,col):
    return self._rows[row][col]

  def set_by_pos(self,row,col,letter):
    self._rows[row][col] = letter

  def __setitem__(self, point, letter):
    self._rows[point.row][point.col] = letter

  def get_num_rows(self):
    return self.num_rows
  def get_num_cols(self):
    return self.num_cols

  def __str__(self):
    '''
      Display the board with borders
    '''
    return 'Board:\n' + '\n'.join(['[' + '|'.join(row) + ']' for row in self._rows])

  def empty(self, point):
    '''
      Determine whether the space is isEmpty

      Args: 
        point: position for the space on the board with row and column

      Return:
        True if the space in this point is empty
    '''

    return self._rows[point.row][point.col] == self.init_char

  def valid(self, point):
    '''Determine whether a point is valid.

    Args:
      point: position for the space on the board with row and column

    Returns:
      True if the position exist in the board
    '''
    
    return (point.row >= 0 and point.row < self.num_rows and
            point.col >= 0 and point.col < self.num_cols)