# palindrome integer is the reverse order and the original order are the same
# which means reads the same in both directions

# Determine whether an integer is paindrome 
# num 121,reverse 1, 1*10 + 2, 12+10 + 1
def PalindromeInt(num): 
  reverse = 0
  number = num
  while number > 0:
    reverse = reverse * 10 + number % 10
    number /= 10

  return reverse  

print PalindromeInt(121)

# given a string s,find the longest palindrome substring in s