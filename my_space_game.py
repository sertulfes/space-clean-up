#space junk game
#importing libraries
import pgzrun
import random
import time

WIDTH = 1000 #width of window
HEIGHT = 600 #length of window
SCOREBOX_HEIGHT = 90

#background and sprites
BACKGROUND_IMG = "space_background"
PLAYER_IMG = "player"
JUNK_IMG = "space_junk"
SATELLITE_IMG = "satellite_two"
DEBRIS_IMG = "space_debris"
CAR_IMG = "tesla_roadster"
LASER_IMG = "laser_red"

#sprites
player = Actor(PLAYER_IMG)
player.midright = (1000, 300)
junk = Actor(JUNK_IMG)
sat = Actor(SATELLITE_IMG)
deb = Actor(DEBRIS_IMG)
car = Actor(CAR_IMG)

#satellite position
x_sat = random.randint(-500, -50)
y_sat = random.randint(SCOREBOX_HEIGHT, HEIGHT - sat.height)
sat.topright = (x_sat, y_sat)

#debris position
x_deb = random.randint(-500, -50)
y_deb = random.randint(SCOREBOX_HEIGHT, HEIGHT - deb.height)
deb.topright = (x_deb, y_deb)

#car position
x_car = random.randint(-500, -50)
y_car = random.randint(SCOREBOX_HEIGHT, HEIGHT - car.height)
car.topright = (x_car, y_car)

#make more junk
junks = []
for i in range(7):
    junk = Actor(JUNK_IMG)

    #random junk position
    x_pos = random.randint(-500, -50)
    y_pos = random.randint(SCOREBOX_HEIGHT, HEIGHT - junk.height)
    junk.topright = (x_pos, y_pos)

    #adding junk and making random speed
    junk.junk_speed = random.randint(4,10)
    junks.append(junk)

#laser list
lasers = []

#start time
start_time = time.time()

#update everything
def update():
    
    #timer
    global start_time, elp_time

    if(score >= 0) and (score < 150):
        current_time = time.time()
        elp_time = current_time - start_time

        #updating
        updatePlayer()
        updateJunk()
        updateSat()
        updateDeb()
        updateCar()
        updateLasers()

#score
score = 0

#background music
sounds.space_music_suspense.play(-1)

#to update the player
def updatePlayer():

    #to move up
    if(keyboard.up == 1 and player.top > 90):
        player.y += -7
        
    #to move down
    elif(keyboard.down == 1 and player.bottom < 600):
        player.y += 7

    #fire laser
    elif(keyboard.space == 1):
        laser = Actor(LASER_IMG)
        laser.midright = (player.midleft)
        fireLasers(laser)

#junk speed
junk_speed = random.randint(4,8)

#to update junk
def updateJunk():
    global score, junk_speed

    #make more junks
    for junk in junks:

        #make junk move itself
        junk.x += junk.junk_speed

        #collision variable
        collision = player.colliderect(junk)
        
        #puts junk back on right side
        if(junk.left > 1000) or (collision == 1):

            #makes position
            x_pos = -50
            y_pos = random.randint(SCOREBOX_HEIGHT, HEIGHT - junk.height)
            junk.topleft = (x_pos, y_pos)

        #collisions
        if(collision == 1):

            #adding score
            score += 1
            
            #sound effect
            sounds.collect_pep.play(1)

#to update satilites

#speed of satellite
sat_speed = 5
def updateSat():
    global score, sat_speed

    #make satellite move
    sat.x += sat_speed

    #satellite collision variable and speed
    sat_speed = random.randint(4,6)
    collision = player.colliderect(sat)

    if(sat.left > 1000) or (collision == 1):

        #satellite position
        x_sat = random.randint(-500, -50)
        y_sat = random.randint(SCOREBOX_HEIGHT, HEIGHT - sat.height)
        sat.topright = (x_sat, y_sat)

    #collisions satellite
    if(collision == 1):

        #taking score
        score += -3

        #sound effect
        sounds.explosion.play(1)

#to update debris

#speed of debris
deb_speed = 5
def updateDeb():
    global score, deb_speed

    #debris speed
    deb.x += deb_speed

    #debris collision variable and speed
    deb_speed = random.randint(4,6)
    collision = player.colliderect(deb)

    if(deb.left > 1000) or (collision == 1):

        #debris position
        x_deb = random.randint(-500, -50)
        y_deb = random.randint(SCOREBOX_HEIGHT, HEIGHT - deb.height)
        deb.topright = (x_deb, y_deb)

    #collisions
    if(collision == 1):

        #points
        score += -3

        #sound effect
        sounds.explosion.play(1)

#update car

#speed of car
car_speed = 5
def updateCar():
    global score, car_speed

    #car speed
    car.x += car_speed

    #car collision variable and speed
    car_speed = random.randint(5,7)
    collision = player.colliderect(car)

    if(car.left > 1000) or (collision == 1):

        #car position
        x_car = random.randint(-500, -50)
        y_car = random.randint(SCOREBOX_HEIGHT, HEIGHT - car.height)
        car.topright = (x_car, y_car)

    #collisions
    if(collision == 1):

        #points
        score += 3

        #sound effect
        sounds.collect_pep.play(1)

def updateLasers():
    global score

    #making lasers move
    for laser in lasers:
        laser.x += -8

        #collision variables
        collision_sat = sat.colliderect(laser)
        collision_deb = deb.colliderect(laser)
        collision_car = car.colliderect(laser)

        #making laser dissapear
        if(laser.right < 0) or (collision_sat == 1) or (collision_deb == 1) or (collision_car == 1):
            lasers.remove(laser)

        #satellite collisions
        if(collision_sat == 1):

            #reposition
            x_sat = random.randint(-500, -50)
            y_sat = random.randint(SCOREBOX_HEIGHT, HEIGHT - sat.height)
            sat.topright = (x_sat, y_sat)

            #score
            score += -3

            #sound effect
            sounds.explosion.play(1)

        #debris collisions
        if(collision_deb == 1):

            #reposition
            x_deb = random.randint(-500, -50)
            y_deb = random.randint(SCOREBOX_HEIGHT, HEIGHT - deb.height)
            deb.topright = (x_deb, y_deb)

            #score
            score += 3

            #sound effect
            sounds.explosion.play(1)

        #debris collisions
        if(collision_car == 1):

            #reposition
            x_car = random.randint(-500, -50)
            y_car = random.randint(SCOREBOX_HEIGHT, HEIGHT - car.height)
            car.topright = (x_car, y_car)

            #score
            score += 3

            #sound effect
            sounds.explosion.play(1)

# activating lasers 
player.laserActive = 1  # add laserActive status to the player

def makeLaserActive():  # when called, this function will make lasers active again
    global player
    player.laserActive = 1

def fireLasers(laser):
    if player.laserActive == 1:  # active status is used to prevent continuous shoot when holding space key
        player.laserActive = 0
        clock.schedule(makeLaserActive, 0.2)  # schedule an event (function, time afterwhich event will occur)
        sounds.laserfire02.play()  # play sound effect
        lasers.append(laser)  # add laser to lasers list
          
#to show on screem
def draw():
    screen.clear()

    #background
    screen.blit(BACKGROUND_IMG, (0,0,))

    #putting player on screen
    player.draw()

    #putting satellite on screen
    sat.draw()

    #putting debris on screen
    deb.draw()

    #putting car on screen
    car.draw()

    #putting junk on screen
    for junk in junks:
        junk.draw()

    #putting lasers on screen
    for laser in lasers:
        laser.draw()

    #instructions
    ins = "Touch rocks and cars. Shoot broken satellites and cars."
    ins_2 = "Don't shoot good satelites. Don't touch good or bad satellites."
    screen.draw.text(ins, topleft=(400, 5), fontsize=20, color="yellow")
    screen.draw.text(ins_2, topleft=(400, 20), fontsize=20, color="yellow")

    #game over
    if (score < 0):
        show_game_over = "GAME OVER"
        screen.draw.text(show_game_over, center=(WIDTH/2,HEIGHT/2), fontsize=100, color="red", ocolor='white', owidth=0.5)

    #game win
    if (score >= 150):
        win = "YOU WIN!"
        screen.draw.text(win, center=(WIDTH/2,HEIGHT/2), fontsize=100, color="orange", ocolor='white', owidth=0.5)

    #timer
    timer = "Time: " + str(elp_time)
    screen.draw.text(timer, topleft=(896,42), fontsize=45, color="orange")
        
    #showing score on screen
    show_score = "Score: " + str(score)
    screen.draw.text(show_score, topleft=(880,15), fontsize=35, color="white")

pgzrun.go() #runs game loop
