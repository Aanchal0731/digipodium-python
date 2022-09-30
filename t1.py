from turtle import *

speed ('slowest')
for i in range (10):
    fd(72)
    lt(360/10)



    #pentagon
    side = 5
    for i in range(side):
        fd(-54)
        lt(360/side)
        dot(side*3)
        pensize(6)
        pencolor('Blue')
        circle(side*10)
        pencolor('green')


    mainloop()

