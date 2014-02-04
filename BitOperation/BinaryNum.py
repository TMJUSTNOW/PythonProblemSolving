'''
Practice Bit Operation 
'''

'''
print binary representation of a positive number
'''
def Binary(num):
  binary_list = []
  binary_list.append(num % 2)
  num /= 2
  while num:
    binary_list.append(num % 2)
    num /= 2
  return ''.join(str(b) for b in reversed(binary_list))

for i in range(10):
  print "%d: %s" % (i, Binary(i))

'''
convert fraction to binary representation
'''