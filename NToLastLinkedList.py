class Node(object):
  def __init__(self,data=None,next=None):
    self.data = data
    self.next = next
# print the linked list
def printLinkedList(head):
  s = ''
  p = Node(next=head) # create an empty node
  # p.next = head
  while p.next :
    s += str(p.next.data) + '->'
    p = p.next

  s += 'Null'
  return s
# print the nth element to the last element of a a linked list
# given the n and the head node of the linked list
def printNToLast(n,head):
  p = Node()
  p.next = head
  q = Node()
  q.next = head
  for i in range(n-1):
    q = q.next
  while q.next:
    p = p.next
    q = q.next
  print printLinkedList(p)

# given a singlely linked list, check whether the linkedlist has circle
# create two pointer, one's moving speed is +1, another's moving speed is +2
# if the faster one move onto or over the slower one, then it has circle
def DetectCircle(head):
  slow = Node(next=head)
  # slow.next = head
  fast = Node(next=head)
  # fast.next = head      
  while True:
    if fast is None or fast.next is None:
      return False
    elif fast == slow or fast.next == slow :
      return True
    else:
      slow = slow.next
      fast = fast.next.next

# 1->2->3->4
head = Node(1,Node(2,Node(3,Node(4))))
# circle  = Node(6,head)
# head.next = circle
print printLinkedList(head)
printNToLast(2,head)
print DetectCircle(head)
