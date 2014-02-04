class TreeNode(object):
  '''
    tree node for binary tree
  '''
  def __init__(self,data=None,left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

class BinaryTree(object):
  '''
    Binary Tree
  '''  
  def __init__(self,root):
    self.root = root

  def level_print(self):
    '''
      print binary tree by level
    '''
    thisLevel = [self.root]
    while thisLevel:
      nextLevel = []
      print [i.data for i in thisLevel]
      for node in thisLevel:
        if node.left is not None:
          nextLevel.append(node.left)
        if node.right is not None:
          nextLevel.append(node.right)
      thisLevel = nextLevel
  
  def bfs(self):
    '''
     breath first search to print the tree
    '''
    queue = [self.root]
    while queue:
      # print [i.data for i in queue]
      node = pop(0)
      print node.data
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
  
  def dfs(self):
    '''
    depth first search to print the tree
    '''
    # stack last in first out
    stack = [self.root]
    while stack:
      node = stack.pop()
      print node.data
      if node.right:
        stack.append(node.right)
      if node.left:
        # pop left first
        stack.append(node.left) 
