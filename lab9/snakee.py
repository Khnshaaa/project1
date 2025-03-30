import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Размер окна
WIDTH, HEIGHT = 600, 400  
BLOCK_SIZE = 20  

# Начальные параметры игры
SPEED = 5  
APPLES_EATEN = 0  
LEVEL = 1  
SCORE = 0  

# Создание окна игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Цвета еды
RED = (255, 0, 0)    # Яблоко 
YELLOW = (255, 255, 0)  # Банан 
PINK = (255, 20, 147)  # Вишня 

# Типы еды и их очки
FOOD_TYPES = {
    "apple": {"color": RED, "points": 10, "lifetime": 5},
    "banana": {"color": YELLOW, "points": 15, "lifetime": 4},
    "cherry": {"color": PINK, "points": 20, "lifetime": 3}
}

# Начальные параметры змейки
snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"

# Функция генерации случайной еды
def generate_food():
    while True:
        food_pos = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
                    random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE)
        if food_pos not in snake:  # Проверяем, чтобы еда не была на змейке
            food_type = random.choice(list(FOOD_TYPES.keys()))  # Выбираем случайный тип еды
            return food_pos, food_type, time.time()  # Запоминаем время появления еды

food, food_type, food_time = generate_food()  # Первая еда

# Функция рисования змейки
def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

# Функция рисования еды
def draw_food():
    pygame.draw.rect(screen, FOOD_TYPES[food_type]["color"], (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

# Функция отображения счёта и уровня
def draw_score():
    font = pygame.font.Font(None, 30)
    text = font.render(f"Score: {SCORE}  Level: {LEVEL}", True, WHITE)
    screen.blit(text, (10, 10))

# Функция движения змейки
def move_snake():
    global snake, food, food_type, food_time, APPLES_EATEN, SPEED, LEVEL, SCORE
    head_x, head_y = snake[0]  

    # Двигаем голову змейки
    if direction == "RIGHT":
        new_head = (head_x + BLOCK_SIZE, head_y)
    elif direction == "LEFT":
        new_head = (head_x - BLOCK_SIZE, head_y)
    elif direction == "UP":
        new_head = (head_x, head_y - BLOCK_SIZE)
    elif direction == "DOWN":
        new_head = (head_x, head_y + BLOCK_SIZE)

    snake.insert(0, new_head)

    # Проверяем, съела ли змейка еду
    if new_head == food:
        SCORE += FOOD_TYPES[food_type]["points"]  # Начисляем очки за съеденную еду
        APPLES_EATEN += 1  
        food, food_type, food_time = generate_food()  # Создаём новую еду

        # Повышаем уровень каждые 4 яблока
        if APPLES_EATEN % 4 == 0:
            LEVEL += 1
            SPEED += 2  

    else:
        snake.pop()  

    # Проверяем, не истёк ли таймер еды
    if time.time() - food_time > FOOD_TYPES[food_type]["lifetime"]:
        food, food_type, food_time = generate_food()  # Генерируем новую еду

# Функция проверки столкновений
def check_collision():
    head_x, head_y = snake[0]

    # Проверка выхода за границы
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        return True

    # Проверка столкновения с собой
    if (head_x, head_y) in snake[1:]:
        return True

    return False

# Игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)  

    # Обрабатываем события (клавиши)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
            elif event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"

    move_snake()  
    if check_collision():  
        running = False  

    draw_snake()  
    draw_food()  
    draw_score()  

    pygame.display.flip()  
    clock.tick(SPEED)  

pygame.quit()  
