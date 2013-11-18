'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''
def add_binary(str1,str2):
  '''
  Args: two binary_string
  Return: sum of the two binary strings in binary
  '''
  # sum of the two binary strings
  total = []
  
  max_len = max(len(str1), len(str2))
  # fill the string with zeros to make the two strings same length
  # turn the string to list and reverse it
  list1 = list(str1.zfill(max_len))
  list1.reverse()
  list2 = list(str2.zfill(max_len))
  list2.reverse()
  
  carry = 0
  for i in range(max_len):
    # sum for this bit
    bit_sum = int(list1[i])+ int(list2[i]) + carry
    total.append(str(bit_sum % 2))
    if bit_sum >= 2:
      carry = 1
   
  if carry == 1:
    total.append('1')
  
  total.reverse()  
  
  return ''.join(total)

