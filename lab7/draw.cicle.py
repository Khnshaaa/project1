# Draw circle - a red ball of size 50 x 50 (radius = 25) on white background.
# When user presses Up, Down, Left, Right arrow keys on keyboard, the
# ball should move by 20 pixels in the direction of pressed key. 
# The ball should not leave the screen, i.e. user input that leads the ball 
# to leave of the screen should be ignored
import pygame

pygame.init()
width, hight = 500, 500
win = pygame.display.set_mode((width, hight))
pygame.display.set_caption("Red Ball")

radius = 25 
x, y = width // 2, hight // 2  
vel = 20  


run = True
while run:
    pygame.time.delay(100) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x - radius - vel >= 0: 
        x -= vel
    if keys[pygame.K_RIGHT] and x + radius + vel <= width:  
        x += vel
    if keys[pygame.K_UP] and y - radius - vel >= 0:  
        y -= vel
    if keys[pygame.K_DOWN] and y + radius + vel <= hight:  
        y += vel

   
    win.fill((255, 255, 255))  
    pygame.draw.circle(win, (255, 0, 0), (x, y), radius) 
    pygame.display.update() 

pygame.quit()
