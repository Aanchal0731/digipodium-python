import pgzrun

HEIGHT = 500
WIDTH = 800

def draw():
    #fill the images on the screen at (100,100) coordinates
    screen.fill("blue")
    #display the image on the screen at(100,100)
    screen.blit('ironman',(100, 100))

pgzrun.go()