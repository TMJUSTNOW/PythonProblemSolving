"""
Reverse linked list
"""
class Node(object):
  def __init__(self,data=None,next=None):
  	self.data = data
  	self.next = next
class LinkedList(object):
  def __init__(self,head=None):
    self.head = head
  
  # Print out the linked list
  def Display(self):
    nodeList = []
    p = self.head
    if p is None:
      print 'empty list'
    else:
      while p:
        nodeList.append(str(p.data))
        p = p.next
    print '->'.join(nodeList) + '->null'
  # reverse linked list
  def Reverse(self):
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
linkedList.Display()
linkedList.Reverse()
linkedList.Display()
