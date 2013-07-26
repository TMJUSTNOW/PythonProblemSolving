# given a string, return reverse words in a string
# 'do or do not, there is no try.' => 'try. no is there, not do or do'
def reverseWords0(string):
  a = string.split(' ')
  print a
  a.reverse()
  return ' '.join(a)

# reverse string
def reverseArr(arr,i,j):
  '''
  string = s # save the string first.ALWAYS!!!!
  # arr = string.split() # string is immutable, has to be changed to list
  # split function is to split the string with separator
  arr = list(string)
  '''
  while i <= j:
    temp = ''
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    i += 1
    j -= 1
  # print arr
  
  return arr

# don't use the reverse function in python,reverse them manually
# reverse the entire string first and then reverse the word
def reverseWords(string):
  arr = list(string)
  print reverseArr(arr,0,len(string)-1)

  start = 0
  end = 0
  while end < len(string):
    if arr[end] == ' ':
      reverseArr(arr,start,end-1)
      # print arr
      start = end + 1
      
    end += 1

  if start < end:
    reverseArr(arr,start,end - 1)

  return ''.join(arr)

string = 'do or do not, there is no try.'
print reverseWords0(string)
# print reverseStr('asdf',0,3)
# print reverseArr(['1','2','4'],0,3)
print reverseWords(string)