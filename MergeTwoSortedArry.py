'''
Given two sorted arr, merge them together, return one sorted array
'''
def MergeTwoSortedArr(arr1,arr2):
  result = []
  i = 0
  j = 0
  while i < len(arr1) and j < len(arr2):
  	if arr1[i] <= arr2[j] :
  	  result.append(arr1[i])
  	  i += 1
  	else:
  	  result.append(arr2[j])
  	  j +=1
  if i < len(arr1):
  	  result.extend(arr1[i:])
  if j < len(arr2):
  	  result.extend(arr2[j:])
  return result


print MergeTwoSortedArr([1,3,5],[2,4,6,7])