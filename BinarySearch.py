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