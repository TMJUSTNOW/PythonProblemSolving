'''
It consists of three rods, and a number of disks of different sizes which can slide
onto any rod. The puzzle starts with the disks in a neat stack in ascending order of 
size on one rod, the smallest at the top, thus making a conical shape.

The objective of the puzzle is to move the entire stack to another rod, 
obeying the following simple rules:
  Only one disk may be moved at a time.
  Each move consists of taking the upper disk from one of the stacks 
  and placing it on top of another stack.
  No disk may be placed on top of a smaller disk.
  
'''
NUMSTACKS = 3
class Hanoi(object):
  '''
  solve the hanoi puzzle
  Args:
    num_stacks: the number of stacks
    disks: list of numbers indicating the size of the disk in ascending order
           smallest at the top
  '''
  def __init__(self,disks=[1,2,3,4,5,6,7]):
    self.num_stacks = NUMSTACKS
    self.disks = disks
    self.stacks = []
    # create stacks 
    for i in range(self.num_stacks):
      self.stacks.append([])
    # the initial status of the stacks
    # first stack has all the disks as ascending order
    # the last item in the list is the top
    self.stacks[0] = sorted(disks,reverse=True)[:]
  
  # def can_place(self,stack,disk_size):
  # '''
  #   Only one disk may be moved at a time.
  #   Each move consists of taking the upper disk from one of the stacks 
  #   and placing it on top of another stack.
  #   No disk may be placed on top of a smaller disk.

  #   Args:
  #     stack: the stack that the disk is going to be placed
  #     disk_size: the size of the disk
  #   Return:
  #     True if the disk can be placed onto this stack
  # '''
  #   if not stack:
  #     return True
  #   elif disk_size < stack[-1]:
  #     return True
  #   else:
  #     return False
def solver(n, start, to, via):
  if n > 0:
    solver(n-1, start, via, to)
    print 'move disk %d from stack %d to stack %d via stack %d' % (n,start,to,via)
    # solver(1, start, to, via)
    solver(n-1, to, start, via)

def main():
  # h = Hanoi(3,[2,3,1])
  # print h.stacks
  solver(4,1,3,2)

main()


