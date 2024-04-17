# PROJECT LASER

# Game specific variables
horizontal_movement = True
vertical_movement = True
ship_size = 100, 60
chicken_size = 100, 60
ruffs_size = 142, 160
repair_size = 50, 50
meteoroid_velocity = 5
star1_velocity = 6
star2_velocity = 2
planet_velocity = 1
ship_velocity = 5
enemy_velocity = 3
laser_velocity = 5
repair_velocity = 3
fps = 60

# Importing
import pygame
from pygame.locals import *
import pickle
from random import randint, choice

# Inisialization
pygame.init()
pygame.mixer.init()
font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0 ,255)
yellow = (255, 255, 0)

# Creating window
screen_width = 800
screen_height = 450
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PROJECT LASER')

# Images
cosmos = pygame.image.load('Assets/Sprites/cosmos.png')
cosmos = pygame.transform.scale(cosmos, (screen_width, screen_height)).convert_alpha()

dialog_box = pygame.image.load('Assets/Sprites/dialog-box.png')
dialog_box = pygame.transform.scale(dialog_box, (524, 160)).convert_alpha()

star1 = pygame.image.load('Assets/Sprites/star1.png')
star1 = pygame.transform.scale(star1, (10, 5)).convert_alpha()
star2 = pygame.image.load('Assets/Sprites/star2.png')
star2 = pygame.transform.scale(star2, (5, 5)).convert_alpha()

meteoroid1= pygame.image.load('Assets/Sprites/meteoroid1.png')
meteoroid1 = pygame.transform.scale(meteoroid1, (50, 25)).convert_alpha()
meteoroid2= pygame.image.load('Assets/Sprites/meteoroid2.png')
meteoroid2 = pygame.transform.scale(meteoroid2, (50, 25)).convert_alpha()

mercury = pygame.image.load('Assets/Sprites/mercury.webp')
mercury = pygame.transform.scale(mercury, (200, 200)).convert_alpha()
venus = pygame.image.load('Assets/Sprites/venus.webp')
venus = pygame.transform.scale(venus, (200, 200)).convert_alpha()
earth = pygame.image.load('Assets/Sprites/earth.png')
earth = pygame.transform.scale(earth, (200, 200)).convert_alpha()
jupiter = pygame.image.load('Assets/Sprites/jupiter.png')
jupiter = pygame.transform.scale(jupiter, (200, 200)).convert_alpha()
saturn = pygame.image.load('Assets/Sprites/saturn.png')
saturn = pygame.transform.scale(saturn, (200, 100)).convert_alpha()

laser1 = pygame.image.load('Assets/Sprites/laser1.png')
laser1 = pygame.transform.scale(laser1, (20, 20)).convert_alpha()
laser2 = pygame.image.load('Assets/Sprites/laser2.png')
laser2 = pygame.transform.scale(laser2, (20, 20)).convert_alpha()

space_ship = pygame.image.load('Assets/Sprites/space-ship.png')
space_ship = pygame.transform.scale(space_ship, ship_size).convert_alpha()
chicken = pygame.image.load('Assets/Sprites/chicken.png')
chicken = pygame.transform.scale(chicken, chicken_size).convert_alpha()
ruffs = pygame.image.load('Assets/Sprites/ruffs.png')
ruffs = pygame.transform.scale(ruffs, ruffs_size).convert_alpha()

health_bar = pygame.image.load('Assets/Sprites/health-bar.png')
health_bar = pygame.transform.scale(health_bar, (155,90)).convert_alpha() # Don't cahnge the size
repair = pygame.image.load('Assets/Sprites/repair.png')
repair = pygame.transform.scale(repair, (repair_size[0], repair_size[1])).convert_alpha()

# Sounds
shoot_sound = pygame.mixer.Sound('Assets/Audio/shoot.wav')
explosion_sound = pygame.mixer.Sound('Assets/Audio/explosion.wav')

# Start
def start():
    pygame.mixer.music.load('Assets/Audio/title_screen.mp3')
    pygame.mixer.music.play(-1)
    for i in (1,2,3,2,1,4,5,6,7,8,9,10,11,12,13,14,14,14,13,13,14):
        frame = pygame.image.load(f'Assets/Sprites/start/frame{i}.jpg')
        frame = pygame.transform.scale(frame, (screen_width, screen_height))
        gameWindow.blit(frame, (0,0))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == KEYUP:
                if event.key == K_RETURN:
                    return True
            elif event.type == MOUSEBUTTONUP:
                cord = pygame.mouse.get_pos()
                if screen_width*0.324<=cord[0]<=screen_width*0.6774 and screen_height*0.81334<=cord[1]<=screen_height*0.9:
                    return True
        clock.tick(10)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == KEYUP:
                if event.key == K_RETURN:
                    return True
            elif event.type == MOUSEBUTTONUP:
                cord = pygame.mouse.get_pos()
                if screen_width*0.324<=cord[0]<=screen_width*0.6774 and screen_height*0.81334<=cord[1]<=screen_height*0.9:
                    return True
        clock.tick(fps)

# Game Over
def game_over():
    pygame.mixer.music.load('Assets/Audio/game_over.mp3')
    pygame.mixer.music.play(-1)
    for i in (1,2,3,4,5,6,7,8,9):
        frame = pygame.image.load(f'Assets/Sprites/end/frame{i}.jpg')
        frame = pygame.transform.scale(frame, (screen_width, screen_height)).convert_alpha()
        gameWindow.blit(frame, (0,0))
        update_score()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == MOUSEBUTTONUP:
                cord = pygame.mouse.get_pos()
                if screen_width*0.715<=cord[0]<=screen_width*0.895 and screen_height*0.8175<=cord[1]<=screen_height*0.91:
                    clear()
                    return True
                elif screen_width*0.5175<=cord[0]<=screen_width*0.694 and screen_height*0.8175<=cord[1]<=screen_height*0.91:
                    return False
        clock.tick(10)
        
    A = pygame.image.load('Assets/Sprites/end/frameA.jpg')
    A = pygame.transform.scale(A, (screen_width, screen_height)).convert_alpha() 
    B = pygame.image.load('Assets/Sprites/end/frameB.jpg')
    B = pygame.transform.scale(B, (screen_width, screen_height)).convert_alpha()
    C = pygame.image.load('Assets/Sprites/end/frameC.jpg')
    C = pygame.transform.scale(C, (screen_width, screen_height)).convert_alpha()
    Frame = (A, B, C)
    t = i = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == MOUSEBUTTONUP:
                cord = pygame.mouse.get_pos()
                if screen_width*0.715<=cord[0]<=screen_width*0.895 and screen_height*0.8175<=cord[1]<=screen_height*0.91:
                    clear()
                    return True
                elif screen_width*0.5175<=cord[0]<=screen_width*0.694 and screen_height*0.8175<=cord[1]<=screen_height*0.91:
                    credits()
                    return False
        if fps/(t+1) in (1,1.5,2):
            gameWindow.blit(Frame[i], (0,0))
            i += 1
            if i==len(Frame): i = 0
            update_score()
            pygame.display.update()
        t = tick(t)

# Showing credits when user tries to exit the program
def credits():
    T = t = 0
    for y in range(screen_height, -20, -1):
        if check(): return False
        gameWindow.fill(black)
        gameWindow.blit(font.render('Images and music - SuperCell' , True, white), (screen_width/2-130,y))
        gameWindow.blit(font.render('Coding - Anubhav Jha' , True, white), (screen_width/2-110,y+40))
        pygame.display.update()
        t = tick(t)


# Clear the previous game data
def clear():
    laser1_list.clear()
    laser2_list.clear()
    meteoroid_dict.clear()
    planet_dict.clear()
    enemy_dict.clear()
    repair_dict.clear()

# This fuction will prevent the while loop from going out of control and also regulate time
def tick(t):
    global score, T
    clock.tick(fps)
    t += 1
    if t == fps:
        score += 1
        T += 1
        t = 0
    return t

# This function checks if the user want to quit in between or if the window is out of focus
def check():
    for event in pygame.event.get():
        if event.type == QUIT:
            return True
        elif event.type == WINDOWFOCUSLOST:
            if not pause(): return True

# Navigating to a screen displaying new high score if the previous record was beaten
def new_high_score():
    pygame.mixer.music.load('Assets/Audio/victory1.mp3')
    pygame.mixer.music.play()
    frame = pygame.image.load('Assets/Sprites/new-high-score.png')
    frame = pygame.transform.scale(frame, (screen_width, screen_height))
    gameWindow.blit(frame, (0,0))
    update_score()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == MOUSEBUTTONUP:
                cord = pygame.mouse.get_pos()
                if screen_width*0.33<=cord[0]<=screen_width*0.4665 and screen_height*0.76<=cord[1]<=screen_height*0.834:
                    credits()
                    return False
                elif screen_width*0.5362<=cord[0]<=screen_width*0.675 and screen_height*0.76<=cord[1]<=screen_height*0.834:
                    clear()
                    return True
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load('Assets/Audio/victory2.mp3')
            pygame.mixer.music.play(-1)
        clock.tick(fps)    

# Planets
planet_dict = {}
planet_tuple = (mercury, venus, earth, jupiter, saturn)

def update_planets():
    lst = []
    for p in planet_dict:
        gameWindow.blit(planet_dict[p]['type'], (planet_dict[p]['x'], planet_dict[p]['y']))
        planet_dict[p]['x'] -= planet_velocity
        planet_dict[p]['y'] += d
        if planet_dict[p]['x']<-200:
            lst.append(p)
    if lst:
        for p in lst:
            planet_dict.pop(p)

# Making sure to generate only required no. of stars
if vertical_movement: out = 200
else: out = 0

# Foreground Stars
star1_list = []
for i in range(10, screen_width+1, 100):
    column = []
    for j in range(-out, screen_height+out+1, 100):
        column.append([i+randint(-80,80), j+randint(-80,80)])
    star1_list.append(column)

def update_star1():
    for column in star1_list:
        for i in range(len(column)):
            gameWindow.blit(star1, (column[i][0], column[i][1]))
            column[i][0] -= star1_velocity
            column[i][1] += d
    if star1_list[0][0][0]<0:
        star1_list.pop(0)
        column = []
        for j in range(-out, screen_height+out+1, 100):
            column.append([screen_width+randint(-80,80), j+randint(-80,80)])
        star1_list.append(column)

# Background Stars
star2_list = []
for i in range(0, screen_width+1, 100):
    column = []
    for j in range(-out, screen_height+out+1, 100):
        column.append([i+randint(-80,80), j+randint(-80,80)])
    star2_list.append(column)

def update_star2():
    for column in star2_list:
        for i in range(len(column)):
            gameWindow.blit(star2, (column[i][0], column[i][1]))
            column[i][0] -= star2_velocity
            column[i][1] += d
    if star2_list[0][0][0]<-50:
        star2_list.pop(0)
        column = []
        for j in range(-out, screen_height+out+1, 100):
            column.append([screen_width+randint(-80,80), j+randint(-80,80)])
        star2_list.append(column)

# Laser shoot animation
laser1_list = []
def update_laser1():
    for i in range(len(laser1_list)):
        try:
            if laser1_list[i][0]>screen_width:
                laser1_list.pop(i)
            gameWindow.blit(laser1, (laser1_list[i][0], laser1_list[i][1]))
            
            for e in enemy_dict:
                if enemy_dict[e]['type']==chicken:
                    enemy_rect = pygame.Rect(enemy_dict[e]['x'],enemy_dict[e]['y'] ,chicken_size[0], chicken_size[1])
                elif enemy_dict[e]['type']==ruffs:
                    enemy_rect = pygame.Rect(enemy_dict[e]['x'],enemy_dict[e]['y'] ,ruffs_size[0], ruffs_size[1])
                laser_rect = pygame.Rect(laser1_list[i][0], laser1_list[i][1], 20, 20)            
                if pygame.Rect.colliderect(enemy_rect, laser_rect):
                    enemy_dict[e]['h'] -= 1
                    laser1_list.pop(i)
                    explosion_sound.play()
                    break
            else:
                laser1_list[i] = (laser1_list[i][0]+laser_velocity, laser1_list[i][1])
        except: pass

laser2_list = []
def update_laser2():
    global h
    for i in range(len(laser2_list)):
        try:
            if laser2_list[i][0]<0:
                laser2_list.pop(i)
            gameWindow.blit(laser2, (laser2_list[i][0], laser2_list[i][1]))

            ship_rect = pygame.Rect(ship_x, ship_y, ship_size[0], ship_size[1])
            laser_rect = pygame.Rect(laser2_list[i][0], laser2_list[i][1], 20, 20)                
            if pygame.Rect.colliderect(ship_rect, laser_rect):
                h -= 1
                laser2_list.pop(i)
                explosion_sound.play()
            else:
                laser2_list[i] = (laser2_list[i][0]-laser_velocity, laser2_list[i][1])
        except: pass 

# Points from where meteoroids and enemies can spawn
def spawn(n, space=25):
    "Spawns n number of meteoroids"
    lst1 = [(screen_width, y) for y in range(25, screen_height-49, space)]
    if n >= len(lst1): n = len(lst1)-1
    lst2 = []
    for i in range(n):
        lst3 = [i for i in lst1 if i not in lst2]
        lst2.append(choice(lst3))
    return lst2

# Meteoroids
meteoroid_tuple = (meteoroid1, meteoroid2)
meteoroid_dict = {}
def update_meteoroids():
    global h
    lst = []
    for m in meteoroid_dict:
        ship_rect = pygame.Rect(ship_x, ship_y, ship_size[0], ship_size[1])
        meteoroid_rect = pygame.Rect(meteoroid_dict[m]['x'], meteoroid_dict[m]['y'], 50, 25)
        if pygame.Rect.colliderect(ship_rect, meteoroid_rect):
            h -= 2
            lst.append(m)
            explosion_sound.play()
        else:
            if meteoroid_dict[m]['x'] < -50:
                lst.append(m)
            else:
                gameWindow.blit(meteoroid_dict[m]['type'], (meteoroid_dict[m]['x'], meteoroid_dict[m]['y']))
                meteoroid_dict[m]['x'] -= meteoroid_velocity
    for m in lst:
        meteoroid_dict.pop(m)

# Health bar
def update_health_bar():
    gameWindow.blit(health_bar, (10,-10))
    for i in range(0, h*8, 8):
        pygame.draw.rect(gameWindow, white, [60+i, 30, 6,13])

# Dialog Box (Reusable)
def dialog(str1):
    gameWindow.blit(dialog_box, (0,screen_height-160))
    lst1 = str1.split('\n')
    if   len(lst1)>=4: n = 0
    elif len(lst1)==3: n = 10
    else: n = 20
    for str2 in lst1:
        gameWindow.blit(font.render(str2 , True, white), (170,screen_height-95+n))
        n += 20

# Repair power up to recover lost health
repair_dict = {}
def update_repair():
    global h
    lst = []
    for r in repair_dict:
        repair_rect = pygame.Rect(repair_dict[r]['x'], repair_dict[r]['y'], repair_size[0], repair_size[1])
        ship_rect = pygame.Rect(ship_x, ship_y, ship_size[0], ship_size[1])
        if pygame.Rect.colliderect(ship_rect, repair_rect):
            h += 3
            if h>12: h = 12
            lst.append(r)
        elif repair_dict[r]['x'] < -repair_size[0]:
            lst.append(r)
        else:
            gameWindow.blit(repair, (repair_dict[r]['x'], repair_dict[r]['y']))
            repair_dict[r]['x'] -= repair_velocity
    for r in lst:
        repair_dict.pop(r)

# Our Space-Ship
def update_ship(dialog = False):
    global ship_x, ship_y
    ship_x += velocity_x
    ship_y += velocity_y

    if ship_x>screen_width-ship_size[0]-10: ship_x = screen_width-ship_size[0]-10
    elif ship_x<10: ship_x = 10

    if dialog: height =  screen_height-140  # screen_height-dialog_box_height
    else: height = screen_height
    if ship_y>height-ship_size[1]-10: ship_y = height-ship_size[1]-10
    elif ship_y<10: ship_y = 10

    gameWindow.blit(space_ship, (ship_x, ship_y))

# Enemies
enemy_dict = {}
def update_enemy():
    global h, score
    lst = []
    for e in enemy_dict:
        ship_rect = pygame.Rect(ship_x, ship_y, ship_size[0], ship_size[1])
        if enemy_dict[e]['type']==chicken:
            enemy_rect = pygame.Rect(enemy_dict[e]['x'], enemy_dict[e]['y'], chicken_size[0], chicken_size[1])
        elif enemy_dict[e]['type']==ruffs:
            enemy_rect = pygame.Rect(enemy_dict[e]['x'], enemy_dict[e]['y'], ruffs_size[0], ruffs_size[1])
        if pygame.Rect.colliderect(ship_rect, enemy_rect):
            if enemy_dict[e]['type']==chicken:
                h -= 3
            elif enemy_dict[e]['type']==ruffs:
                h -= 5
            lst.append(e)
            explosion_sound.play()
        else:
            if enemy_dict[e]['x'] < -ruffs_size[0]:
                lst.append(e)
            elif enemy_dict[e]['h']<=0:
                if enemy_dict[e]['type']==chicken:
                    score += 30
                elif enemy_dict[e]['type']==ruffs:
                    score += 100
                lst.append(e)
            else:
                gameWindow.blit(enemy_dict[e]['type'], (enemy_dict[e]['x'], enemy_dict[e]['y']))
                if enemy_dict[e]['direct']=='w':
                    enemy_dict[e]['x'] -= enemy_velocity
                elif enemy_dict[e]['direct']=='n':
                    enemy_dict[e]['y'] -= 1                    
                elif enemy_dict[e]['direct']=='s':
                    enemy_dict[e]['y'] += 1
    for e in lst:        
        enemy_dict.pop(e)


# Generation of meteoroids, enemies and power ups
def generate(T):
    if T%15==0:
        planet_dict[T] = {'type':choice(planet_tuple), 'x':screen_width, 'y':randint(0, screen_height-200)}
    if T%60==0:        
        for x,y in spawn(2,170):
            enemy_dict[f'{T} {y}'] = {'type':ruffs, 'h':10, 'direct':'w', 'x':x+randint(0,300), 'y':y}
    elif T%20==0:
        for x,y in spawn(randint(3,6),70):            
            enemy_dict[f'{T} {y}'] = {'type':chicken, 'h':3, 'direct':'w', 'x':x+randint(0,300), 'y':y}        
    if enemy_dict:
        for e in enemy_dict:
            if enemy_dict[e]['type']==chicken:
                laser2_list.append((enemy_dict[e]['x']+15,enemy_dict[e]['y']+45))
            elif enemy_dict[e]['type']==ruffs:
                laser2_list.append((enemy_dict[e]['x']+50,enemy_dict[e]['y']+140))
            shoot_sound.play()
        if (T+18)%20==0:
            for e in enemy_dict:
                enemy_dict[e]['direct']='n'
        elif (T+16)%20==0:
            for e in enemy_dict:
                enemy_dict[e]['direct']='s'
        elif (T+12)%20==0:
            for e in enemy_dict:
                enemy_dict[e]['direct']='n'
        elif (T+10)%20==0:
            for e in enemy_dict:
                enemy_dict[e]['direct']='w'
                if randint(0,1): repair_dict[T] = {'x':screen_width, 'y':randint(10, screen_height-repair_size[1])}
    elif T%randint(3,4)==0:
        for i in spawn(randint(3,6)):
            meteoroid_dict[f'{T} {i}'] = {'type':choice(meteoroid_tuple), 'x':i[0]+randint(-100,200), 'y':i[1]}

# Pausing the game on will or minimizing the screen
def pause():
    pygame.mixer.music.pause()
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pygame.mixer.music.unpause()
                    return True
            elif event.type == QUIT:
                return False

# Clearing the screen and recreating every image after updating their positions
def refresh(dialog = False):
    if not vertical_movement: d = 0 
    gameWindow.blit(cosmos, (0,0))
    update_star2()
    update_planets()
    update_meteoroids()
    update_enemy()
    update_ship(dialog)
    update_star1()
    update_repair()
    update_laser1()
    update_laser2()
    update_score()
    update_health_bar()

# Score and high score
def update_score():
    global high_score, record_broken
    gameWindow.blit(font.render(f'Score: {score}', True, white), (161,30))
    if high_score<score:
        high_score = score
        record_broken = True
    gameWindow.blit(font.render(f'High Score: {high_score}', True, white), (120,10))

# THE GAME LOOP
def game_loop():

    # Game specific variables
    global star1_velocity, star2_velocity, planet_velocity, T, h, d, score, high_score, record_broken, new_player
    global ship_x, ship_y, velocity_x, velocity_y
    record_broken = False
    ship_x = screen_width/4
    ship_y = screen_height/3
    velocity_x = 0
    velocity_y = 0
    T = t = 0
    d = 0

    if not new_player:
        pygame.mixer.music.load('Assets/Audio/cosmos.mp3')
        pygame.mixer.music.play(-1)
        score = 0
        h = 12
    new_player = False
    
    while True:        
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == WINDOWFOCUSLOST:
                if not pause(): return False

            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key ==K_d:
                    velocity_x = ship_velocity
                    if horizontal_movement:
                        star1_velocity *= 2
                        star2_velocity *= 2
                        planet_velocity *=2
                elif event.key == K_LEFT or event.key ==K_a:
                    velocity_x = -ship_velocity
                    if horizontal_movement:
                        star1_velocity /= 2
                        star2_velocity /= 2
                        planet_velocity /=2
                elif event.key == K_UP or event.key == K_w:
                    velocity_y = -ship_velocity
                    d = 0.5       # Relative upward movement
                elif event.key == K_DOWN or event.key == K_s:
                    velocity_y = ship_velocity
                    d = -0.5      # Relative downward movement
                elif event.key == K_RETURN:
                    laser1_list.append((ship_x+60, ship_y))
                    shoot_sound.play()
                elif event.key == K_SPACE:
                    if not pause(): return False
                        
            elif event.type == KEYUP:
                if event.key == K_RIGHT or event.key ==K_d:
                    if velocity_x > 0: velocity_x = 0
                    if horizontal_movement:
                        star1_velocity /= 2
                        star2_velocity /= 2
                        planet_velocity /=2
                elif event.key == K_LEFT or event.key ==K_a:
                    if velocity_x < 0: velocity_x = 0
                    if horizontal_movement:
                        star1_velocity *= 2
                        star2_velocity *= 2
                        planet_velocity *=2
                elif event.key == K_UP or event.key ==K_w:
                    if velocity_y < 0: velocity_y = 0
                    d = 0
                elif event.key == K_DOWN or event.key ==K_s:
                    if velocity_y > 0: velocity_y = 0
                    d = 0   
          
        refresh()
        pygame.display.update()
        if h<=0:
            pygame.time.delay(1000)
            return True     
        
        clock.tick(fps)
        t += 1
        if t==fps:
            T += 1
            score +=1
            t = 0
            generate(T)

# A one time tutorial for some one runnig this game for the first time
def tutorial():     # Also a gameloop
    
    # Game specific variables
    global star1_velocity, star2_velocity, planet_velocity, T, h, d, score, high_score, record_broken
    global ship_x, ship_y, velocity_x, velocity_y
    score = 0
    record_broken = False
    ship_x = screen_width/4
    ship_y = screen_height/3
    velocity_x = 0
    velocity_y = 0
    h = 12
    T = t = 0
    d = 0

    pygame.mixer.music.load('Assets/Audio/cosmos.mp3')
    pygame.mixer.music.play(-1)

    while T<3:
        refresh()
        pygame.display.update()
        if check(): return False
        t = tick(t)
    
    # Introduction
    T = t = 0
    flag = True
    while flag:
        refresh(True)
        dialog('Welcome to the Cosmos! \nThis is our Space Ship.')
        pygame.display.update()
        t = tick(t)
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == WINDOWFOCUSLOST:
                if not pause(): return False
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if T>0: flag = False
        if T==3: break
    
    # UP
    T = t = 0
    flag = True
    while flag:
        refresh(True)
        dialog('Press and HOLD the "up arrow" key \nor the "W" key to move in the \nupward direction.')
        pygame.display.update()
        t = tick(t)
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == WINDOWFOCUSLOST:
                if not pause(): return False
            elif event.type == KEYDOWN:
                if event.key in (K_UP, K_w):
                    velocity_y = -ship_velocity
                    d = 0.5      # Relative upward movement
            elif event.type == KEYUP:
                if event.key in (K_UP, K_w):
                    if velocity_y < 0: velocity_y = 0
                    d = 0
                    flag = False
        if T==5 and velocity_y==0: break

    # DOWN
    T = t = 0
    flag = True
    while flag:
        refresh(True)
        dialog('Press and HOLD the "down arrow" key \nor the "S" key to move in the \ndownward direction.')
        pygame.display.update()
        t = tick(t)
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == WINDOWFOCUSLOST:
                if not pause(): return False
            elif event.type == KEYDOWN:
                if event.key in (K_DOWN, K_s):
                    velocity_y = ship_velocity
                    d = -0.5      # Relative downward movement
            elif event.type == KEYUP:
                if event.key in (K_DOWN, K_s):
                    if velocity_y > 0: velocity_y = 0
                    d = 0
                    flag = False
        if T==5 and velocity_y==0: break
    
    # RIGHT
    T = t = 0
    flag = True
    while flag:
        refresh(True)
        dialog('Press and HOLD the "right arrow" key \nor the "D" key to move in the \nright direction.')
        pygame.display.update()
        t = tick(t)
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == WINDOWFOCUSLOST:
                if not pause(): return False
            elif event.type == KEYDOWN:
                if event.key in (K_RIGHT, K_d):
                    velocity_x = ship_velocity
                    if horizontal_movement:
                        star1_velocity *= 2
                        star2_velocity *= 2
                        planet_velocity *=2
            elif event.type == KEYUP:
                if event.key in (K_RIGHT, K_d):
                    if velocity_x > 0: velocity_x = 0
                    if horizontal_movement:
                        star1_velocity /= 2
                        star2_velocity /= 2
                        planet_velocity /=2
                    flag = False
        if T==5 and velocity_x==0: break

    # LEFT
    T = t = 0
    flag = True
    while flag:
        refresh(True)
        dialog('Press and HOLD the "left arrow" key \nor the "A" key to move in the \nleft direction.')
        pygame.display.update()
        t = tick(t)
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == WINDOWFOCUSLOST:
                if not pause(): return False
            elif event.type == KEYDOWN:
                if event.key in (K_LEFT, K_a):
                    velocity_x = -ship_velocity
                    if horizontal_movement:
                        star1_velocity /= 2
                        star2_velocity /= 2
                        planet_velocity /=2
            elif event.type == KEYUP:
                if event.key in (K_LEFT, K_a):
                    if velocity_x < 0: velocity_x = 0
                    if horizontal_movement:
                        star1_velocity *= 2
                        star2_velocity *= 2
                        planet_velocity *=2
                    flag = False
        if T==5 and velocity_x==0: break

    # FIRE
    T = t = 0
    flag = True
    while flag:
        refresh(True)
        dialog('Press the "enter" key to fire.')
        pygame.display.update()
        t = tick(t)
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == WINDOWFOCUSLOST:
                if not pause(): return False
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    laser1_list.append((ship_x+60, ship_y))
                    shoot_sound.play()
                    if T>0: flag = False
        if T==5: break
    
    T = t = 0
    while T<10:        
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == WINDOWFOCUSLOST:
                if not pause(): return False

            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_d:
                    velocity_x = ship_velocity
                    if horizontal_movement:
                        star1_velocity *= 2
                        star2_velocity *= 2
                        planet_velocity *=2
                elif event.key == K_LEFT or event.key ==K_a:
                    velocity_x = -ship_velocity
                    if horizontal_movement:
                        star1_velocity /= 2
                        star2_velocity /= 2
                        planet_velocity /=2
                elif event.key == K_UP or event.key == K_w:
                    velocity_y = -ship_velocity
                    d = 0.5       # Relative upward movement
                elif event.key == K_DOWN or event.key == K_s:
                    velocity_y = ship_velocity
                    d = -0.5      # Relative downward movement
                elif event.key == K_RETURN:
                    laser1_list.append((ship_x+60, ship_y))
                    shoot_sound.play()
                elif event.key == K_SPACE:
                    if not pause(): return False
                        
            elif event.type == KEYUP:
                if event.key == K_RIGHT or event.key ==K_d:
                    if velocity_x > 0: velocity_x = 0
                    if horizontal_movement:
                        star1_velocity /= 2
                        star2_velocity /= 2
                        planet_velocity /=2
                elif event.key == K_LEFT or event.key ==K_a:
                    if velocity_x < 0: velocity_x = 0
                    if horizontal_movement:
                        star1_velocity *= 2
                        star2_velocity *= 2
                        planet_velocity *=2
                elif event.key == K_UP or event.key ==K_w:
                    if velocity_y < 0: velocity_y = 0
                    d = 0
                elif event.key == K_DOWN or event.key ==K_s:
                    if velocity_y > 0: velocity_y = 0
                    d = 0
        if T in (3,4,5):
            refresh(True)
            dialog('U can also use two keys at once \nto move diagonaly.')
        else:
            refresh()
        pygame.display.update()
        t = tick(t)

    # Healht Bar
    gameWindow.fill(black)
    update_health_bar()
    dialog('This is the health bar \nof our space ship. \nIt has 12 units.')
    pygame.display.update()
    T = t = 0
    flag = True
    while flag:
        t = tick(t)
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == WINDOWFOCUSLOST:
                if not pause(): return False
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if T>0: flag = False
        if T==5: break

    # Score and High-Score
    T = t = 0
    flag = 2
    while flag:
        t = tick(t)
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == WINDOWFOCUSLOST:
                if not pause(): return False
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if T>0: 
                        flag -= 1
                        T = 0
        gameWindow.fill(black)
        if   flag==2:
            dialog('The "Score" displays our current score \nand the "high score" is the hightest \nscore record which you have to beat :)')           
        elif flag==1:
            dialog('Your Score increases every second \nyou survive and also by destroying \nthe enemies...')           
        if T==5:
            flag -= 1
            T = 0
        update_score()
        pygame.display.update()
    
    # DEMO MODE
    T = t = 0
    flag = True
    ship_x = screen_width/4
    ship_y = screen_height/3
    while flag:
        refresh(True)
        if T<=3: dialog('I will show you a Demo. \nYour controls are turned off.')
        pygame.display.update()
        t = tick(t)
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == WINDOWFOCUSLOST:
                if not pause(): return False
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if T>0: flag = False
        if T==5: break

    # Meteoroids
    meteoroid_dict['m1'] = {'type':choice(meteoroid_tuple), 'x':screen_width, 'y':ship_y}
    T = t = 0
    while True:
        refresh()
        pygame.display.update()
        t = tick(t)
        if T==1: break

    gameWindow.fill(black)
    update_meteoroids()
    update_ship()
    dialog('This Meteoroid can harm the Space \nShip. They are too rigid,  we can\'t \ndistroy them from our laser gun. \nWe must dodge it.')
    pygame.display.update()
    flag = True
    while flag:
        t = tick(t)
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == WINDOWFOCUSLOST:
                if not pause(): return False
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if T>0: flag = False
        if T==7: break

    T = t = 0    
    while True:                        

        if   T==0 and fps/(t+1) >= 4: ship_y -= ship_velocity
        elif T==2 and fps/(t+1) >= 2: ship_y += ship_velocity

        if t==0 and T==1:
            meteoroid_dict['m2'] = {'type':choice(meteoroid_tuple), 'x':screen_width, 'y':ship_y}
        elif fps/(t+1)==2 and T==1:
            meteoroid_dict['m3'] = {'type':choice(meteoroid_tuple), 'x':screen_width, 'y':ship_y+50}
        elif meteoroid_dict == {}: break

        if check(): return False
        refresh()
        pygame.display.update()
        t = tick(t)

    # Enemies

    while True:    
        if (ship_x, ship_y) ==  (screen_width/4, screen_height/3): break
        else:
            if  ship_x<screen_width/4:
                ship_x += ship_velocity
            elif ship_x>screen_width/4:
                ship_x -= ship_velocity
            if  ship_y<screen_height/3:
                ship_y += ship_velocity
            elif ship_y>screen_height/3:
                ship_y -= ship_velocity

        refresh()
        pygame.display.update()
        t = tick(t)
        if check(): return False

    enemy_dict['e1'] = {'type':chicken, 'h':3, 'direct':'w', 'x': screen_width, 'y': screen_height/2-chicken_size[1]-20}
    enemy_dict['e2'] = {'type':ruffs, 'h':10, 'direct':'w', 'x': screen_width, 'y': screen_height/2}
    T = t = 0
    while True:
        refresh()
        pygame.display.update()
        t = tick(t)
        if check(): return False
        if t==0:
            for e in enemy_dict:
                if enemy_dict[e]['type']==chicken:
                    laser2_list.append((enemy_dict[e]['x']+15,enemy_dict[e]['y']+45))
                elif enemy_dict[e]['type']==ruffs:
                    laser2_list.append((enemy_dict[e]['x']+50,enemy_dict[e]['y']+140))
                shoot_sound.play()
        if T==1 and fps/(t+1)==2: break        
  
    T = t = 0
    gameWindow.fill(black)
    update_enemy()
    update_laser2()
    update_ship()
    flag = 2

    while flag:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == WINDOWFOCUSLOST:
                if not pause(): return False
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    T = 1 #
                    if T>0:
                        flag -= 1
                        T = t = 0
        
        if flag == 2:
            dialog('Thses are your enemies, they \nshoot laser beams, try to dodge them. \nAnd don\'t collide with them, \nspecialy with the big one.')
        elif flag == 1:
            dialog('You can shift your lane and \navoid taking damage or shoot at \nthem to destroy them to get points.')
        if T==7:
            flag -= 1
            T = t = 0
        pygame.display.update()
        t = tick(t)

    T = 1
    t = fps//2
    while True:
        t = tick(t)
        if t==0:
            for e in enemy_dict:
                if enemy_dict[e]['type']==chicken:
                    laser2_list.append((enemy_dict[e]['x']+15,enemy_dict[e]['y']+45))
                elif enemy_dict[e]['type']==ruffs:
                    laser2_list.append((enemy_dict[e]['x']+50,enemy_dict[e]['y']+140))
                shoot_sound.play()
            if (T+18)%20==0:
                for e in enemy_dict:
                    enemy_dict[e]['direct']='n'
            elif (T+16)%20==0:
                for e in enemy_dict:
                    enemy_dict[e]['direct']='s'
            elif (T+12)%20==0:
                for e in enemy_dict:
                    enemy_dict[e]['direct']='n'
            elif (T+10)%20==0:
                for e in enemy_dict:
                    enemy_dict[e]['direct']='w'

        if T==1:
            ship_x -= ship_velocity
            ship_y += ship_velocity
        if T<6:
            if   fps/(t+1) > 2: ship_y += ship_velocity
            elif fps/(t+1) > 1: ship_y -= ship_velocity
            if fps/(t+1) in (3,1.5,1):
                laser1_list.append((ship_x+60, ship_y))
                shoot_sound.play()

        if check(): return False
        if enemy_dict=={}: break
        refresh()
        pygame.display.update()  

    # Repair Power Up
    repair_dict['r1'] = {'x':screen_width, 'y':randint(10, screen_height-repair_size[1])}
    repair_dict['r2'] = {'x':screen_width+200, 'y':randint(10, screen_height-repair_size[1])}
    T = t = 0
    while T==0:
        refresh()
        pygame.display.update()
        t = tick(t)
    gameWindow.fill(black)
    update_repair()
    update_ship()
    dialog('This is a repair power up. \nTaking it will retrieve your health.')
    pygame.display.update()
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == WINDOWFOCUSLOST:
                if not pause(): return False
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if T>0: flag = False
        t = tick(t)
        if T==6: break
    
    while True:
        if repair_dict=={}:
            break
        else:
            r = tuple(repair_dict)[0]
            if  ship_y < repair_dict[r]['y'] and abs(ship_y-repair_dict[r]['y'])>=ship_velocity:
                ship_y += ship_velocity
            elif ship_y > repair_dict[r]['y'] and abs(ship_y-repair_dict[r]['y'])>=ship_velocity:
                ship_y -= ship_velocity
            elif ship_x < repair_dict[r]['x'] and abs(ship_x-repair_dict[r]['x'])>=ship_velocity:
                ship_x += ship_velocity
            elif ship_x > repair_dict[r]['x'] and abs(ship_x-repair_dict[r]['x'])>=ship_velocity:
                ship_x -= ship_velocity
        refresh()
        pygame.display.update()
        clock.tick(fps)       
 
    # Ending the tutorial
    
    while True:      

        if (ship_x, ship_y) ==  (screen_width/4, screen_height/3): break
        else:
            if  ship_x<screen_width/4:
                ship_x += ship_velocity
            elif ship_x>screen_width/4:
                ship_x -= ship_velocity
            if  ship_y<screen_height/3:
                ship_y += ship_velocity
            elif ship_y>screen_height/3:
                ship_y -= ship_velocity

        refresh()
        pygame.display.update()
        t = tick(t)
        if check(): return False
    
    T = t = 0
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == WINDOWFOCUSLOST:
                if not pause(): return False
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if T>0: flag = False
        if T==5: break
        refresh()
        dialog('You are ready to take the Lead!')
        pygame.display.update()
        t = tick(t)

    return True      
    

if start():
    # Storing information in a binary file called data.txt
    try:
        with open('Data/data.dat', 'rb') as f:
            high_score = pickle.load(f)
            new_player = pickle.load(f)
    except Exception:
        high_score = 0
        new_player = True

    while True:
        if new_player:
            if not tutorial():
                break
        if not game_loop():
            break
        if record_broken:
            if not new_high_score():
                break
        elif not game_over():
            break
    with open('Data/data.dat', "wb") as f:
        pickle.dump(high_score, f)
        pickle.dump(new_player, f)

    pygame.quit()
