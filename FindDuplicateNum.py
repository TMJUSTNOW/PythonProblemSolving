# given a list of numbers 1-10000, the size of the array is 10001
def findDuplicate(arr):
  dup = 0
  for i in range(len(arr)):
    dup ^= arr[i] ^ i
    print i, dup

  return dup

arr = [1,2,3,4,5,3]
print findDuplicate(arr)