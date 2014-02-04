'''
you have an input string like "banana"
you want to sort the characters in the string
based on the order they appear in a reference string, 
e.g., "bna" so "banana" would sort as "bnnaaa"
'''

def solver(ref_str,str1):
  str_list = []
  for ref_char in ref_str:
    count = 0
    for char in str1:
      if char == ref_char:
        count += 1
    for i in range(count):
      str_list.append(ref_char)
  return ''.join(str_list)    

def solver1(ref_str,st1):
  str_list = []
  map = {}
  for char in str1:
    map[char] = map.get(char, 0) + 1
  for ref_char in ref_str:
    str_list.append(ref_char * map[ref_char])
  return ''.join(str_list)

str1 = 'banana'
ref_str = 'bna'

print solver1(ref_str,str1)
