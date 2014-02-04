'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region .

For example,
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

'''

'''
recursive 

'''
from Board import Board
from Board import Point

def is_o(board, i, j):
  """Checks whether this position has an 'O'."""
  return (i < board.get_num_rows() - 1 and j < board.get_num_cols() -1 and
          board.get_by_pos(i,j) == 'O')

def is_region_x_surrounded(board, i, j, region):
  """Determines whether the region is surrounded by 'X's.

  Args:
    board: The board to check.
    i: The row index to examine.
    j: The column index to examine.
    region: A list of row-column tuples that have 'O's in them.

  Returns:
    Whether the region is surrounded by 'X's or not, and adds all 
    'O' positions to 'region'.
  """
  # Implement.
  if (i, j) in region:
    return True
  if i < 0 or j < 0 or i >= board.get_num_rows() or j >= board.get_num_cols():
    return False
  value = board.get_by_pos(i,j)
  if value == 'X':
    return True
  else:
    region.add((i,j))
    return (is_region_x_surrounded(board, i-1, j, region) and
            is_region_x_surrounded(board, i+1, j, region) and
            is_region_x_surrounded(board, i, j-1, region) and
            is_region_x_surrounded(board, i, j+1, region))

def solver(board):
  # check the board without border
  region = set()
  num_rows = board.get_num_rows()
  num_cols = board.get_num_cols()
  for i in range(1,num_rows - 1):
    for j in range(1,num_cols - 1):
      if is_o(board,i,j):
        sub_region = set([(i, j)])
        if is_region_x_surrounded(board, i, j, sub_region):
          # Replace all positions in 'sub_region' with 'X's.
          print "Sub region: %s" % sub_region
          for pos in sub_region:
            print " Pos: %s" % pos
            board.set_by_pos(pos[0], pos[1], 'X')

      #   # check the neighbour
      #   region.update(sub_region)
      #   region.update(check(board,i-1,j))
      #   region.update(check(board,i+1,j))
      #   region.update(check(board,i,j-1))
      #   region.update(check(board,i,j+1))
  return region

b = Board(4,4,'X')
# args: row,col,letter
b.set_by_pos(1,1,'O')
b.set_by_pos(1,2,'O')
b.set_by_pos(2,2,'O')
b.set_by_pos(3,2,'O')

print str(b)
print solver(b)
# print b.getitem(p)
# print b.get_by_pos(2,2)
# print b.get_num_rows()
# print b.get_num_cols()
