'''
Swaps the keys and values in a dictionary.
'''

a = {
    'a': 1,
    'b': 2,
    'c': 3,
}
b = dict((value,key) for (key,value) in a.iteritems())

print a
print b