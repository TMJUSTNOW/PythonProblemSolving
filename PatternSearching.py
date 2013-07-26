# pattern searching
# given a string  and a pattern string
# return the index of where they found the pattern in the string

def patternSearching(string,pattern):
  arr = []
  for i in range(len(string)):
    if string[i] == pattern[0]:
      print i
      start = i + 1
      isSame = True
      for j in range(1,len(pattern)):
        if pattern[j] != string[start]:
          isSame = False
        start += 1
      if isSame == True:
        arr.append(i)
  return arr 
'''
The number of comparisons in best case is O(n).
What is the worst case ?
The worst case of Naive Pattern Searching occurs in following scenarios.
1) When all characters of the text and pattern are same.

txt[] = "AAAAAAAAAAAAAAAAAA"
pat[] = "AAAAA".
2) Worst case also occurs when only the last character is different.

txt[] = "AAAAAAAAAAAAAAAAAB"
pat[] = "AAAAB"
Number of comparisons in worst case is O(m*(n-m+1)).
Although strings which have repeated characters are not likely to appear in English text,
they may well occur in other applications (for example, in binary texts). 
The KMP matching algorithm improves the worst case to O(n).
'''

string = 'abcdabca'
pattern = 'bc'
print patternSearching(string,pattern)