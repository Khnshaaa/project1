import pygame

pygame.init()

# Размеры окна и создание поверхности для рисования (canvas)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint")

# Создаем canvas, на котором будем рисовать (фон - белый)
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

# Начальные настройки рисования
current_color = (0, 0, 0)   # текущий цвет (по умолчанию черный)
brush_size = 5            # размер кисти для рисования
mode = "draw"             # режимы: "draw" (свободное рисование), "rectangle", "circle", "eraser"

# Шрифт для вывода инструкций на экран
font = pygame.font.SysFont('Arial', 18)

# Переменные для отслеживания рисования
drawing = False
start_pos = None
last_pos = None

def draw_ui():
    """Функция для отображения текущего режима и инструкций на экране."""
    mode_text = font.render("Mode: " + mode, True, (0, 0, 0))
    color_text = font.render("Color: " + str(current_color), True, (0, 0, 0))
    instructions = [
        "Press D for free draw",
        "Press R for rectangle",
        "Press C for circle",
        "Press E for eraser",
        "Press 1: Red, 2: Green, 3: Blue, 4: Yellow, 5: Magenta",
        "Left mouse button to draw"
    ]
    screen.blit(mode_text, (10, 10))
    screen.blit(color_text, (10, 30))
    y = 50
    for line in instructions:
        instr_text = font.render(line, True, (0, 0, 0))
        screen.blit(instr_text, (10, y))
        y += 20

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Обработка нажатий клавиш для переключения режимов и выбора цвета
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                mode = "draw"
            elif event.key == pygame.K_r:
                mode = "rectangle"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_1:
                current_color = (255, 0, 0)  # красный
            elif event.key == pygame.K_2:
                current_color = (0, 255, 0)  # зелёный
            elif event.key == pygame.K_3:
                current_color = (0, 0, 255)  # синий
            elif event.key == pygame.K_4:
                current_color = (255, 255, 0)  # жёлтый
            elif event.key == pygame.K_5:
                current_color = (255, 0, 255)  # магента

        # Обработка событий мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # левая кнопка мыши
                drawing = True
                start_pos = event.pos
                last_pos = event.pos
                if mode in ["draw", "eraser"]:
                    draw_color = current_color if mode == "draw" else (255, 255, 255)
                    pygame.draw.circle(canvas, draw_color, event.pos, brush_size // 2)
        elif event.type == pygame.MOUSEMOTION:
            if drawing and mode in ["draw", "eraser"]:
                draw_color = current_color if mode == "draw" else (255, 255, 255)
                pygame.draw.line(canvas, draw_color, last_pos, event.pos, brush_size)
                last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                drawing = False
                end_pos = event.pos
                if mode == "rectangle":
                    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    rect.normalize()
                    pygame.draw.rect(canvas, current_color, rect, brush_size)
                elif mode == "circle":
                    dx = end_pos[0] - start_pos[0]
                    dy = end_pos[1] - start_pos[1]
                    radius = int((dx**2 + dy**2) ** 0.5)
                    pygame.draw.circle(canvas, current_color, start_pos, radius, brush_size)
                    
                    
                    

    # Обновляем экран: заливаем фон для UI и выводим canvas
    screen.fill((200, 200, 200))  # фон для области UI (серый)
    screen.blit(canvas, (0, 0))
    draw_ui()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
