'''
  Sum Root to Leaf Number
'''
class Node(object):
  def __init__(self,val=None,left=None,right=None):
    self.val = val
    self.left = left
    self.right = right

def SumNumbers(root):
  return SumRootToLeaf(root,0)

def SumRootToLeaf(root,total) :
  '''
    Args: a binary tree containing digits from 0-9 only, 
          each root to leaf path represent a number

    Return: total sum of all root to leaf numbers
    For example,
       1
      2 3
    represents as 123, 1->2 represents 12, 1->3 represents 13
    return the sum = 12 + 13 = 25
  '''
  if root is None :
    return 0
  total = total * 10 + root.val
  if root.left is None and root.right is None:
    return total
  else : 
    return SumRootToLeaf(root.left,total) + SumRootToLeaf(root.right,total)

root = Node(1,Node(2,Node(4)),Node(3))

print SumNumbers(root)
  
