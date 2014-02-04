'''
remove the loop in linked list
'''
class Node(object):
  def __init__(self,data=None,next=None):
    self.data = data
    self.next = next

'''
given the head node of the linked list,
find how big is the loop

return the length of the loop and a node in the loop
'''
def loop_len(head):
  '''
  create tow pointers with different speed,
  save the node they meet to calculate the length of the loop
  '''
  # fast = Node()
  # slow = Node()
  # fast.next = head
  # slow.next = head
  fast = head
  slow = head

  while fast and slow:
    fast = fast.next.next
    slow = slow.next
    if fast == slow:
      start_loop = fast
      break
  # the length of the loop 
  # self pointing node, loop length is zero
  p = start_loop
  length = 0
  while p:
    p = p.next
    length += 1
    if p == start_loop:
      break
    
  return (length,start_loop)

def remove_loop(head):
  '''
  create two pointer wit the distance of the loop's length
  when the two pointers meet again,that's the start of the loops
  remove the link between the previous node and the start node of the loop

  '''
  loop_length,start_loop = loop_len(head)
  # p1, the start node, p2 the nex
  # p1 = Node()
  # p2 = Node()
  # p3 = Node()
  p1 = head
  # p2 = p1.next
  p3 = head
  k = loop_length
  while k:
    p3 = p3.next
    k -= 1 
  # move the two pointers to the start loop node
  # while p1 != start_loop:
  #   p1 = p1.next
  #   p2 = p2.next
  #   p3 = p3.next

  while p1.next != p3.next:
    p1 = p1.next
    # p2 = p2.next
    p3 = p3.next
  # remove the link between p1 and p3
  p3.next = None

N = 6
nodes = [Node(data=d) for d in range(N)]
for i in range(N - 1):
  nodes[i].next = nodes[i + 1]
nodes[N - 1].next = nodes[2]
head = nodes[0]

def PrintNodes(head):
  data = []
  seen_nodes = set()
  node = head
  while node:
    data.append(str(node.data))
    if node in seen_nodes:
      break
    seen_nodes.add(node)
    node = node.next
  print "->".join(data)

PrintNodes(head)
remove_loop(head)
PrintNodes(head)

