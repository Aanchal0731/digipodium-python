evens = 0

While True :
    num = input("Enter a number")
    if not num:
        break
    if not num.isnumeric():
        continue
    num = int(num)
    if num % 2 ==0:
        evens =+ num

      