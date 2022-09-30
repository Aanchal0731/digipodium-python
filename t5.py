from turtle import *
outside = 3
inside = 3



speed  ('fastest')
i = 1
while True:
    fd(10+i)
    for j in range(6):
        fd(i)
        lt(360/6)

    lt(360/6)
    
    i += 2 
    write(i)
    if i > 100:
        break
mainloop()