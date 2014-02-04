'''
Given a string s and a dictionary of words dict, 
determine if s can be segmented into a space-separated sequence of 
one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''

DICT =["cat", "cats", "and", "sand", "dog"]

def is_word(word):
  return word in DICT
'''
given the string and dictionary,  
check whether the string can be space-seperated sentence

Args: string

Return: True or False
'''
def word_break(s):
  if not s:
    return True
  else: 
    for i in range(len(s)):
      # string slicing 
      word = s[0:i+1]
      if is_word(word):
        rest = s[i+1:]
        if word_break(rest):
          return True
    # defaul there is no solution
    return False 
# check wether it is empty string
def word_break_no_empty(s):
  if not s:
    return False
  else:
    return word_break(s)

'''
Given a string s and a dictionary of words dict,
add spaces in s to construct a sentence 
where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
'''

'''
construct a sentense with space-separated words based on the given string 
and dictionary

Args: string
Return: list of sentences 

'''

def solver(s):
  results = []
  if not s:
    results.append('')
  else:
    for i in range(len(s)):
      word = s[0:i+1]
      if is_word(word):
        sub_sentences = solver(s[i+1:])
        for sentence in sub_sentences:
          # append the first word
          results.append(word + ' ' + sentence )
  return results

def main():
  test1 = 'leetcode'
  test2 = 'catsanddog'
  print word_break_no_empty(test2)
  print solver(test2)
  # print results

main()
