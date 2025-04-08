import pygame
import sys
import math

# Инициализация Pygame
pygame.init()

# Константы экрана
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw Star")

# Функция для рисования звезды
def draw_star(screen, color, center, radius, points):
    angle = math.pi / points  # Угол между вершинами звезды
    points_list = []
    for i in range(2 * points):
        angle_offset = angle * i
        if i % 2 == 0:
            x = center[0] + radius * math.cos(angle_offset)
            y = center[1] + radius * math.sin(angle_offset)
        else:
            x = center[0] + (radius / 2) * math.cos(angle_offset)
            y = center[1] + (radius / 2) * math.sin(angle_offset)
        points_list.append((x, y))
    pygame.draw.polygon(screen, color, points_list)

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Задний фон
    screen.fill((0, 0, 0))

    # Рисуем звезду
    draw_star(screen, (255, 255, 0), (WIDTH // 2, HEIGHT // 2), 100, 5)

    # Обновляем экран
    pygame.display.update()

# Закрытие Pygame
pygame.quit()
sys.exit()
