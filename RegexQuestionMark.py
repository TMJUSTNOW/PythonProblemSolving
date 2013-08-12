'''
Given a string consist of '1','0' and '?'
return all the matching strings，
“?” can match 0 or  1
For example:
input : 1?? 
output: {100, 101, 110, 111}.

input: 100100?00?
output: {1001000000,1001000001,1001001000,1001001001}
'''

def Matching(listStr,level):
  if level == len(listStr):
    print listStr
    return

  if listStr[level] == '?':
    listStr[level] = '0'
    Matching(listStr,level+1)
    listStr[level] = '1'
    Matching(listStr,level+1)
    listStr[level] = '?'
  else:
    Matching(listStr,level+1)

def Main(string):
  result = list(string)
  Matching(result,0)

Main('1??')