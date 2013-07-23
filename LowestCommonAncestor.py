# build tree node
class TreeNode(object):
  def __init__(self,data=None,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right

# given two nodes,find the lowest common ancestor for the two node in binary search tree
def LowestCommonAncestor(root,node1,node2):
  while root:
    if root.data > node1.data and root.data > node2.data:
      root = root.left
    elif root.data < node1.data and root.data < node2.data:
      root = root.right
    else:
      return root

# create a binary search tree
'''  
    6
  3   7
1  4    8
'''
a = TreeNode(1)
b = TreeNode(4)
c = TreeNode(8)
d = TreeNode(3,left=a,right=b)
e = TreeNode(7,right=c)
root = TreeNode(6,d,e)
# root = TreeNode(
#     6,
#     left=TreeNode(
#         3,
#         left=TreeNode(1),
#         right=TreeNode(4)),
#     right=TreeNode(
#         7,
#         right=TreeNode(8)))
ancestor =  LowestCommonAncestor(root,a,d)
print ancestor.data