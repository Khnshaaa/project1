# import pygame
# from color_palette import *
# from random import randint

# pygame.init()

# WIDTH = 600
# HEIGHT = 600

# screen = pygame.display.set_mode((HEIGHT, WIDTH))

# CELL = 30

# def draw_grid():
#     for i in range(HEIGHT // 2):
#         for j in range(WIDTH // 2):
#             pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

# def draw_grid_chess():
#     colors = [colorWHITE, colorGRAY]

#     for i in range(HEIGHT // 2):
#         for j in range(WIDTH // 2):
#             pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"{self.x}, {self.y}"

# class Snake:
#     def __init__(self):
#         self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
#         self.dx = 1
#         self.dy = 0

#     def move(self):
#         for i in range(len(self.body) - 1, 0, -1):
#             self.body[i].x = self.body[i - 1].x
#             self.body[i].y = self.body[i - 1].y

#         self.body[0].x += self.dx
#         self.body[0].y += self.dy

#     def draw(self):
#         head = self.body[0]
#         pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
#         for segment in self.body[1:]:
#             pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

#     def check_collision(self, food):
#         head = self.body[0]
#         if head.x == food.pos.x and head.y == food.pos.y:
#             print("Got food!")
#             self.body.append(Point(head.x, head.y))

# class Food:
#     def __init__(self):
#         self.pos = Point(9, 9)

#     def draw(self):
#         pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

#     def move_rnd(self):
#         self.pos = Point(randint(0, WIDTH // CELL - 1), randint(0, HEIGHT // CELL - 1))

# FPS = 5
# clock = pygame.time.Clock()

# food = Food()
# snake = Snake()

# loop_cnt = 0

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 snake.dx = 1
#                 snake.dy = 0
#             elif event.key == pygame.K_LEFT:
#                 snake.dx = -1
#                 snake.dy = 0
#             elif event.key == pygame.K_DOWN:
#                 snake.dx = 0
#                 snake.dy = 1
#             elif event.key == pygame.K_UP:
#                 snake.dx = 0
#                 snake.dy = -1

#     draw_grid_chess()

#     loop_cnt += 1

#     if(loop_cnt > 4):
#         loop_cnt = 0
#         food.move_rnd()
        

#     snake.move()
#     snake.check_collision(food)

#     snake.draw()
#     food.draw()

    


#     pygame.display.flip()
#     clock.tick(FPS)

# pygame.quit()

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

red = (255, 0, 0)
blue = (0, 0, 255)

running = True

clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 72)

text = font.render("Hello KBTU", True, blue)

x = 400 - text.get_width() // 2
y = 300 - text.get_height() // 2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]: 
        x += 1
    if keys[pygame.K_LEFT]: 
        x -= 1
    if keys[pygame.K_DOWN]:
        y += 1
    if keys[pygame.K_UP]:
        y -= 1
        
    screen.fill((0, 0, 0))

    screen.blit(text, (x, y))
    
    pygame.display.flip()
    clock.tick(60)