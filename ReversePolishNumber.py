'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Which is the postfix 
Valid operators are +, -, *, /. 
Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''
import operator

ops = {
  '+':operator.add,
  '-':operator.sub,
  '*':operator.mul,
  '/':operator.div,
}

def ReversePolishNumber(inputs):
  stack = []
  for input in inputs:
    if input not in ops:
      stack.append(input)
    else:  
      val1 = int(stack.pop())
      val2 = int(stack.pop())

      result = str(ops[input](val2, val1))
      stack.append(result)

  return stack.pop()

test1 = ["2", "1", "+", "3", "*"]
test2 = ["4", "13", "5", "/", "+"]
print ReversePolishNumber(test1)