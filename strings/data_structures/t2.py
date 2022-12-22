x = 1,2,3,3,54,5
print(x)
print(type(x))

#assignment in python
a,b = 10,20 # 2 values are stored in two variables 
print(a,b)
a = 10 ,20 # 2 values are stored in 1 var
print(a, type(a))

#special case
x, x2,x3,*y = 1,2,3,3,54,5    # 1 value is stored in x and rest are stored in y as a list
print(x,x2,x3,y)
print(type(x),type(y)) 

#concatenation 
print((1,2,3)+(1,2,3))


#Repeat
print(("repeat",)*3)

my_tuple = ('a','p','p','l','e')
print(my_tuple.count('p'))  
print(my_tuple.index('l'))