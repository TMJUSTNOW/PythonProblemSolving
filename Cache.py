class Node(object):
  '''
    implement LRU cache
    using doubly linked list
    null <- 1 <-> 2 <-> 3 <-> 4 ->null
  '''
  def __init__(self,pageNumbe,prev=None,next=None):
    self.pageNumber = pageNumber
    self.prev = prev
    self.next = next
class Cache(object):
  '''
    using double linked list to create cache
  '''
  def __init__(self,n):
    self.limit = n
    self.head = None
    self.tail = None

  def enqueue(self, pageNum):
    newNode = Node(pageNum)
    if self.head is None:
      self.head = newNode
      self.tail = newNode
    else: 
    # push the node on the first node
      newNode.next = self.head
      self.head.prev = newNode
      self.head = newNode

  # pop the least recent used page
  def LRU(self,pageNum):
    #  check whether the page is in the memory
    p = Node(next=self.head)
    # if it already in the memory, move to the end
    # if not, move to the end of the queue directly
  
    while p.next and p.next.pageNumber != pageNum:
        p = p.next
    node = p.next
    #remove the node
    if node.prev = null:
      self.head = node.next
    else:
      node.prev.next = node.next
    if node.next = null:
      self.tail = node.prev
    else:
      node.next.prev = node.prev
    # put in the end of the queue
    self.tail.next = node
    node.prev = self.tail
    self.tail = node

    return self.pop(0)
