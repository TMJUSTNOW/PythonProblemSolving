class Node(object):
  def __init__(self,data=None,next=None):
    self.data = data
    self.next = next
# print the linked list
def printLinkedList(head):
  s = []
  p = Node(next=head) # create an empty node
  while p.next :
    s.append(str(p.next.data))
    p = p.next
  s.append('Null') # using list instead of string concatenation
  return '->'.join(s)

# print the nth element to the last element of a a linked list
# given the n and the head node of the linked list
def printNToLast(n,head):
  p = Node(next=head)
  q = Node(next=head)
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
  fast = Node(next=head)   
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
print printLinkedList(head)
printNToLast(2,head)
print DetectCircle(head)
