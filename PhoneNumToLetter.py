'''
Given a digit string, 
return all possible letter combinations that the number could represent.

A mapping of digit to letters
(just like on the telephone buttons) is given below.
1     2abc 3def
4ghi  5jkl 6mno
7pqrs 8tuv 9wxyz
  *     0   #

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''
phone_map = {
  2:'abc',
  3:'def',
  4:'ghi',
  5:'jkl',
  6:'mno',
  7:'pqrs',
  8:'tuv',
  9:'wxyz'
}

def letter_combination(str1):
  letters = []
  for char in str1:
    if phone_map[char]:
      letters.append(list(phone_map[char])
