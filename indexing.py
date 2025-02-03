# # def even(n):
# #     return n%2==0
# # l=[11,22,33,44]
# # print(tuple(filter(even,l)))



# # adding=lambda x,y:x*y
# # print(adding(10,20))




# #map with normal function
# def addition (n):
#     return n+10
# print(list(map(addition,[11,22,33,40])))




# def even(n):
#     return n%2 == 0
# l=[11,22,33,10,46]
# print(tuple(filter(even,l)))


# from functools import reduce

# L=[11,22,30,44,55]
# print(reduce (lambda x,y:x+y,L))

#ternary operator

from functools import reduce
L=[11,22,30,44,5]
print(reduce(lambda x,y:x if x>y else y,L))