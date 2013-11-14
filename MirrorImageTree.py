class Node(object):
  def __init__(self,data=None,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right

def Mirror(node):
  '''
    Build a mirror image for a binary tree
    Args: start node in the binary tree
  '''
  if node is None:
    return 
  else:
    newNode = Node(node.data)
    newNode.left = Mirror(node.right)
    newNode.right = Mirror(node.left)

  return newNode

def bfsPrint(root):
  queue = []
  queue.append(root)
  node = root
  while node and len(queue) > 0 :
    node = queue.pop(0)
    print node.data
    if node.left is not None:
      queue.append(node.left)
    if node.right is not None:
      queue.append(node.right)
def MirrorTrees(root1,root2):
  '''
    Check whether two trees are mirror
    Args: two root node for the binary trees
    Return : True or False if the two trees are mirror or not
  '''



   1
 2   3
 4 5
'''
a = Node(1,Node(2,Node(4),Node(5)),Node(3))
print 'a'
bfsPrint(a)
mirror = Mirror(a)
print 'mirror'
bfsPrint(mirror)

