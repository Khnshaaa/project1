import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы ширины и высоты экрана
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game with Coins")

# Загрузка изображений
background_img = pygame.image.load("lab8/imagee/AnimatedStreet.png")
player_img = pygame.image.load("lab8/imagee/Player.png")
enemy_img = pygame.image.load("lab8/imagee/Enemy.png")
coin_img_original = pygame.image.load("lab8/imagee/coin.png")

# Уменьшаем размер монеты
coin_img = pygame.transform.scale(coin_img_original, (60, 60))

# Загрузка музыки
pygame.mixer.music.load("lab8/imagee/lab_8_IMAG_background.wav")
pygame.mixer.music.play(-1)

# Классы для игрока, врага и монет
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 80))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect(center=(random.randint(40, WIDTH - 40), -50))

    def update(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > HEIGHT:
            self.rect.center = (random.randint(40, WIDTH - 40), -50)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect(center=(random.randint(40, WIDTH - 40), random.randint(-100, -40)))

    def update(self):
        self.rect.move_ip(0, 3)
        if self.rect.top > HEIGHT:
            self.rect.center = (random.randint(40, WIDTH - 40), random.randint(-100, -40))

# Группы спрайтов
player = Player()
enemy = Enemy()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)

# Добавляем несколько монет
for _ in range(5):
    coin = Coin()
    coins.add(coin)
    all_sprites.add(coin)

# Счётчик монет
coin_count = 0

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
        print("Game Over!")
        running = False

    # Проверка сбора монет
    collected_coins = pygame.sprite.spritecollide(player, coins, dokill=True)
    for _ in collected_coins:
        coin_count += 1
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    # Отрисовка заднего фона и всех объектов
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)

    # Отображение количества собранных монет
    font = pygame.font.SysFont('Arial', 24)
    coin_text = font.render(f'Coins: {coin_count}', True, (255, 255, 0))
    screen.blit(coin_text, (WIDTH - 140, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()