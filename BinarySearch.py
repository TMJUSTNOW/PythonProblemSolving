def binary_search(sortedList, num=None, start=None, end=None):
  '''
    binary search recursively
  '''
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
    return binary_search(sortedList,num,start,middleIdx - 1)
  elif num > middle:
    return bbinary_search(sortedList,num,middleIdx + 1, end)
  else:
    return True
    
def binary_search_iter(sortedList,num=None, start=None, end=None):
  '''
    binary search iteratively
  '''
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