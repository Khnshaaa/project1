# Create a simple clock application (only with minutes and seconds) 
# which is synchronized with system clock. Use Mickey's right hand 
# as minutes arrow and left - as seconds.
import pygame 
import time 
import math 

pygame.init()

width , hight = 500 , 500
screen = pygame.display.set_mode((500 , 500))
pygame.display.set_caption("clock")

background = pygame.image.load("lab7/imagee/clock.png") 
fir_hand = pygame.image.load("lab7/imagee/min_hand.png")
sec_hand = pygame.image.load("lab7/imagee/sec_hand.png")
#pygame.transform.scale(image, (new_width, new_height))
background = pygame.transform.scale(background, (width , hight )) 
fir_hand = pygame.transform.scale(fir_hand, ( 400 , 400))  
sec_hand = pygame.transform.scale(sec_hand, ( 400 , 400))  
 

def rotate_center(image, angle, pos):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pos)
    return rotated_image, new_rect

clock = pygame.time.Clock()
run = True 
while run :
    screen.blit(background, (0, 0))
    
    t = time.localtime()
    minn = t.tm_min
    secc = t.tm_sec
    secc_angle = -secc * 6 
    minn_angle = -minn * 6 
    #В Pygame угол поворота измеряется против часовой стрелки, 
    # а в реальных часах стрелки двигаются по часовой стрелке.
    
    center_x , center_y = width //2 , hight //2 
    #Функция rotate_center():
    # Поворачивает стрелку на вычисленный угол.
    # Размещает её в центре экрана.
    rotated_sec, rect_sec = rotate_center(sec_hand, secc_angle, (center_x, center_y))
    screen.blit(rotated_sec, rect_sec.topleft)
    #Теперь стрелка всегда поворачивается вокруг центра, оставаясь на месте.
    
    rotated_min, rect_min = rotate_center(fir_hand, minn_angle, (center_x, center_y))
    screen.blit(rotated_min, rect_min.topleft)
    
    pygame.display.update()
    clock.tick(1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    
pygame.quit()