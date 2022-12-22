a = {'Ram','Shyam','Hari','geeta','seeta'}
b = {'tom','sen','soozi','john','alex'}
c = {'Ram','Alex','Gita','Tanya','Sergri'}

#union

ab = a|b
print("union=>", ab)
#or
ab = a.union(b)
print("union=>", ab)

#intersection
ac = a & c #a.intersection(c) also works
print('intersection=>', ac)

abi = a & b
print('intersection=>', abi)

#difference
ac = a - c #difference(c) also works
print('difference=>', ac)


ca = c-a 
print('differnece=>', ca)

#symmetric difference
ac = a ^ c
print('symmetric difference=>', ac)  