
import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы экрана
WIDTH, HEIGHT = 500 , 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game with Coins")

# Загрузка изображений
background_img = pygame.image.load("lab9/imagee/bqq.png")
player_img = pygame.image.load("lab8/imagee/Player.png")
enemy_img = pygame.image.load("lab8/imagee/Enemy.png")
coin_img_original = pygame.image.load("lab8/imagee/coin.png")

# Уменьшаем размер монеты
coin_img = pygame.transform.scale(coin_img_original, (40, 40))

# Загрузка музыки
pygame.mixer.music.load("lab8/imagee/lab_8_IMAG_background.wav")
pygame.mixer.music.play(-1)

# Константа для увеличения скорости врага
SPEED_INCREMENT = 1
COINS_FOR_SPEED_UP = 5

# # Функция для сброса игры
# def reset_game():
#     global player, enemy, coins, all_sprites, coin_count, COINS_FOR_SPEED_UP

#     player = Player()
#     enemy = Enemy()
#     coins = pygame.sprite.Group()
#     all_sprites = pygame.sprite.Group()
    
#     all_sprites.add(player)
#     all_sprites.add(enemy)

#     for _ in range(4):
#         coin = Coin()
#         coins.add(coin)
#         all_sprites.add(coin)

coin_count = 0
COINS_FOR_SPEED_UP = 5


# Классы
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 80))
    
        # Определяем границы внутри дороги (между жёлтыми линиями)
        self.left_boundary = WIDTH // 7  # Левая граница дороги
        self.right_boundary = WIDTH - WIDTH // 4 + self.rect.width  # Правая граница
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > self.left_boundary:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < self.right_boundary:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        #self.rect = self.image.get_rect(center=(random.randint(40, WIDTH - 40), -50))
        self.speed = 4 
        # Определяем три возможных позиции на дороге
        lane_positions = [WIDTH // 4, WIDTH // 2, 3 * WIDTH // 4]
        self.rect = self.image.get_rect(center=(random.choice(lane_positions), -50))

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            #self.rect.center = (random.randint(40, WIDTH - 40), -50)
            self.rect.center = (random.choice([WIDTH // 4, WIDTH // 2, 3 * WIDTH // 4]), -50)
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        #self.rect = self.image.get_rect(center=(random.randint(40, WIDTH - 40), random.randint(-100, -40)))
        self.value = random.choice([1, 3, 5])  # Разная ценность монет
        
        # Определяем три возможных позиции на дороге
        lane_positions = [WIDTH // 4, WIDTH // 2, 3 * WIDTH // 4]
        self.rect = self.image.get_rect(center=(random.choice(lane_positions), random.randint(-100, -40)))

    def update(self):
        self.rect.move_ip(0, 3)
        if self.rect.top > HEIGHT:
            self.kill()
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
            self.rect.center = (random.randint(40, WIDTH - 40), random.randint(-100, -40))
def spawn_coin():
    if len(coins) < 4:  
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)
        
        

# Группы спрайтов
player = Player()
enemy = Enemy()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)

# Добавляем несколько монет
for _ in range(4):
    coin = Coin()
    coins.add(coin)
    all_sprites.add(coin)

# Счётчик монет
coin_count = 0
health = 3  # Начальное количество жизней

# Запускаем игру
# reset_game()


# Основной цикл игры
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление спрайтов
    all_sprites.update()

    # Проверка столкновения с врагом
    if pygame.sprite.collide_rect(player, enemy):
        health= health-1
        if health == 0 :
        #    pygame.time.wait(5000)  # Пауза 5 секунд
        
        #    reset_game()  
           running = False  
        else:
            enemy.rect.center = (random.choice([WIDTH//4,WIDTH//2 , 3 * WIDTH//4 ]) , -50)
    # Проверка сбора монет
    collected_coins = pygame.sprite.spritecollide(player, coins, dokill=True)
    for coin in collected_coins:
        coin_count += coin.value  # Добавляем очки за монету
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)
        
    for _ in collected_coins:
        coin_count += 1
        spawn_coin() 
    # Увеличиваем скорость врага при достижении N монет
    if coin_count >= COINS_FOR_SPEED_UP:
        enemy.speed += SPEED_INCREMENT
        COINS_FOR_SPEED_UP += 15 # Следующий порог

    # Отрисовка
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)

    # Отображение количества монет
    font = pygame.font.SysFont('Arial', 24)
    coin_text = font.render(f'Coins: {coin_count}', True, (255, 255, 0))
    screen.blit(coin_text, (WIDTH - 120, 10))
    # Отображение здоровья
    health_text = font.render(f'Health: {health}', True, (255, 0, 0))
    screen.blit(health_text, (10, 10))  # Рисуем здоровье в левом верхнем углу

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
