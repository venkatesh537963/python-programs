# from functools import reduce
# L=[11,22,30,44,5]
# print(reduce(lambda x,y:x if x>y else y,L))




from functools import reduce
L=[[11,22],[30,44],[90,5]]
print(reduce (lambda x,y:x+y,L))