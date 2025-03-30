import pygame
import random

# Инициализация pygame
pygame.init()

# Константы
width, height = 600, 600
block_size = 20
speed = 5


WHITE = (255, 255, 255)


# Экран
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Функция генерации случайной позиции еды
def random_food_position(snake_body):
    while True:
        x = random.randrange(0, width, block_size)
        y = random.randrange(0, height, block_size)
        if [x, y] not in snake_body:
            return [x, y]

# Начальные параметры змейки
snake = [[100, 100]]
dx, dy = block_size, 0
food = random_food_position(snake)
score = 0
level = 1

# Основной цикл игры
running = True
while running:
    screen.fill((0 , 255 , 0))
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -block_size
            if event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, block_size
            if event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -block_size, 0
            if event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = block_size, 0

    # Движение змейки
    new_head = [snake[0][0] + dx, snake[0][1] + dy]
    snake.insert(0, new_head)

    # Проверка столкновения с границей
    if new_head[0] < 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height:
        running = False

    # Проверка съедения еды
    if new_head == food:
        score += 1
        if score % 4 == 0:
            level += 1
            speed += 2
        food = random_food_position(snake)
    else:
        snake.pop()

    # Проверка столкновения с собой
    if new_head in snake[1:]:
        running = False

    # Рисование змейки и еды
    for segment in snake:
        pygame.draw.rect(screen,  ("Orange"), (segment[0], segment[1], block_size, block_size))
    pygame.draw.rect(screen, ("Red"), (food[0], food[1], block_size, block_size))

    # Отображение счета и уровня
    font = pygame.font.SysFont('Arial', 25)
    score_text = font.render(f'Score: {score} Level: {level}', True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
