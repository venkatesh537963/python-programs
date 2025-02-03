'''


# collection of charcters


# '''
# b='venkatesh'
# a="venkatesh"
# c='''venkatesh'''
# print(type(b),type(a),type(c))

# using reduce to compute minimum element from list
from functools import reduce
L=[11,22,33,44,5]
print(reduce(lambda x,y:x if x<y else y,L))