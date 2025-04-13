# import pygame

# pygame.init()
# screen = pygame.display.set_mode((500, 500))
# clock = pygame.time.Clock()

# # Начальные координаты круга
# x, y = 250, 250
# radius = 25
# vel = 5

# running = True
# while running:
#     screen.fill((255, 255, 255))  # Белый фон
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and x - radius > 0:
#         x -= vel  # Двигаем круг влево
#     if keys[pygame.K_RIGHT] and x + radius < 500:
#         x += vel  # Двигаем круг вправо
#     if keys[pygame.K_UP] and y - radius > 0:
#         y -= vel  # Двигаем круг вверх
#     if keys[pygame.K_DOWN] and y + radius < 500:
#         y += vel  # Двигаем круг вниз
    
#     pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)  # Рисуем круг
#     pygame.display.update()
#     clock.tick(60)

# pygame.quit()

import pygame

pygame.init()
WIDTH , HIGHT = 500  , 500

screen = pygame.display.set_mode((WIDTH , HIGHT))
WHITE = (255 , 255 , 255)
BLUE = (0 , 0 , 255)

x , y = WIDTH//2, HIGHT//2
radius = 20

velocity_x , velocity_y = 0 , 0 
gravity = 0.5
jump_strength = -20
is_jumping = False 

acseleration = 0.5 
friction = 0.95

clock = pygame.time.Clock()

run = True   
while run :
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        velocity_x -= acseleration
    if keys[pygame.K_RIGHT]:
        velocity_x += acseleration
    if  keys[pygame.K_UP] and not is_jumping:
        velocity_y = jump_strength
        is_jumping = True
        # velocity_y -= acseleration
        
    # if keys[pygame.K_DOWN]:
    #     velocity_y += acseleration
    
    velocity_x *= friction
    # velocity_y *= friction
    velocity_y += gravity 
    
    
    x += velocity_x
    y += velocity_y
    
    # Проверка, не упал ли шар на землю
    if y >= HIGHT - radius:  # Шар на земле
        y = HIGHT - radius  # Устанавливаем на землю
        velocity_y = 0  # Останавливаем вертикальную скорость
        is_jumping = False  # Можно прыгать снова
    
    if x - radius < 0 or x + radius > WIDTH :
        velocity_x = - velocity_x 
    # if  y - radius < 0 or y + radius > HIGHT :
    #     velocity_y = - velocity_y
    
    pygame.draw.circle(screen , BLUE , (int(x) , int (y)) , radius)
    pygame.display.update()
    
    
    clock.tick(60)
pygame.quit()
    
    