
# import pygame 
# from pygame.locals import *

# # Размеры окна
# size = width, height = (600, 800)

# # Ширина дороги для 3 полос
# road_w = int(width / 1.3)
# roadmark_w = int(width / 80)

# pygame.init()
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Racer - 3 Lane Road")
# # Определяем границы между белыми линиями

# #background_img = pygame.image.load("lab8/imagee/AnimatedStreet.png")
# player_img = pygame.image.load("lab8/imagee/Player.png")
# enemy_img = pygame.image.load("lab8/imagee/Enemy.png")
# coin_img_original = pygame.image.load("lab8/imagee/coin.png")
# coin_img = pygame.transform.scale(coin_img_original, (40, 40))
# # pygame.mixer.music.load("lab8/imagee/lab_8_IMAG_background.wav")
# # pygame.mixer.music.play(-1)
# running = True
# clock = pygame.time.Clock()
# left_border = width / 2 - road_w / 2 + roadmark_w * 3 # Левая граница (белая линия)
# right_border = width / 2 + road_w / 2 - roadmark_w * 3 - player_img.get_width() # Правая граница (белая линия)

# car_loc = player_img.get_rect()
# car_loc.center = width/2  , height*0.85
# car2_loc = enemy_img.get_rect()
# #car2_loc.center = (width / 2, -enemy_img.get_height())  # По центру дороги, выше экрана
# car2_loc.center = width/2 , height*0.1  # Фиксированное положение по вертикали


# while running:
#     screen.fill((60, 220, 0)) 
#     pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_w / 2, 0, road_w, height))
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             running = False  
#         if event.type == KEYDOWN:
#             if event.key  in [K_a , K_LEFT] :
#                 if car_loc.left - road_w / 3 >= left_border:
#                     car_loc.move_ip([-int(road_w / 3), 0])
#             elif event.key in [K_d , K_RIGHT]:
#                 if car_loc.right + road_w / 3 <= right_border + player_img.get_width():
#                     car_loc.move_ip([int(road_w / 3), 0])
                
#     pygame.draw.rect(screen, (255, 240, 60), (width / 2 - road_w / 6 - roadmark_w / 2, 0, roadmark_w, height))  # Линия слева
#     pygame.draw.rect(screen, (255, 240, 60), (width / 2 + road_w / 6 - roadmark_w / 2, 0, roadmark_w, height))  # Линия справа
#     pygame.draw.rect(screen, (255, 255, 255), (width / 2 - road_w / 2 + roadmark_w, 0, roadmark_w, height))
#     pygame.draw.rect(screen, (255, 255, 255), (width / 2 + road_w / 2 - roadmark_w * 2, 0, roadmark_w, height))
#     screen.blit(player_img , car_loc)
#     screen.blit(enemy_img , car2_loc)
#     pygame.display.update()
#     pygame.display.flip()
#     clock.tick

# pygame.quit()
import pygame 
import random
from pygame.locals import *

# Размеры окна
size = width, height = (600 , 800)

# Ширина дороги для 3 полос
road_w = int(width / 1.3)
roadmark_w = int(width / 80)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Racer - 3 Lane Road")

player_img = pygame.image.load("lab8/imagee/Player.png")
enemy_img = pygame.image.load("lab8/imagee/Enemy.png")
clock = pygame.time.Clock()

left_border = width / 2 - road_w / 2 + roadmark_w * 3  # Левая граница
right_border = width / 2 + road_w / 2 - roadmark_w * 3 - player_img.get_width()  # Правая граница

car_loc = player_img.get_rect()
car_loc.center = width / 2, height * 0.85

# Список врагов
enemies = []
enemy_speed = 5  # Начальная скорость врагов

running = True

while running:
    screen.fill((60, 220, 0)) 
    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_w / 2, 0, road_w, height))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False  
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                if car_loc.left - road_w / 3 >= left_border:
                    car_loc.move_ip(-int(road_w / 3), 0)
            elif event.key in [K_d, K_RIGHT]:
                if car_loc.right + road_w / 3 <= right_border + player_img.get_width():
                    car_loc.move_ip(int(road_w / 3), 0)
    
    # Спавн врагов
    if random.randint(1, 100) < 2:  # 3% шанс спавна на каждом кадре
        lane_x = random.choice([width / 2 - road_w / 3, width / 2, width / 2 + road_w / 3])
        enemy_rect = enemy_img.get_rect(center=(lane_x, -50))
        enemies.append(enemy_rect)
    
    # Движение врагов
    for enemy in enemies[:]:
        enemy.move_ip(0, enemy_speed)
        if enemy.top > height:  # Удаляем врагов, когда они уходят за экран
            enemies.remove(enemy)
        if car_loc.colliderect(enemy):  # Проверка столкновения
            print("Game Over!")
            running = False
    
    # Отрисовка объектов
    pygame.draw.rect(screen, (255, 240, 60), (width / 2 - road_w / 6 - roadmark_w / 2, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255, 240, 60), (width / 2 + road_w / 6 - roadmark_w / 2, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - road_w / 2 + roadmark_w, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 + road_w / 2 - roadmark_w * 2, 0, roadmark_w, height))
    
    screen.blit(player_img, car_loc)
    for enemy in enemies:
        screen.blit(enemy_img, enemy)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
