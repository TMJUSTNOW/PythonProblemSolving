class Node(object):
  """A node in a cyclic linked list."""

  def __init__(self, value):
    self.value = value
    self.next = None

  def GetPrevious(self):
    """Gets the node before this one."""
    before = self
    while before.next != self:
      before = before.next
    return before

class CyclicList(object):
  """A cyclic sorted linked list."""

  def __init__(self):
    self.root = None

  def Insert(self, value):
    """Inserts a sorted value into the list."""
    new_node = Node(value)
    if not self.root:
      # There were no nodes, so just make this one the root, self-link, and
      # we're done.
      self.root = new_node
      self.root.next = self.root
    else:
      last = None
      node = self.root
      # Look through all the nodes, finding the first one 'value' is greater
      # than. Also keep track of the last seen node since that will be needed
      # to insert.
      while node and value > node.value:
        if node.next == self.root:
          # We've completed the circle and come all the way back around to the
          # root being next, so this must be the new greatest element.
          new_node.next = node.next
          node.next = new_node
          inserted = True
          return
        # Keep looking.
        last = node
        node = node.next
      # Insert before 'node'.
      if not last:
        # The node must be less than the root, which means it'll be the new
        # root.
        last = node.GetPrevious()
      last.next = new_node
      new_node.next = node
      if node == self.root:
        # Make sure the root gets updated.
        self.root = new_node

  def __str__(self):
    """Gets a string representation of the linked list."""
    values = []
    node = self.root
    while node:
      values.append(str(node.value))
      node = node.next
      if node == self.root:
        # We've completed the circle, so stop.
        break
    return "->".join(values)


def testCyclicListInsert(values):
  """Tests inserting the values into a 'CyclicList'.

  Verifies that the list stays sorted at each step, and prints either 'Success'
  or '*** FAIL ***' for each step.
  """
  cyc_list = CyclicList()
  for i in range(len(values)):
    cyc_list.Insert(values[i])
    test_value = str(cyc_list)
    correct = "->".join(str(v) for v in sorted(values[0:i + 1]))
    success = test_value == correct
    print test_value, "Success" if success else "*** FAIL ***"
    if not success:
      print "Expected ", correct


testCyclicListInsert([1,6,72,2,3,5,5,9,1,0,2,6,72])
