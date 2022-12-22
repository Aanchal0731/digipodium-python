import pgzrun


HEIGHT = 500
WIDTH = 800

p = Actor('ironman', (100,100))   #actor is a class
z = Actor('zombie', (700,400))
f = Actor('frog',(600,400))

def draw():  #defining a fn dt is draw()
    screen.fill('black')
    p.draw()
    z.draw()
    f.draw()

def update():
    print(p.pos, z.pos)
    print(p.pos, f.pos)
    #player control
    if keyboard.left:
        p.x -= 5
        p.angle = 10
        sounds.bomb.play()
    elif keyboard.right:
        p.x += 5
        p.angle = -10
    elif keyboard.up:
        p.y -= 5
    elif keyboard.down:
        p.y += 5
    elif keyboard.SPACE:
        p.angle = 360
    else:
        p.angle = 0
        

    #zombie control
    if p.x > z.x:
        z.x += 1
    if p.y > z.y:
        z.y += 1
    if p.x < z.x:
        z.x -= 1
    if p.y < z.y:
        z.y -= 1
    #if p.zombie(z):
        #exit()

    
    #frog control
    if f.x > f.x:
        f.x += 1
    if f.y > f.y:
        f.y += 1
    if f.x < f.x:
        f.x -= 1
    if f.y < f.y:
        f.y -= 1



pgzrun.go()
