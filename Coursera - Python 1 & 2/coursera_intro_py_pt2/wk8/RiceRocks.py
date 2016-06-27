# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
rock_time = 0
time = 0
started = False
rock_vel = [1, 1]
ANG_VEL = .05
FRIC_CONST = .01
ACCEL_CONST = .2
MISS_CONST = 7.5

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# load 64 frame sprite sheer for asteroid - image source is opengameart, artist is warspawn 
ROCK_CENTER = [64, 64]
ROCK_SIZE = [128, 128]
ROCK_DIM = 64
rock_info = ImageInfo(ROCK_CENTER, ROCK_SIZE, 40)
rock_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid1.opengameart.warspawn.png")


# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
EXPLOSION_CENTER = [64, 64]
EXPLOSION_SIZE = [128, 128]
EXPLOSION_DIM = [9, 9]
explosion_info = ImageInfo(EXPLOSION_CENTER, EXPLOSION_SIZE, 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.sound = ship_thrust_sound
 
        
    def rotate_lf(self, av_inc):
        self.angle_vel -= av_inc
        
    def rotate_rt(self, av_inc):
        self.angle_vel += av_inc
        
    def thrusters_on(self):
        self.thrust = True
        
        #thruster sound
        self.sound.rewind()
        self.sound.play()

    def thrusters_off(self):
        self.thrust = False
        self.sound.pause()
        
    def shoot(self):
        global missile_group
        missile_group.add(Sprite([my_ship.pos[0] + (angle_to_vector(my_ship.angle)[0] * my_ship.radius), 
                                  (my_ship.pos[1] + (angle_to_vector(my_ship.angle)[1] * my_ship.radius))], 
                                 [my_ship.vel[0] + (angle_to_vector(my_ship.angle)[0] * MISS_CONST), 
                                  my_ship.vel[1] + (angle_to_vector(my_ship.angle)[1] * MISS_CONST)], 
                                 my_ship.angle, 40, missile_image, missile_info, missile_sound))
        
    def draw(self,canvas):
        if self.thrust == False:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, [self.image_center[0] + (self.image_size[0]), self.image_center[1]], self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0])  % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1])  % HEIGHT
        
        for k in range(2):
            self.vel[k] *= (1 - FRIC_CONST)
        
        if self.thrust:
            for i in range(2):
                self.vel[i] += angle_to_vector(self.angle)[i] * ACCEL_CONST
                
    def get_position(self):
        return self.pos
   
    def get_radius(self):
        return self.radius
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        global time
        global rock_time
        explosion_index = [time % EXPLOSION_DIM[0], (time // EXPLOSION_DIM[0]) % EXPLOSION_DIM[1]]
        if self.animated == True:
            canvas.draw_image(explosion_image, 
                    [EXPLOSION_CENTER[0] + explosion_index[0] * EXPLOSION_SIZE[0], 
                     EXPLOSION_CENTER[1] + explosion_index[1] * EXPLOSION_SIZE[1]], 
                     self.image_size, self.pos, self.image_size, self.angle)
            time += 1       
        
        elif self.lifespan == 50:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
        else:
            current_rock_index = (rock_time % ROCK_DIM) // 1
            current_rock_center = [ROCK_CENTER[0] +  current_rock_index * ROCK_SIZE[0], ROCK_CENTER[1]]
            canvas.draw_image(rock_image, current_rock_center, self.image_size, self.pos, self.image_size, self.angle) 
            rock_time += .07
            
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0])  % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1])  % HEIGHT 
        self.age += 1
        if self.age >= self.lifespan:
            return True
        else:
            return False
            
        
    def collide(self, other_object):
         if dist(self.pos, other_object.get_position()) <= self.radius + other_object.get_radius():
            return True
        
    def get_position(self):
        return self.pos
   
    def get_radius(self):
        return self.radius        

# define keyhandlers to control ship rotation
def keydown(key):   
    if simplegui.KEY_MAP["left"] == key:
        my_ship.rotate_lf(ANG_VEL)
    elif simplegui.KEY_MAP["right"] == key:
        my_ship.rotate_rt(ANG_VEL)
    elif simplegui.KEY_MAP["up"] == key:
        my_ship.thrusters_on()
    elif simplegui.KEY_MAP["space"] == key:
        my_ship.shoot()
    

def keyup(key):
    if simplegui.KEY_MAP["left"] == key:
        my_ship.rotate_rt(ANG_VEL)
    elif simplegui.KEY_MAP["right"] == key:
        my_ship.rotate_lf(ANG_VEL)
    elif simplegui.KEY_MAP["up"] == key:
        my_ship.thrusters_off()
               
# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, lives, score, my_ship
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
    lives = 3
    score = 0
    timer.start()
    my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)

    
# draw handler
def draw(canvas):
    global time, started, lives, score, rock_vel, rock_group, missile_group
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    
    # draw ship and sprites
    my_ship.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
   
    # call the process_sprite_group function on rock_group
    process_sprite_group(rock_group, canvas)
    
    # call the process_sprite_group function on missile_group
    process_sprite_group(missile_group, canvas)
    
    # call the process_sprite_group function on explosion_group
    process_sprite_group(explosion_group, canvas)
    
    # determine if the ship hit any rocks
    if group_collide(rock_group, my_ship):
        lives -= 1
        
    #call function to detect missile/rock collisions / increment score by number of missile collisions
    score += group_group_collide(missile_group, rock_group)
    for v in rock_vel:
        v *= score * .05
    
    # lives and score
    canvas.draw_text('Lives', (WIDTH / 27, HEIGHT / 14), 24, 'White', 'monospace')
    canvas.draw_text(str(lives), (WIDTH / 27, HEIGHT / 8.5), 24, 'White', 'monospace')
    canvas.draw_text('Score', (WIDTH / 1.13, HEIGHT / 14), 24, 'White', 'monospace')
    canvas.draw_text(str(score), (WIDTH / 1.13, HEIGHT / 8.5), 24, 'White', 'monospace')

    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
    if lives == 0:
        started = False
        timer.stop()
        for r in rock_group:
            rock_group.discard(r)
             
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group, ang_vel, rock_vel, started, score
    rock_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
    rock_vel = [random.randint(-2, 2), random.randint(-2, 2)]
    rock_ang_vel = (random.random() * .1 + (-.02))
    rock_sprite = Sprite(rock_pos, rock_vel, 4, rock_ang_vel, rock_image, rock_info)
    if len(rock_group) < 12:
        rock_group.add(rock_sprite)
        if dist(rock_sprite.get_position(), my_ship.get_position()) <= rock_sprite.get_radius() + my_ship.get_radius():
            rock_group.discard(rock_sprite)
           
            
# take a set and a canvas and call the update and draw methods for each sprite in the group
def process_sprite_group(set, canvas):
    for s in list(set):
        s.draw(canvas)
        if s.update() == True:
            set.remove(s)
           
def group_collide(rgroup, other_object):
    for e in list(rgroup):
        if e.collide(other_object) == True:
            expl_sprite = Sprite(e.get_position(), e.vel, e.angle, e.angle_vel, explosion_image, explosion_info)
            explosion_group.add(expl_sprite)
            explosion_sound.play()
            rgroup.remove(e)
            return True
        
def group_group_collide(group1, group2):
    g_o_collisions = 0
    for g_o in list(group1):
        if group_collide(group2, g_o) == True:
            g_o_collisions += 1
            group1.discard(g_o)
    return g_o_collisions
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set([])
missile_group = set([])
explosion_group = set([])

# play soundtrack
soundtrack.play()
soundtrack.set_volume(0.7)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_mouseclick_handler(click)
frame.set_keyup_handler(keyup)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling

frame.start()