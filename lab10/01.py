import pygame              
import random              
import sys                  # для выхода из программы
import psycopg2             # для подключения к PostgreSQL

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)

class DBManager:
    def __init__(self):
        # Подключаемся к базе данных PostgreSQL
        
        self.conn = psycopg2.connect(
            dbname='snake',
            user='postgres',
            password='12345678',
            host='localhost'
        )
        
        self.cursor = self.conn.cursor()
        self.create_tables()
    
    def create_tables(self):
        # Создаем таблицу пользователей
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                user_name VARCHAR(255) UNIQUE
            );
        """)
        
        
        # Создаем таблицу для сохранения результатов
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_score (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(user_id),
                score INTEGER,
                level INTEGER
            );
        """)
        self.conn.commit()

    def get_or_create_user(self, username):
        # Пытаемся получить пользователя из таблицы
        self.cursor.execute("SELECT user_id FROM users WHERE user_name = %s;", (username,))
        row = self.cursor.fetchone()
        if row:
            user_id = row[0]
            # Получаем последний сохранённый уровень
            self.cursor.execute("SELECT level FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1;", (user_id,))
            level_row = self.cursor.fetchone()
            level = level_row[0] if level_row else 1
            return user_id, level
        else:
            # Создаем нового пользователя, если его нет
            self.cursor.execute("INSERT INTO users (user_name) VALUES (%s) RETURNING user_id;", (username,))
            user_id = self.cursor.fetchone()[0]
            self.conn.commit()
            return user_id, 1

    def save_score(self, user_id, score, level):
        self.cursor.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s);", 
                            (user_id, score, level))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

#  Класс для еды 
class Food:
    def __init__(self, snake, walls):
        self.snake = snake
        self.walls = walls
        self.position = (0, 0)
        self.spawn()

    def spawn(self):
        # Ищем позицию для еды, не занятую змейкой или стенами
        while True:
            pos = (random.randint(1, GRID_WIDTH - 2), random.randint(1, GRID_HEIGHT - 2))
            if pos not in self.snake.body and pos not in self.walls:
                self.position = pos
                break

# Класс для змейки 
class Snake:
    def __init__(self, db_manager):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.db_manager = db_manager
        self.player_name = ""
        self.user_id = None
        self.paused = False

    def get_player_name(self):
        # Открываем поле ввода имени игрока
        input_box = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 25, 200, 50)
        font = pygame.font.Font(None, 32)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Активируем поле, если кликнули по нему
                    active = input_box.collidepoint(event.pos)
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            done = True
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            # Отрисовка поля ввода
            screen.fill(BLACK)
            txt_surface = font.render(text, True, color)
            input_box.w = max(200, txt_surface.get_width() + 10)
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()

        self.player_name = text
        self.user_id, loaded_level = self.db_manager.get_or_create_user(self.player_name)
        return loaded_level

    def move(self, food, walls):
        global score, level, speed
        if self.paused:
            return True

        head = self.body[0]
        new_head = ((head[0] + self.direction[0]) % GRID_WIDTH,
                    (head[1] + self.direction[1]) % GRID_HEIGHT)

        # Проверка столкновения с телом или стенами
        if new_head in self.body[1:] or new_head in walls:
            return False

        self.body.insert(0, new_head)
        if new_head == food.position:
            score += 1
            # Каждые 3 очка увеличивается уровень и скорость
            if score % 3 == 0:
                level += 1
                speed += 1
            food.spawn()
        else:
            self.body.pop()
        return True

    def change_direction(self, direction):
        # Избегаем разворота на 180 градусов
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def save_progress(self):
        # Сохраняем текущий счёт и уровень
        self.db_manager.save_score(self.user_id, score, level)
        print(f"Прогресс игрока {self.player_name} сохранён!")

# Функция создания стен по краям поля 
def create_walls():
    walls = [(0, i) for i in range(GRID_HEIGHT)] + [(GRID_WIDTH - 1, i) for i in range(GRID_HEIGHT)]
    walls += [(i, 0) for i in range(GRID_WIDTH)] + [(i, GRID_HEIGHT - 1) for i in range(GRID_WIDTH)]
    return walls

#  Основной блок выполнения
def main():
    global score, level, speed, screen

    # Инициализация Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Змейка")

    # Инициализируем менеджер БД
    db_manager = DBManager()

    # Создаем стены, змейку и еду
    walls = create_walls()
    snake = Snake(db_manager)
    loaded_level = snake.get_player_name()  # получаем имя игрока и последний уровень
    food = Food(snake, walls)
    score = 0
    level = loaded_level
    speed = 10 + (loaded_level - 1) * 2

    clock = pygame.time.Clock()
    running = True

    # Основной игровой цикл
    while running:
        screen.fill(BLACK)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))
                elif event.key == pygame.K_SPACE:
                    # Пауза
                    snake.paused = not snake.paused
                elif event.key == pygame.K_s:
                    # Ручное сохранение прогресса
                    snake.save_progress()

        # Обновляем состояние игры
        if not snake.move(food, walls):
            running = False  # игра заканчивается при столкновении

        # Отрисовка змейки
        for segment in snake.body:
            pygame.draw.rect(screen, WHITE,
                             (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        # Отрисовка еды
        pygame.draw.rect(screen, RED,
                         (food.position[0] * GRID_SIZE, food.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Отрисовка счетчика и уровня
        font = pygame.font.SysFont(None, 25)
        text_surface = font.render(f"Счёт: {score}   Уровень: {level}", True, WHITE)
        screen.blit(text_surface, (10, 10))

        pygame.display.flip()
        clock.tick(speed)

    # Сохраняем прогресс при выходе и закрываем соединение с БД
    snake.save_progress()
    pygame.quit()
    db_manager.close()

if __name__ == "__main__":
    main()
