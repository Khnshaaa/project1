import pygame
pygame.init()

fps = 60
timer = pygame.time.Clock()
WIDTH, HEIGHT = 800, 600
active_size = 10
active_color = 'black'
active_figure = None   # выбранная фигура (например, 'rectangle', 'circle', и т.д.)
is_erasing = False
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
painting = []
last_pos = None  

def draw_menu(size, color, erasing):
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
        if size == brush_sizes[i] and not erasing and active_figure is None:
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
    e_triangle = pygame.draw.rect(screen, 'blue', [550, 10, 50, 50])
    pygame.draw.polygon(screen, 'white', [(575, 15), (555, 50), (595, 50)])
    rhombuss = pygame.draw.rect(screen, 'blue', [610, 10, 50, 50])
    pygame.draw.polygon(screen, 'white', [(635, 15), (655, 35), (635, 55), (615, 35)])
    
    return brush_list, color_rects, color_values, eraser

def draw_painting(paints):
    for i in range(1, len(paints)):
        if paints[i-1][3] and paints[i][3]:
            if isinstance(paints[i][2], (int, float)):
                pygame.draw.line(screen, paints[i][0], paints[i-1][1], paints[i][1], int(paints[i][2]) * 2)
                pygame.draw.circle(screen, paints[i][0], paints[i][1], int(paints[i][2]))

run = True
while run:
    timer.tick(fps)
    screen.fill('white')
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
    brushes, colors, rgbs, eraser, = draw_menu(active_size, active_color, is_erasing)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, brush in enumerate(brushes):
                if brush.collidepoint(event.pos):
                    active_size = [20, 15, 10, 5][i]
                    is_erasing = False
            for i, color in enumerate(colors):
                if color.collidepoint(event.pos):
                    active_color = rgbs[i]
                    is_erasing = False
            if eraser.collidepoint(event.pos):
                is_erasing = True
        if event.type == pygame.MOUSEBUTTONUP:
            last_pos = None

    pygame.display.flip()
pygame.quit()
