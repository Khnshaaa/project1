import pygame
pygame.init()

screen = pygame.display.set_mode((800 , 400))

red = (255 , 0 , 0)
blue = (0 , 0 ,255)

run = True 
is_red = True

flip = 1
inc_flip_freq = pygame.USEREVENT +1
flip_color = pygame.USEREVENT +2 

pygame.time.set_timer(inc_flip_freq , 3000)
pygame.time.set_timer(flip_color , int(1000/flip))

while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False
        if event.type == flip_color:
            is_red = not is_red
        if event.type == inc_flip_freq:
            flip += 1 
            pygame.time.set_timer(flip_color , (int(1000/flip)))
    
    if is_red:
        screen.fill(red)
    else:
        screen.fill(blue)
    pygame.display.flip()
pygame.quit()