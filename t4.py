from turtle import *

speed  ('fastest')
i = 1
while True:
    fd(10 + i)
    lt(360/6) 
    i += 2 
    write(i)
    if i > 500:
        break
mainloop()