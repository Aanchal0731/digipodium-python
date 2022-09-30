m = "This is an example"
print (len(m))
for a,b in enumerate(m):
    print(f'{a} --> {b}')

#slicing 
print(m[5:7]) # is
print(m[8:10]) # an
print(m[0:5]) #this

#getting a slice
s = 'digipodium'
slice1 = s[0:4]  # 0 to 4th char
slice2 = s[:4] # 0 to 4th char 
print(slice1)
print(slice2)

s = 'digipodium'
slice1 = s[4:len(s)]  # 4 to 0 char
slice2 = s[4:] # 4 to end char 
print(slice1)
print(slice2)

#slicing 2
print(m[:7])
print(m[-11:])
print(m[8:14])

amt = '$3000'
print(int(amt[1:]))


rr = '1,143 ratings  | 347 answered questions'
print ("total answers", rr[15:])
print("no of rating", rr[:12])

