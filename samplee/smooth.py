import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Smooth Movement")

x, y = 50, 425
width, height = 40, 60
vel = 0  # Начальная скорость
acceleration = 0.5  # Ускорение
friction = 0.9  
clock = pygame.time.Clock()

run = True
while run:
    dt = clock.tick(60) / 1000  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        vel -= acceleration
    elif keys[pygame.K_RIGHT]:
        vel += acceleration
    else:
        vel *= friction  

    x += vel  

    if x < 0:
        x = 0
        vel = 0
    elif x > 500 - width:
        x = 500 - width
        vel = 0

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
