"""Given an array S of n integers, 
find three integers in S such that the sum is equal to a given number,
target. Return the sum of the two integers. 
You may assume that each input would have exactly one solution.
for example, [1,2,3,4,5] target = 6, return 1,5,
"""
# given a list of numbers and a target, return the two numbers whose sum is equal to target
# it is n^2
def TwoSum(listNum,target):
 # sort thte list
  newList = sorted(listNum)
  solutions = set()
  for i in newList:
    rest = target - i
    for j in newList:
      if j == rest:
        solutions.add(tuple(sorted((i,j))))
  return solutions
def TwoSumBiSearch(listNum,target):
  newList = sorted(listNum)
  solutions = set()
  for i in newList:
    rest = target - i
    if binarySearchIter(newList,rest,0,len(listNum)) == True:
      solutions.add(tuple(sorted( (i,rest) )))
  return solutions
# make nlogn
# look up a number in binary search
# recursively 
def binarySearch(sortedList, num=None, start=None, end=None):
  if num is None:
    raise Error("I can't search for nothing!")
  if start is None:
    start = 0
  if end is None:
    end = len(sortedList) - 1

  if start > end:
    return False
  middleIdx = (start +  end) / 2
  middle = sortedList[middleIdx]
  if num < middle:
    return binarySearch(sortedList,num,start,middleIdx - 1)
  elif num > middle:
    return binarySearch(sortedList,num,middleIdx + 1, end)
  else:
    return True
#  iteratively
def binarySearchIter(sortedList,num=None, start=None, end=None):
  if start is None:
    start = 0
  if end is None:
    end = len(sortedList) - 1 
  while start <= end:
    print start, end
    middleIdx = (start + end) / 2
    middle = sortedList[middleIdx]
    if num > middle:
      start = middleIdx + 1
    elif num < middle:
      end = middleIdx - 1
    else:
      return True
  return False

def test():
  arr = [1,2,3,4,5,7,9]
  print TwoSum(arr,5)
  print binarySearchIter(arr,3)
  # print TwoSumBiSearch(arr,5)
test()
