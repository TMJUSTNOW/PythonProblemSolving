'''
Reverse linked list
'''
class Node(object):
  '''
  node for the linked list 
  '''
  def __init__(self,data=None,next=None):
  	self.data = data
  	self.next = next

class LinkedList(object):
  '''
  create linked list
  '''
  def __init__(self,head=None):
    self.head = head
  
  def __str___(self):
    '''
    Print out the linked list
    '''
    nodeList = []
    p = self.head
    if p is None:
      return 'empty list'
    else:
      while p:
        nodeList.append(str(p.data))
        p = p.next
    return '->'.join(nodeList) + '->null'
  def Reverse(self):
    '''
    reverse linked list
    '''
    current = self.head
    prev = None
    next = current.next
    while current:
      current.next = prev
      prev = current
      current = next
      next = next.next if next else None
    self.head = prev

linkedList = LinkedList(Node(1,Node(2,Node(3,Node(4)))))

