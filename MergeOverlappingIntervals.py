'''
  Merge overlapping intervals
'''
def MergeIntervals(intervals):
  '''
    Args: a set of intervals like [1,3],[2,4],[5,7],[6,8]
    Return [1,4],[5,8]
  '''
  i = 0
  # copy the list first
  inters = intervals[:]
  total = len(inters) - 1
  # sort the list by starting time
  inters.sort(key=lambda x: x[0])
  # function(x) { return x[0]; }
  while i < total: 
    if inters[i][0] < inters[i+1][0] and inters[i][1]> inters[i+1][0]:
      inters[i][1] = inters[i+1][1]
      inters.remove(inters[i+1])
      total = total - 1 
    i = i + 1

  return inters

def MergeIntervalsBetter(intervals):
  '''
    using stack for hosting
  '''
  inters = intervals[:]
  #  sort the first time by ascending order
  inters.sort(key=lambda x : x[0])
  stack = []
  for inter in inters:
    if len(stack) == 0 or inter[0] > stack[-1][1]:
      stack.append(inter)
    elif inter[0] < stack[-1][1] and inter[1] > stack[-1][1]: 
      stack[-1][1] = inter[1]  
  return stack

a = [[2,4],[1,3],[5,7],[6,8]]
print MergeIntervals(a)

print MergeIntervalsBetter(a)
