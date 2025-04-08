import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# Базовый класс сцены
class Scene:
    def update(self):
        pass
    def draw(self, screen):
        pass
    def handle_event(self, event):
        pass

# Меню
class MenuScene(Scene):
    def draw(self, screen):
        font = pygame.font.Font(None, 50)
        text = font.render("Press ENTER to Start", True, (255, 255, 255))
        screen.fill((0, 0, 0))
        screen.blit(text, (50, 200))

    def handle_event(self, event):
        global current_scene
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            current_scene = GameScene()  # Переключаемся на игру

# Игра
class GameScene(Scene):
    def __init__(self):
        self.x = 250

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_RIGHT]:
            self.x += 5

    def draw(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, 400, 50, 50))

    def handle_event(self, event):
        pass

# Запуск
current_scene = MenuScene()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        current_scene.handle_event(event)

    current_scene.update()
    current_scene.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
