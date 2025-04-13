
import pygame
pygame.init()

fps = 60
timer = pygame.time.Clock()
WIDTH = 800
HIGHT = 600 
active_size = 0 
active_color = 'white'
active_figure = None 
# active_figure = circle(5)
screen = pygame.display.set_mode((WIDTH , HIGHT))
pygame.display.set_caption("painttt")
paintingg = []
start_pos = None
drawing = False
last_pos = None  # Хранит предыдущее положение мыши


def draw_menu(size , color  , active_figure):  
    pygame.draw.rect(screen , 'gray' , [0 , 0 , WIDTH , 70])
    pygame.draw.line(screen , 'black' , (0 , 70) , (WIDTH , 70) ,3 )
    
    xl_brush = pygame.draw.rect(screen , 'black', [10 , 10 , 50 , 50 ] )
    pygame.draw.circle(screen , 'white' ,(35 , 35 ) , 20 )
    l_brush = pygame.draw.rect(screen , 'black' , [70 , 10 , 50 , 50 ] )
    pygame.draw.circle(screen , 'white' ,(95 , 35 ) , 15 )
    m_brush = pygame.draw.rect(screen , 'black' , [130, 10 , 50 , 50] )
    pygame.draw.circle(screen , 'white' ,(155 , 35 ) , 10)
    s_brush = pygame.draw.rect(screen , 'black' , [190 , 10 , 50 , 50] )
    pygame.draw.circle(screen , 'white' ,(215 , 35 ) , 5)
    brush_list = [ xl_brush , l_brush , m_brush , s_brush]
    
    if size == 20:
        pygame.draw.rect(screen ,'green ' , [10 , 10 , 50 , 50] , 3  )
    elif size == 15 :
        pygame.draw.rect(screen ,'green ' , [70 , 10 , 50 , 50] , 3  )
    elif  size == 10:
        pygame.draw.rect(screen ,'green ' , [130 , 10 , 50 , 50] , 3  )
    elif  size == 5 :
        pygame.draw.rect(screen ,'green ' , [190 , 10 , 50 , 50] , 3  ) 
          
    # pygame.draw.circle(screen , color ,(215 , 35) , 30 )
    # pygame.draw.circle(screen , 'dark gray ' , (215 , 35 ), 30 , 3 )
    
    rectanglee = pygame.draw.rect(screen , 'blue' , [250 , 10 , 50 , 50] )
    # inner_size = 30  
    # inner_x = 250 + (50 - inner_size) // 2
    # inner_y = 10 + (50 - inner_size) // 2
    # # pygame.draw.rect(screen, 'white', [inner_x, inner_y, inner_size, inner_size])
    pygame.draw.rect(screen, 'white', [260 , 20 , 30 , 30])
    circlee = pygame.draw.rect(screen , 'blue' , [310 , 10 , 50 , 50] )
    pygame.draw.circle(screen , 'white' ,(335 , 35 ) , 18 )
    eraserr = pygame.draw.rect(screen , 'blue' , [370 , 10 , 50 , 50] )
    eraser_img = pygame.image.load('lab9/imagee/image.png')
    eraser_img = pygame.transform.scale(eraser_img, (40, 40))
    screen.blit(eraser_img, (375, 15))  # Position it inside the blue square
    squaree = pygame.draw.rect(screen , 'blue' , [430 , 10 , 50 , 50] )
    pygame.draw.rect(screen, 'white', [440, 20, 30, 30])  
    r_triangle = pygame.draw.rect(screen , 'blue' , [490 , 10 , 50 , 50] )
    pygame.draw.polygon(screen, 'white', [(500, 50), (500, 15), (530, 50)])  
    e_triangle = pygame.draw.rect(screen , 'blue' , [550 , 10 , 50 , 50] )
    pygame.draw.polygon(screen, 'white', [(575, 15), (555, 50), (595, 50)])  
    rhombuss = pygame.draw.rect(screen , 'blue' , [610 , 10 , 50 , 50] )
    pygame.draw.polygon(screen, 'white', [(635, 15), (655, 35), (635, 55), (615, 35)])
    
    figuree = [rectanglee , circlee , eraserr , squaree ,  r_triangle , e_triangle , rhombuss  ]
    figure_dict = {
        'rectangle': rectanglee, 'circle': circlee, 'eraser': eraserr, 
        'square': squaree, 'right_triangle': r_triangle, 
        'equilateral_triangle': e_triangle, 'rhombus': rhombuss
    }
    if active_figure in figure_dict:
        pygame.draw.rect(screen, 'green', figure_dict[active_figure], 3)
    
    
    blue = pygame.draw.rect(screen , ( 0 , 0 , 255) , [WIDTH - 35 , 10 , 25 , 25])
    red = pygame.draw.rect(screen , ( 255 , 0 , 0) , [WIDTH - 35 , 35 , 25 , 25])
    green = pygame.draw.rect(screen , ( 0 ,255 , 0) , [WIDTH - 60 , 10 , 25 , 25])
    yellow = pygame.draw.rect(screen , ( 255 , 255 , 0) , [WIDTH - 60 , 35 , 25 , 25])
    teal = pygame.draw.rect(screen , ( 0 , 255 , 255) , [WIDTH - 85 , 10 , 25 , 25])
    purple = pygame.draw.rect(screen , ( 255 , 0 , 255) , [WIDTH - 85 , 35 , 25 , 25])
    white = pygame.draw.rect(screen , ( 255 , 255 , 255 ) , [WIDTH - 110 , 10 , 25 , 25])
    black = pygame.draw.rect(screen , ( 0 , 0, 0) , [WIDTH - 110 , 35 , 25 , 25])
    color_rect = [ blue , red , green , yellow , teal , purple , white , black ]
    rgb_list = [( 0 , 0 , 255) ,( 255 , 0 , 0) , ( 0 ,255 , 0) , ( 255 , 255 , 0) ,( 0 , 255 , 255) , ( 255 , 0 , 255) ,( 255 , 255 , 255 ) ,(0 , 0 , 0)]
    
    return brush_list , color_rect , rgb_list , [rectanglee, circlee, eraserr, squaree, r_triangle, e_triangle, rhombuss]

def draw_painting(paints):
    for paint in paints:
        if paint[2] == "rectangle":
            pygame.draw.rect(screen, paint[0], paint[1], 2)
        else:
            pygame.draw.circle(screen, paint[0], paint[1], paint[2])
# def draw_painting(paints):
#     for paint in paints:
#         if paint[2] == "rectangle":
#             pygame.draw.rect(screen, paint[0], paint[1], 2)
#         elif paint[2] == "line":  # Новый случай для линий
#             pygame.draw.line(screen, paint[0], paint[1], paint[2], paint[4] * 2)
#         else:
#             pygame.draw.circle(screen, paint[0], paint[1], paint[2])

        
    
run = True    
while run :
    timer.tick(fps)
    screen.fill((255 , 255 , 255))
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    
    if drawing and active_figure == "rectangle":
        end_pos = mouse
        rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
        rect.normalize()
        pygame.draw.rect(screen, active_color, rect, 2)
    # if left_click and mouse[1]> 70 :
    #     paintingg.append((active_color , mouse , active_size))
    draw_painting(paintingg)
    
    if mouse[1] > 70 and active_size > 0:
        pygame.draw.circle(screen , active_color , mouse  , active_size)    
    if left_click and mouse[1] > 70:
        if active_figure == 'eraser':
            paintingg = [p for p in paintingg if (p[1][0] - mouse[0])**2 + (p[1][1] - mouse[1])**2 > active_size**2]
        paintingg.append((active_color, (mouse[0], mouse[1]), active_size))
    
    brushes , colors , rgbs , figures = draw_menu(active_size , active_color , active_figure)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

        elif event.type == pygame.MOUSEBUTTONDOWN:
            last_pos = event.pos  # Запоминаем начальную точку
            for i in range(len(brushes)): 
                if brushes[i].collidepoint(event.pos):
                    active_size = 0 if active_size == 20 - (i * 5) else 20 - (i * 5)
                    active_figure = None  

            for i in range(len(colors)): 
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

            figure_names = ['rectangle', 'circle', 'eraser', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']
            for i in range(len(figures)):
                if figures[i].collidepoint(event.pos):
                    active_figure = None if active_figure == figure_names[i] else figure_names[i]

            if active_figure == "rectangle":
                drawing = True
                start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            last_pos = None  
            if active_figure == "rectangle" and drawing:
                end_pos = event.pos
                rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                rect.normalize()
                paintingg.append((active_color, rect, "rectangle"))  # Сохраняем прямоугольник
                drawing = False  # Завершаем рисование

    pygame.display.flip()
pygame.quit()
   
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False 
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             last_pos = event.pos  # Устанавливаем начальную точку при нажатии
#         elif event.type == pygame.MOUSEBUTTONUP:
#             last_pos = None              
#         if  event.type == pygame.MOUSEBUTTONDOWN:
#             for i in range(len(brushes)): 
#                 if brushes[i].collidepoint(event.pos):
#                     if active_size == 20 - (i*5):
#                         active_size = 0 
#                     else :
#                         active_size = 20 - (i*5)
#                         active_figure = None  
#             for i in range(len(colors)): 
#                 if colors [i].collidepoint(event.pos):
#                     active_color = rgbs[i]
                    
#             # for i in range(len(figures)): 
#             #     if figures[i].collidepoint(event.pos):
#             #         active_figure = rgbs[i]  
#             figure_names = ['rectangle', 'circle', 'eraser', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']
#             for i in range(len(figures)):
#                 if figures[i].collidepoint(event.pos):
#                     if active_figure == figure_names[i]:  
#                         active_figure = None  # Если фигура уже выбрана, отключаем её
#                     else:
#                         active_figure = figure_names[i] 
#                         # active_size = 0 
#             if active_figure == "rectangle":
#                 drawing = True
#                 start_pos = event.pos
#         if event.type == pygame.MOUSEBUTTONUP:
#             if active_figure == "rectangle" and drawing:
#                 end_pos = event.pos
#                 rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
#                 rect.normalize()
#                 paintingg.append((active_color, rect, "rectangle"))  # Сохраняем прямоугольник
#                 drawing = False
        
#     pygame.display.flip()
    
# pygame.guit()

