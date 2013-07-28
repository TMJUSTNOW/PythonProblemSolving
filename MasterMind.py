'''
MasterMind game:
two player. codemaker,codebreaker
codemaker make 4 numbers, coderbreaker guess up to 12 times
codemaker will give codercreaker how many digit are right number in right position
and how many digit are right number in wrong position
'''
ROUNDMAX = 12 # the maxium number of rounds for the game
# return the map of the codebreaker's guess
# how many numbers are right and in the right position 
# how many numbers are right but in the right position
def Result(code,guessCode):
  res = {
      'RightNumRightPos':0,
      'RightNumWrongPos':0
  }
  # build code map : key - digit , value - index
  codeMap = {}
  for i in range(len(code)):
    codeMap[code[i]] = i
  
  if len(guessCode) > 4 :
    return 'wrong number'
  else:
    for guess in guessCode :
      if guess in codeMap:
        if codeMap[guess] == guessCode.index(guess):
          res['RightNumRightPos'] += 1
        else:
          res['RightNumWrongPos'] += 1

  return res

# main loop for the game 
def MasterMind(code):
  round = ROUNDMAX
  while round >=0 :
    guessCode = str(raw_input('guess the code \n'))
    res = Result(code,guessCode)
    RightNumRightPos = res['RightNumRightPos']
    RightNumWrongPos = res['RightNumWrongPos']
    print 'Right number in right position: %d Right number in wrong position: %d' % (RightNumRightPos, RightNumWrongPos)
    if RightNumRightPos == 4:
      return 'Congrats You Win'
    round -= 1
  
  return 'Sorry you lose, the real number is %s' % code

print MasterMind('1234')