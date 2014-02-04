'''
Given an array of integers, 
every element appears twice except for one. 
Find that single one.
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
'''
'''
find the single occurence number in array of integers whose occurence are two 
except one
args: array of integers
return: the once occurence number in the array
'''
def single_num(arr):
  # create a map for the occurence of number
  map = {}
  for num in arr:
    if num in map:
      map[str(num)] += 1
    else:
      map[str(num)] = 1
  # look for the num
  for key in map:
    if map[key] == 1:
      return key
    else:
      return None

test = [1,2,2,4,4]
print single_num(test)


'''
Given an array of integers, 
every element appears three times except for one. 
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?

'''