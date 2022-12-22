import pgzrun

WIDTH = 1200
HEIGHT = 500

p = Actor('ironman',(50,50))
rx = random.randint(50, WIDTH-50)
ry = random.randint(50, HEIGHT-50)
c = Actor('cookie_img', (rx, ry)) #cookie

def draw():
    screen.clear()
    p.draw()
    c.draw()

def player_control():
    pass

def handle_score():
    pass

def update():
    pass


pgzrun.go()