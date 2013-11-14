class Node(object):
  def __init__(self,val=None,left=None,right=None):
    self.val = val
    self.left = left
    self.right = right
'''
  print all the path of a binary tree from root to the leaf
'''
paths = []
def AllPaths(root,paths):
  '''
    Args: root node of a binary tree
    Return: list of all the path from the root to the leaf
  '''
  if root is None:
    return paths
  if root.left is None and root.right is None:
    paths.append(root.val)
  else:
    path.
