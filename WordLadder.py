'''
  word ladder
  only change one letter every time
  return the minimum steps
'''

DICT  = ['cat','cot','dot','dog']
CHARS = ['a','b','c','d','e','g','t','o']

def get_one_letter_neighbors(word):
  # make words that are one letter changed from the given word
  char_list = [c for c in word]
  # print char_list
  length = len(char_list)
  neighbors = []
  for i in range(length):
    for char in CHARS:
      if char != char_list[i]:
        print char
        new_word_list = char_list[:]
        new_word_list[i] = char
        new_word =''.join(new_word_list)
        if new_word in DICT:
          print new_word
          neighbors.append(new_word)
  
  return neighbors


def word_ladder(word1,word2):
  '''
    bfs searching for the minimus steps between two words
  '''
  # queue = []
  # neighbors = get_one_letter_neighbors(word1)
  # for new_word in neighbors:
  #   new_neighbors = get_one_letter_neighbors(new_word)
  #   if new_neighbors:
  #     queue.append(new_word)
  queue = []
  queue.append([word1])
  while queue:
    # ['cat']
    path = queue.pop(0)
    if path[-1] == word2:
      return path
    # ['cot', 'bat', 'mat']
    children = get_one_letter_neighbors(path[-1])
    # ['cat', ['cot', 'bat', 'mat']]
    queue.append(path[:] + [children])

  return None


def bfs(initial_state, finish_state, get_child_states):
  queue = []
  queue.append(initial_state)
  while queue:
    state = queue.pop(0)
    if state == finish_state:
      return True
    queue.extend(get_child_states(state))
  return False


def bfs_path(initial_state, finish_state, get_child_states):
  queue = []
  # ['cat']
  queue.append([initial_state])
  while queue:
    # ['cat', 'cot']
    path = queue.pop(0)
    # 'cot'
    if path[-1] == finish_state:
      return path
    for child in get_child_states(path[-1]):
      # 'cot' -> ['cat', 'cot']
      # 'bat' -> ['cat', 'bat']
      # 'mat' -> ['cat', 'mat']
      new_path = path[:]
      new_path.append(child)
      queue.append(new_path)
  return None


word1 = 'cat'
word2 = 'dog'

print word_ladder(word1,word2)