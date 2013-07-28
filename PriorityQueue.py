
import Heap

# implement priority queue
class Node(object):
  def __init__(self,data=None,priority=None):
    self.data = data
    self.priority = priority

  def __repr__(self):
    return "%s %d" % (self.data, self.priority)

class PriorityQueue(object):
  def __init__(self):
    # self._heap = Heap.MinHeap(key=lambda x: -x.priority)
    self._heap = Heap.MaxHeap(key=lambda x: x.priority)

  def add(self, data, priority):
    node = Node(data=data, priority=priority)
    self._heap.insert(node)

  def remove(self):
    return self._heap.pop()

  def size(self):
    return self._heap.size()

pq = PriorityQueue()
pq.add("Task 1", 5)
pq.add("Task 2", 10)
pq.add("Task 3", 1)
pq.add("Task 4", 3)
pq.add("Task 5", 2)
pq.add("Task 6", 7)

while pq.size():
  print pq.remove()
