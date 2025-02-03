# l=[11,22,33,44,66]
# for i in l:
#     if i%2==1:
#         print(i)
# l=[11,22,33,44,66]
# l=[i for i in l if i%2==0]
# print(l)



# n=5
# stars=1
# spaces=n-1
# for i in range(1,n+1):
#     for j in range(1,spaces+1):
#         print('',end='')
#     for k in range(1,stars+1):
#         print('*',end=' ')
#     print()
#     spaces+=2
#     stars+=1


# a=[10,20,30]
# b=[40,50]
# a=zip(a,b)
# print(set(a))


# from itertools import zip_longest
# a=set(zip_longest('abc',[10,20],fillvalue=0))
# print(a)

# import re
# s='hai123@&.com'
# re.findall(' ',s)
# print(s)
# import re
s='hai hp heep hep heeep heap'
a=re.findall('^e',s)
print(a) 

