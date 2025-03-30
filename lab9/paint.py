
import pygame
pygame.init()
# Размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Paint")
# Создаем холст (фон - белый)
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))
# Настройки рисования
current_color = (0, 0, 0)  # Цвет кисти по умолчанию
brush_size = 5  # Размер кисти
mode = "draw"  # Режим рисования (по умолчанию - кисть)
active_size = 10  # Активный размер кисти
active_color = 'black'  # Активный цвет
active_figure = None  # Выбранная фигура (rectangle, circle и т.д.)
is_erasing = False  # Флаг режима стирания
painting = []  # Список для хранения нарисованных линий
# Шрифт для UI
font = pygame.font.SysFont('Arial', 18)
drawing = False
start_pos = None
preview_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)  # Прозрачный слой для предпросмотра

def draw_menu(size, color, erasing , active_figure):
    # Рисуем панель меню
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)

    # Рисуем кнопки кистей
    xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    l_brush = pygame.draw.rect(screen, 'black', [70, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (95, 35), 15)
    m_brush = pygame.draw.rect(screen, 'black', [130, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (155, 35), 10)
    s_brush = pygame.draw.rect(screen, 'black', [190, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (215, 35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]
    
    brush_sizes = [20, 15, 10, 5]
    brush_positions = [10, 70, 130, 190]
    for i, pos in enumerate(brush_positions):
        pygame.draw.circle(screen, 'white', (pos + 25, 35), brush_sizes[i])
        # Если кисть выбрана и ни одна фигура не активна, выделяем зеленым
        if size == brush_sizes[i] and not erasing :
            pygame.draw.rect(screen, 'green', [pos, 10, 50, 50], 3)
    
    eraser = pygame.draw.rect(screen, 'blue', [370, 10, 50, 50])
    eraser_img = pygame.image.load('lab9/imagee/image.png')
    eraser_img = pygame.transform.scale(eraser_img, (40, 40))
    screen.blit(eraser_img, (375, 15))
    if erasing:
        pygame.draw.rect(screen, 'green', [370, 10, 50, 50], 3)
    
    colors = [
        ((0, 0, 255), [WIDTH - 35, 10, 25, 25]),
        ((255, 0, 0), [WIDTH - 35, 35, 25, 25]),
        ((0, 255, 0), [WIDTH - 60, 10, 25, 25]),
        ((255, 255, 0), [WIDTH - 60, 35, 25, 25]),
        ((0, 255, 255), [WIDTH - 85, 10, 25, 25]),
        ((255, 0, 255), [WIDTH - 85, 35, 25, 25]),
        ((255, 255, 255), [WIDTH - 110, 10, 25, 25]),
        ((0, 0, 0), [WIDTH - 110, 35, 25, 25]),
    ]
    
    color_rects = [pygame.draw.rect(screen, col, rect) for col, rect in colors]
    color_values = [col for col, _ in colors]
    
    # Рисуем кнопки фигур
    rectanglee = pygame.draw.rect(screen, 'blue', [250, 10, 50, 50])
    pygame.draw.rect(screen, 'white', [260, 20, 30, 30])
    circlee = pygame.draw.rect(screen, 'blue', [310, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (335, 35), 18)
    squaree = pygame.draw.rect(screen, 'blue', [430, 10, 50, 50])
    pygame.draw.rect(screen, 'white', [440, 20, 30, 30])
    r_triangle = pygame.draw.rect(screen, 'blue', [490, 10, 50, 50])
    pygame.draw.polygon(screen, 'white', [(500, 50), (500, 15), (530, 50)])
    triangle = pygame.draw.rect(screen, 'blue', [550, 10, 50, 50])
    pygame.draw.polygon(screen, 'white', [(575, 15), (555, 50), (595, 50)])
    rhombuss = pygame.draw.rect(screen, 'blue', [610, 10, 50, 50])
    pygame.draw.polygon(screen, 'white', [(635, 15), (655, 35), (635, 55), (615, 35)])
    
    figuree = [rectanglee , circlee ,squaree ,  r_triangle , triangle , rhombuss  ]
    figure_dict = {
        'rectangle': rectanglee, 'circle': circlee, 
        'square': squaree, 'right_triangle': r_triangle, 
        'triangle': triangle, 'rhombus': rhombuss
    }
    if active_figure in figure_dict:
        pygame.draw.rect(screen, 'green', figure_dict[active_figure], 3)
    return brush_list, color_rects, color_values, eraser , [rectanglee, circlee, squaree, r_triangle, triangle, rhombuss]
def draw_painting(paints):
    for i in range(1, len(paints)):
        if paints[i-1][3] and paints[i][3]:
            if isinstance(paints[i][2], (int, float)):
                pygame.draw.line(screen, paints[i][0], paints[i-1][1], paints[i][1], int(paints[i][2]) * 2)
                pygame.draw.circle(screen, paints[i][0], paints[i][1], int(paints[i][2]))
def draw_ui():
    instructions = [
        "              ",
        "              ",
        "Press S for Square",
        "Press Y for Rhombus",
        "Press H for Rtriangle",
        "Press T for Etriangle ",
    ]
    y = 50
    for line in instructions:
        instr_text = font.render(line, True, (0, 0, 0))
        screen.blit(instr_text, (10, y))
        y += 20
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((255, 255, 255))  # Очистка экрана
    screen.blit(canvas, (0, 0))  # Отображение холста
    screen.blit(preview_surface, (0, 0))  # Отображение предпросмотра
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    if left_click and mouse[1] > 70:
        if last_pos:
            pygame.draw.line(screen, active_color, last_pos, mouse, active_size * 2)
        last_pos = mouse
        if is_erasing:
            painting = [p for p in painting if (p[1][0] - mouse[0])**2 + (p[1][1] - mouse[1])**2 > (active_size * 2) ** 2]
        else:
            painting.append((active_color, mouse, active_size, True))
    else:
        last_pos = None
        painting.append((active_color, mouse, active_size, False))
    
    draw_painting(painting)
    if mouse[1] > 70 :
        pygame.draw.circle(screen, active_color, mouse, active_size)
    brushes, colors, rgbs, eraser,figures  = draw_menu(active_size, active_color, is_erasing , active_figure)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, brush in enumerate(brushes):
                if brush.collidepoint(event.pos):
                    # active_size = [20, 15, 10, 5][i]
                    active_size = 0 if active_size == 20 - (i * 5) else 20 - (i * 5)
                    # active_size = 20 - (i * 5)
                    is_erasing = False
            for i, color in enumerate(colors):
                if color.collidepoint(event.pos):
                    active_color = rgbs[i]
                    is_erasing = False
            if eraser.collidepoint(event.pos):
                if is_erasing ==  True :
                    is_erasing = False
                    mode = "draw"
                else :
                    is_erasing = True
                    mode = "eraser"
            figure_names = ['rectangle', 'circle', 'eraser', 'square', 'right_triangle', 'triangle', 'rhombus']
            for i in range(len(figures)):
                if figures[i].collidepoint(event.pos):
                    active_figure = None if active_figure == figure_names[i] else figure_names[i]
        if active_figure == "rectangle":
                mode= "rectangle"
        if active_figure == "circle":
                mode= "circle"
        if active_figure == "square":
                mode= "square"
        if active_figure == "right_triangle":
                mode= "right_triangle"
        if active_figure == "triangle":
                mode= "triangle"
        if active_figure == "rhombus" :
            mode = "rhombus"                
        if event.type == pygame.MOUSEBUTTONUP:
            last_pos = None
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                mode = "draw"
            elif event.key == pygame.K_r:
                mode = "rectangle"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_t:
                mode = "triangle"
            elif event.key == pygame.K_h:
                mode = "right_triangle"
            elif event.key == pygame.K_y:
                mode = "rhombus"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_1:
                current_color = (255, 0, 0)
            elif event.key == pygame.K_2:
                current_color = (0, 255, 0)
            elif event.key == pygame.K_3:
                current_color = (0, 0, 255)
            elif event.key == pygame.K_4:
                current_color = (255, 255, 0)
            elif event.key == pygame.K_5:
                current_color = (255, 0, 255)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                drawing = True
                start_pos = event.pos
                preview_surface.fill((0, 0, 0, 0))  # Очистка слоя предпросмотра
                if mode == "draw" or mode == "eraser":
                    color = current_color if mode == "draw" else (255, 255, 255)
                    pygame.draw.circle(canvas, color, event.pos, brush_size // 2)
            elif event.button == 3:  # Правая кнопка - очистка холста
                canvas.fill((255, 255, 255))
        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "draw" or mode == "eraser":
                color = current_color if mode == "draw" else (255, 255, 255)
                pygame.draw.line(canvas, color, start_pos, event.pos, brush_size)
                start_pos = event.pos
            else:
                preview_surface.fill((0, 0, 0, 0))  # Очистка слоя предпросмотра
                end_pos = event.pos
                if mode == "rectangle":# REcatngle 
                    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    rect.normalize()
                    pygame.draw.rect(preview_surface, current_color + (150,), rect, brush_size)
                elif mode == "circle":
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(preview_surface, current_color + (150,), start_pos, radius, brush_size)          
                elif mode == "equilateral_triangle":
                    size = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    height = (size * (3 ** 0.5)) / 2  # Высота равностороннего треугольника
                    p1 = (start_pos[0], start_pos[1] - height / 2)  # Верхняя вершина
                    p2 = (start_pos[0] - size / 2, start_pos[1] + height / 2)  # Левая вершина
                    p3 = (start_pos[0] + size / 2, start_pos[1] + height / 2)  # Правая вершина
                    pygame.draw.polygon(preview_surface, current_color + (150,), [p1, p2, p3], brush_size)
                elif mode == "right_triangle":
                    pygame.draw.polygon(preview_surface, current_color + (150,), [start_pos, (start_pos[0], end_pos[1]), end_pos], 2)
                elif mode == "rhombus":
                    center_x = (start_pos[0] + end_pos[0]) // 2
                    center_y = (start_pos[1] + end_pos[1]) // 2
                    pygame.draw.polygon(preview_surface, current_color + (150,), [(center_x, start_pos[1]), (end_pos[0], center_y), (center_x, end_pos[1]), (start_pos[0], center_y)], 2)
                elif mode == "square":
                    size = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    rect = pygame.Rect(start_pos, (size, size))
                    if end_pos[0] < start_pos[0]:
                        rect.x -= size
                    if end_pos[1] < start_pos[1]:
                        rect.y -= size
                    pygame.draw.rect(preview_surface, current_color + (150,), rect, brush_size)       
        if event.type == pygame.MOUSEBUTTONUP and drawing:
            drawing = False
            end_pos = event.pos
            if mode == "rectangle":
                rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                rect.normalize()
                pygame.draw.rect(canvas, current_color, rect, brush_size)
            elif mode == "circle":
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(canvas, current_color, start_pos, radius, brush_size)
            elif mode == "triangle":
                pygame.draw.polygon(canvas, current_color, [start_pos, (start_pos[0] - (end_pos[0] - start_pos[0]), end_pos[1]), end_pos], 2)
            elif mode == "right_triangle":
                pygame.draw.polygon(canvas, current_color, [start_pos, (start_pos[0], end_pos[1]), end_pos], 2)
            elif mode == "rhombus":
                center_x = (start_pos[0] + end_pos[0]) // 2
                center_y = (start_pos[1] + end_pos[1]) // 2
                pygame.draw.polygon(canvas, current_color, [(center_x, start_pos[1]), (end_pos[0], center_y), (center_x, end_pos[1]), (start_pos[0], center_y)], 2)
            elif mode == "square":
                size = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                rect = pygame.Rect(start_pos, (size, size))
                if end_pos[0] < start_pos[0]:
                    rect.x -= size
                if end_pos[1] < start_pos[1]:
                    rect.y -= size
                pygame.draw.rect(canvas, current_color, rect, brush_size)
            preview_surface.fill((0, 0, 0, 0))  # Очистка слоя предпросмотра
    draw_ui()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
