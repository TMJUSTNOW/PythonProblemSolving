import unittest

class Node(object):
  def __init__(self,data=None,next=None):
    self.data = data
    self.next = next

def listToString(head):
  s = ''
  p = head
  while p:
    s += str(p.data) + '->'
    p = p.next
  s += 'NULL'
  return s

def listLength(head):
  i = 0
  p = head
  while p:
    p = p.next
    i =  i + 1

  return i

'''
  remove the nth node from end of the list
  1->2->3->4, n=2, return 1->2->4
'''
def RemoveNthNodeFromEnd(head,n):
  '''
    Args: head node of the linked list, 
          the nth node from the end of the list
    Return: the head of the linked list
  '''
  p = head
  q = head
  if n <= 0 or n > listLength(head):
    raise Exception("Invalid n")
  elif n == listLength(head):
    head = p.next
  else:
    while n >= 0:
      q = q.next
      n = n - 1
    while q:
      p = p.next
      q = q.next

    p.next = p.next.next

  return head

def assertEquals(a, b):
  if a != b:
    raise Exception("Values not equal: %s vs. %s" % (a, b))

def assertRaises(f, *args, **kwargs):
  raised = False
  try:
    f(*args, **kwargs)
  except:
    raised = True
  if not raised:
    raise Exception("Exception was not raised")

# printList(RemoveNthNodeFromEnd(head,4))
def GetTestList():
  return Node(1,Node(2,Node(3,Node(4))))
assertEquals("1->2->3->4->NULL", listToString(GetTestList()))
# assertEquals("1->2->3->4->NULL", listToString(RemoveNthNodeFromEnd(head, 0)))
# assertRaises(RemoveNthNodeFromEnd(head, 0))
assertRaises(RemoveNthNodeFromEnd, GetTestList(), 0)
assertEquals("1->2->3->NULL", listToString(RemoveNthNodeFromEnd(GetTestList(), 1)))
assertEquals("1->2->4->NULL", listToString(RemoveNthNodeFromEnd(GetTestList(), 2)))
assertEquals("1->3->4->NULL", listToString(RemoveNthNodeFromEnd(GetTestList(), 3)))
assertEquals("2->3->4->NULL", listToString(RemoveNthNodeFromEnd(GetTestList(), 4)))
assertRaises(RemoveNthNodeFromEnd, GetTestList(), 5)


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()


