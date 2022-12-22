

from re import X
#print (x.index (22)) #value error
z = x  # not a good idea, it's a reference
y = x.copy()
z.append(10)
y.append(20)
print(x is z)
print(x is y)
print(x)
print(y)
print(z)
