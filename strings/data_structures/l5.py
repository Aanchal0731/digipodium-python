#wap to add 10 numbers in a list by user input

num = []        #blank list
for i in range (10):
    data = input("Enter a number: ")
    if data.isnumeric():
        num.append(int(data))

print("your data => ", num)

#wap to take 10 float numbers from user and store them in list

x = []
for i in range(10):
    data = input('Enter a Float value: ')
    if '.' in data and data.count('.')  == 1:
        p1,p2 = data.split('.')
        if p1.isnumeric() and p2.isnumeric():
            x.append(float(data))
    if data.isnumeric():
        x.append(float(data))
print(x)