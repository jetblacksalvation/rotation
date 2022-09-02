import pygame
import math
#

pygame.init()
screen = pygame.display.set_mode([1000,1000])

pi = math.pi;
#point that you draw
x =550
y= 550
#virtual point, we dont want x or y to actually change
pp_x = 0
pp_y= 0

#your position
px = 500
py = 500
pp_ang = 0

A=0
D=1
W = 2
S = 3
E = 4
Q = 5
keys = [False, False, False, False, False, False]

angle = pi#rotates the thing to opposite

#you have to get the tan of this shape


def rel_angl():
    return abs(math.atan2(pp_y-py,pp_x-px))

def distance():
    return math.sqrt((x-px)**2 + (y-py)**2)
while 1:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            #keystuff
            if event.key == pygame.K_e:
                keys[E] =True

            if event.key == pygame.K_q:
                keys[Q] = True
                
            if event.key == pygame.K_a:
                keys[A]=True
            elif event.key == pygame.K_d:
               keys[D]=True
            elif event.key == pygame.K_w:
                keys[W]=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_e:
                keys[E] =False
               
            if event.key == pygame.K_q:
                keys[Q] = False
           
            if event.key == pygame.K_a:
                keys[A]= False
            elif event.key == pygame.K_d:
               keys[D]=False
            elif event.key == pygame.K_w:
                keys[W]=False 


    #get the distance between ponits (uses a similar technique to matrix rotation)
    if keys[E] == True:
        angle +=0.01
    else:
        pass
    if keys[Q] == True:
        angle -= 0.01
    else:
        pass
    # Fill the background with white
    if angle > 2*pi:
        angle = 0.1
    elif angle < 0:
        angle = 2*pi -1
    
    pp_x = math.cos(angle+pp_ang) * distance()+x
    pp_y = math.sin(angle+pp_ang) * distance()+y
    # Draw a solid blue circle in the center
    
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (pp_x ,pp_y), 50)
    pygame.draw.circle(screen, (255,0,0), (500,500),20)

    pp_ang = rel_angl()
  
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.

