# preorder, inorder,postorder traversal for the binary tree
class Node(object):
  '''
    TreeNode
    Args: data, left child, right child
  '''
  def __init__(self,data=None,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right

class BinaryTree(object):
  def __init__(self):
    self.root = None
  def PreOrder(self,node):
    if node is None:
      return
    self.PreOrder(node.left)
    self.PreOrder(node.right)
    print node.data
  def InOrder(self,node):
    if node is None:
      return
    self.PreOrder(node.left)
    print node.data
    self.PreOrder(node.right)
  def PostOrder(self,node):
    if node is None:
      return
    print node.data
    self.PostOrder(node.left)
    self.PostOrder(node.right)

'''
   1
 2   4
3   5 6 
'''
c = Node(3)
d = Node(5)
e = Node(6)
a = Node(2,c)
b = Node(4,d,e)
root = Node(1,a,b)
tree = BinaryTree()
tree.PreOrder(b)


