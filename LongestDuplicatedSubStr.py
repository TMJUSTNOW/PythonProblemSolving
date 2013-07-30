#  given an input file of text, find the longest duplicated subsstring of characters in it.
#  for example, 'Ask not what your country can do for you, but what you can do for your country'
#  the longest duplicated substring is 'can do for you' then 'your country'

# build suffix array based on the string
def SuffixArr(string):
  suffixArr = []
  i = 0
  while i < len(string) :
    suffixArr.append(string[i:])
    i += 1
  return suffixArr

# only start from the beginning of the two strings,
# return the length that its two parameter strings have in common
def ComLen(string1, string2):
  commonLenth = 0
  minLen = min(len(string1),len(string2))
  for i in range(minLen):
    if string1[i] == string2[i]:
      commonLenth += 1
    else:
      break
  return commonLenth

# build the suffix substring based on the given string then sort them
# compare the adjacent substrings in the array
# find the longest common length of two adjacent substrings
def LongestDupSubStr(string):
  arr = SuffixArr(string)
  arr.sort()
# scan through the array comparing adjacent elements 
# to find the longest repeated string
  print arr
  maxLen = ComLen(arr[0],arr[1])
  maxi = 0
  for i in range(1,len(arr)-1 ):
    if ComLen(arr[i],arr[i+1]) > maxLen:
      maxLen = ComLen(arr[i],arr[i+1])
      maxi = i
  print maxLen
  return arr[maxi][0:maxLen]
print LongestDupSubStr('Ask not what your country can do for you, but what you can do for your country')