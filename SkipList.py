# implement skip list
'''
make all nodes level 1
j ← 1
while the number of nodes at level j > 1 do
  for each i'th node at level j do
    if i is odd 
      if i is not the last node at level j
        randomly choose whether to promote it to level j+1
      else
        do not promote
      end if
    else if i is even and node i-1 was not promoted
      promote it to level j+1
    end if
  repeat
  j ← j + 1
repeat
'''
class Node(object):
  def __init__(self,data=None):
    # The single data element for this node.
    self.data = data
    self.nexts = []


class SkipList(object):
  def __init__(self):
    # The root nodes at each level, with the lowest level 
    # (the one with no skips) first.
    self.root = Node()

  def insert(self, value):
    pass

  def findPredecessor(self, value):
    """Find the node before the given value."""
    node = self.root
    if not len(node.nexts):
      node.ne
    level = len(node.nexts) - 1
    if level



head = Node(1,Node(2,Node(3,Node(4))))
    