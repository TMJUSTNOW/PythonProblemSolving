'''
write a method that returns all subsets of a set
bit based algorithm 
all the items in the set have correspoinding bit position
there are 1 << n combinations for the subset 
'''

def subsets(items):
  '''
    given the list of items
    return the list of subsets
  '''
  all_subsets = []
  n = len(items)
  for num in range(1,1 << n):
    subset  = []
    for b in range(n):
      if num & (1 << b):
        subset.append(items[b])
    all_subsets.append(subset)
  return all_subsets

print subsets([1,2,3])

'''
how to write recursively
'''
