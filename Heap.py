# implement priority queue 
# using heap to sort the priority 
class Node(object):
  def __init__(self,data=None,priority=None):
    self.data = data
    self.priority = priority

# implement the min heap
class MinHeap(object):
  def __init__(self, key=None):
    self.items = []
    self._key = key or (lambda x: x)
  
  def size(self):
    return len(self.items)

  def swap(self,a,b):
    temp = self.items[a]
    self.items[a] = self.items[b]
    self.items[b] = temp

  # inset an element into the list
  def insert(self,num):
    self.items.append(num)
    n = len(self.items) -1
    # siftup the nth element in the list
    self.siftup(n)
    return self.items
  # siftup the nth element
  def siftup(self,n):
    i = n
    # parent index
    p = (n - 1)/2
    while i >= 0 and (
        self._key(self.items[p]) > self._key(self.items[i])):
      temp = self.items[i]
      self.items[i] = self.items[p]
      self.items[p] = temp
      i = p
      p = (n - 1)/2
    return self.items
  # siftdown the element place on the first position in the heap
  def siftdown(self,n):
    i = 0
    while True:
      left = 2 * i + 1
      if left > n:
        break
      lesser_child = left
      right = 2 * i + 2
      if right <= n and (
          self._key(self.items[right]) < self._key(self.items[left])):
        lesser_child = right
      if self._key(self.items[i]) <= self._key(self.items[lesser_child]):
        break
      self.swap(i, lesser_child)
      i = lesser_child
    return self.items

  #  pop the heap, return the root
  def pop(self):
    minNode = self.items[0]
    last = self.items.pop()
    if self.items:
      self.items[0] = last
    #  place the last element on the root and then siftdown
    self.siftdown(len(self.items)-1)

    return minNode

class MaxHeap(MinHeap):
  def __init__(self, key=None):
    super(MaxHeap, self).__init__()
    self._key = (lambda x: -key(x)) if key else (lambda x: -x)

def main():
  minheap = MinHeap()
  print minheap.insert(2)
  print minheap.insert(1)
  print minheap.insert(3)
  print minheap.insert(6)
  print minheap.insert(8)
  print minheap.insert(4)
  print minheap.pop()
  print minheap.items

if __name__ == "__main__":
  main()
