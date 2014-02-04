'''
A message containing letters from A-Z is being encoded to numbers 
using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, 
determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''
dict = {
  '1': 'A',
  '2': 'B',
  '3': 'C',
  '4': 'D',
  '5': 'E',
  '6': 'F',
  '7': 'G',
  '8': 'H',
  '9': 'I',
  '10': 'J',
  '11': 'K',
  '12': 'L',
  '13': 'M',
  '14': 'N',
  '15': 'O',
  '16': 'P',
  '17': 'Q',
  '18': 'R',
  '19': 'S',
  '20': 'T',
  '21': 'U',
  '22': 'V',
  '23': 'W',
  '24': 'X',
  '25': 'Y',
  '26': 'Z',
}

def decode(message):
  num_ways  = 0
  for i in range(len(message) - 1):

  return num_ways