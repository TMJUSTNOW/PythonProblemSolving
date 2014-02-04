'''
imagine a robot sitting on the upper left hand corner of an N*N grid,
the robot can only move in two directions: right and down
How many possible paths are there for the robot?
FLLOW UP 
imagine certain squares are 'off limits',such that the robot can not step on 
them
Design an algorithm to get all possible paths for the robot
'''
N = 3
class Point(object):
  '''
  represent the position on the board
  '''
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def __repr__(self):
    return '(' + str(self.x) + ',' + str(self.y) + ')'

def no_moves(point):
  '''
    final state: cannnot move reach the border
  '''
  return point.x == N-1 and point.y == N-1
def next_moves(point):
  '''
    given the current loctation,
    get the possible next moves,
    whether it can move right and down

    return the list of next moves
  '''
  nexts = []
  if point.x + 1 < N:
    nexts.append(Point(point.x + 1, point.y))
  if point.y + 1 < N:
    nexts.append(Point(point.x, point.y + 1)) 
  
  return nexts

def robot_moves(start):
  '''
    given the start position of the robot,
    find all possible moves 

  '''
  queue = []
  queue.append([start])
  all_paths = []
  while queue:
    path = queue.pop(0)
    # print str(path)
    if no_moves(path[-1]):
      all_paths.append(path)
    else:
      for move in next_moves(path[-1]):
        # print str(move)
        new_path = path[:]
        new_path.append(move)
        queue.append(new_path)

  return all_paths

'''
return the number of all the paths
'''
def robot_num_paths(start):
  queue = []
  queue.append(start)
  num_path = 0
  while queue:
    move = queue.pop(0)
    if no_moves(move):
      num_path += 1
    else:
      for next_move in next_moves(move):
        queue.append(next_move)

  return num_path

def robot_recursive(start):
  if no_moves(start):
    return True
  for sib in next_moves(start):
    if robot_recursive(sib):
      return True
  return False





'''
test
'''

start = Point(0,0)

print robot_num_paths(start)
print "\n"
all_paths = robot_moves(start)
print len(all_paths)
print all_paths


class cacher(object):

  def __init__(self, func):
    # print "__init__()"
    self.cache = {}
    self.func = func

  def __call__(self, *args):
    cache_key = tuple(args)
    if cache_key in self.cache:
      return self.cache[cache_key]
    else:
      result = self.func(*args)
      self.cache[cache_key] = result
      return result


DP_COUNT_PATHS_CACHE = {}

def dp_count_paths_cache(x, y):
  '''
    starting point is the destination the robot want to move to.
    ending point for the searching function is (0,0)

    count the numbe rof paths to x and y
  '''
  global DP_COUNT_PATHS_CACHE
  cache_key = (x, y)
  if cache_key in DP_COUNT_PATHS_CACHE:
    return DP_COUNT_PATHS_CACHE[cache_key]
  else:
    num_paths = 0
    if x > 0:
      num_paths += dp_count_paths(x - 1, y)
    if y > 0:
      num_paths += dp_count_paths(x, y - 1)
    if not x and not y:
      num_paths += 1
    DP_COUNT_PATHS_CACHE[(x, y)] = num_paths
    return num_paths


@cacher
def dp_count_paths(x, y):
  '''
    starting point is the destination the robot want to move to.
    ending point for the searching function is (0,0)
    
    count the numbe rof paths to x and y
  '''
  # if obstacle_matrix[x][y]:
  #   return 0
  num_paths = 0
  if x > 0:
    num_paths += dp_count_paths(x - 1, y)
  if y > 0:
    num_paths += dp_count_paths(x, y - 1)
  if not x and not y:
    num_paths = 1
  return num_paths

print "DP (cached): %d" % dp_count_paths_cache(4, 4)
print "DP (decorator): %d" % dp_count_paths(4, 4)

'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''