class TreeNode(object):
  def __init__(self,data=None,left=None, right=None):
    self.data = data
    self.left = left
    self.right = right
 
  # print binary tree by level
def levelPrint(root):
  thisLevel = [root]
  while thisLevel:
    nextLevel = []
    print [i.data for i in thisLevel]
    for node in thisLevel:
      if node.left is not None:
        nextLevel.append(node.left)
      if node.right is not None:
        nextLevel.append(node.right)
    thisLevel = nextLevel
# breath first search to print the tree
def bfs(root):
  queue = [root]
  while queue:
    # print [i.data for i in queue]
    node = pop(0)
    print node.data
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
# depth first search to print the tree
def dfs(root):
  # stack last in first out
  stack = [root]
  while stack:
    node = stack.pop()
    print node.data
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left) # pop left first

c = TreeNode(6)
d = TreeNode(4)
e = TreeNode(5)
a = TreeNode(2,c)
b = TreeNode(3,d,e)
root = TreeNode(1,a,b)
levelPrint(root)
bfs(root)
print 'dfs'
dfs(root)
