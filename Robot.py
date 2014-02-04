
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

  def __init__(self,x,y):
    self.x = x
    self.y = y
  def __repr__(self):
    return '(' + str(self.x) + ',' + str(self.y) + ')'

def no_moves(point):
  '''
    cannnot move reach the border
  '''
  return point.x == N or point.y == N
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

  num_paths_found = 0
  while queue:
    path = queue.pop(0)
    print path
    if no_moves(path[-1]):
      num_paths_found += 1
    else:
      for move in next_moves(path[-1]):
        # print str(move)
        new_path = path[:]
        new_path.append(move)
        queue.append(new_path)
  return num_paths_found

# print has_more_move(1,1)
start = Point(0,0)

print robot_moves(start)


