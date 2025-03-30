# import pygame

# pygame.init()

# win = pygame.display.set_mode((500 , 500))

# pygame.display.set_caption("for practice")
# x = 50
# y = 425
# hight = 60
# width = 40
# vel = 5

# run = True 
# while run :
#     pygame.time.delay(100)
    
#     for event in pygame.event.get() :
#         if event.type == pygame.QUIT:
#             run =False 
            
#     keys = pygame.key.get_pressed()
    
    
#     if keys[pygame.K_LEFT] and x > vel :
#         x-=vel 
#     if keys[pygame.K_RIGHT] and x < 500 - width -  vel  :
#         x+=vel 
#     if keys[pygame.K_UP] and y > vel :
#         y-=vel 
#     if keys[pygame.K_DOWN] and y < 500 - hight - vel :
#         y+=vel 
#     win.fill((0 , 0 , 0))
    
#     pygame.draw.rect(win , (255 , 0 , 0) , (x , y , width , hight ))  
#     pygame.display.update()  
            
# pygame.guit()


import pygame

pygame.init()

win = pygame.display.set_mode((500 , 500))

pygame.display.set_caption("for practice")
x = 50
y = 425
hight = 60
width = 40
vel = 5

isjump = False 
jumpcount = 10

run = True 
while run :
    pygame.time.delay(100)
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            run =False 
            
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_LEFT] and x > vel :
        x-=vel 
    if keys[pygame.K_RIGHT] and x < 500 - width -  vel  :
        x+=vel    
    if not (isjump):
        if keys[pygame.K_UP] and y > vel :
            y-=vel 
        if keys[pygame.K_DOWN] and y < 500 - hight - vel :
            y+=vel 
        if keys[pygame.K_SPACE]:
            isjump = True 
    else :
        if jumpcount >= -10:
            neg = 1
            
            if jumpcount < 0:
                neg = - 1
                
            y -= (jumpcount ** 2) * 0.5 * neg 
            jumpcount -= 1
        else :
            isjump = False
            jumpcount = 10          
    win.fill((0 , 0 , 0))
    
    pygame.draw.rect(win , (255 , 0 , 0) , (x , y , width , hight ))  
    pygame.display.update()  
            
pygame.guit()




# # import pygame
# # pygame.init()

# # fps = 60
# # timer = pygame.time.Clock()
# # WIDTH = 800
# # HIGHT = 600 
# # active_size = 0 
# # active_color = 'white'
# # # active_figure = None 
# # screen = pygame.display.set_mode((WIDTH , HIGHT))
# # pygame.display.set_caption("painttt")
# # painting= []
# # # start_pos = None
# # # drawing = False
# # # last_pos = None  


# # def draw_menu(size , color  ):  
# #     pygame.draw.rect(screen , 'gray' , [0 , 0 , WIDTH , 70])
# #     pygame.draw.line(screen , 'black' , (0 , 70) , (WIDTH , 70) ,3 )
    
# #     xl_brush = pygame.draw.rect(screen , 'black', [10 , 10 , 50 , 50 ] )
# #     pygame.draw.circle(screen , 'white' ,(35 , 35 ) , 20 )
# #     l_brush = pygame.draw.rect(screen , 'black' , [70 , 10 , 50 , 50 ] )
# #     pygame.draw.circle(screen , 'white' ,(95 , 35 ) , 15 )
# #     m_brush = pygame.draw.rect(screen , 'black' , [130, 10 , 50 , 50] )
# #     pygame.draw.circle(screen , 'white' ,(155 , 35 ) , 10)
# #     s_brush = pygame.draw.rect(screen , 'black' , [190 , 10 , 50 , 50] )
# #     pygame.draw.circle(screen , 'white' ,(215 , 35 ) , 5)
# #     brush_list = [ xl_brush , l_brush , m_brush , s_brush]
    
# #     if size == 20:
# #         pygame.draw.rect(screen ,'green ' , [10 , 10 , 50 , 50] , 3  )
# #     elif size == 15 :
# #         pygame.draw.rect(screen ,'green ' , [70 , 10 , 50 , 50] , 3  )
# #     elif  size == 10:
# #         pygame.draw.rect(screen ,'green ' , [130 , 10 , 50 , 50] , 3  )
# #     elif  size == 5 :
# #         pygame.draw.rect(screen ,'green ' , [190 , 10 , 50 , 50] , 3  ) 
          

# #     blue = pygame.draw.rect(screen , ( 0 , 0 , 255) , [WIDTH - 35 , 10 , 25 , 25])
# #     red = pygame.draw.rect(screen , ( 255 , 0 , 0) , [WIDTH - 35 , 35 , 25 , 25])
# #     green = pygame.draw.rect(screen , ( 0 ,255 , 0) , [WIDTH - 60 , 10 , 25 , 25])
# #     yellow = pygame.draw.rect(screen , ( 255 , 255 , 0) , [WIDTH - 60 , 35 , 25 , 25])
# #     teal = pygame.draw.rect(screen , ( 0 , 255 , 255) , [WIDTH - 85 , 10 , 25 , 25])
# #     purple = pygame.draw.rect(screen , ( 255 , 0 , 255) , [WIDTH - 85 , 35 , 25 , 25])
# #     white = pygame.draw.rect(screen , ( 255 , 255 , 255 ) , [WIDTH - 110 , 10 , 25 , 25])
# #     black = pygame.draw.rect(screen , ( 0 , 0, 0) , [WIDTH - 110 , 35 , 25 , 25])
# #     color_rect = [ blue , red , green , yellow , teal , purple , white , black ]
# #     rgb_list = [( 0 , 0 , 255) ,( 255 , 0 , 0) , ( 0 ,255 , 0) , ( 255 , 255 , 0) ,( 0 , 255 , 255) , ( 255 , 0 , 255) ,( 255 , 255 , 255 ) ,(0 , 0 , 0)]
    
# #     return brush_list , color_rect  , rgb_list

# # def draw_painting (paints):
# #     for i in range (len(paints)):
# #         pygame.draw.circle(screen , paints[i][0] , paints[i][1] , paints[i][2])
        
        
    
# # run = True    
# # while run :
# #     timer.tick(fps)
# #     screen.fill('white')
# #     mouse = pygame.mouse.get_pos()
# #     left_click = pygame.mouse.get_pressed()[0]
    
# #     if left_click and mouse[1]>70:
# #           painting.append((active_color , mouse , active_size))
# #     draw_painting(painting)
# #     if mouse[1]>70:
# #         pygame.draw.circle(screen , active_color , mouse , active_size)     
# #     brushes , colors  , rgbs = draw_menu()
    
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             run = False 
# #         if  event.type == pygame.MOUSEBUTTONDOWN :
# #             for i in range (len(brushes)):
# #                 if brushes[i].collidepoint(event.pos):
# #                     active_size = 20-(i*5)
# #         if  event.type == pygame.MOUSEBUTTONDOWN :
# #             for i in range (len(colors)):
# #                 if colors[i].collidepoint(event.pos):
# #                     active_color = rgbs [i]     
            
            
            
# #     pygame.display.flip()
# # pygame.quit()
    

# import pygame

# pygame.init()

# fps = 60
# timer = pygame.time.Clock()
# WIDTH, HEIGHT = 800, 600
# active_size = 10
# active_color = 'black'
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Paint")
# painting = []
# last_pos = None  

# def draw_menu(size, color):  
#     pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
#     pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)

#     xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
#     pygame.draw.circle(screen, 'white', (35, 35), 20)
#     l_brush = pygame.draw.rect(screen, 'black', [70, 10, 50, 50])
#     pygame.draw.circle(screen, 'white', (95, 35), 15)
#     m_brush = pygame.draw.rect(screen, 'black', [130, 10, 50, 50])
#     pygame.draw.circle(screen, 'white', (155, 35), 10)
#     s_brush = pygame.draw.rect(screen, 'black', [190, 10, 50, 50])
#     pygame.draw.circle(screen, 'white', (215, 35), 5)
#     brush_list = [xl_brush, l_brush, m_brush, s_brush]
    
#     brush_sizes = [20, 15, 10, 5]
#     brush_positions = [10, 70, 130, 190]
#     for i, pos in enumerate(brush_positions):
#         if size == brush_sizes[i]:
#             pygame.draw.rect(screen, 'green', [pos, 10, 50, 50], 3)

#     colors = [
#         ((0, 0, 255), [WIDTH - 35, 10, 25, 25]),  
#         ((255, 0, 0), [WIDTH - 35, 35, 25, 25]),  
#         ((0, 255, 0), [WIDTH - 60, 10, 25, 25]),  
#         ((255, 255, 0), [WIDTH - 60, 35, 25, 25]),  
#         ((0, 255, 255), [WIDTH - 85, 10, 25, 25]),  
#         ((255, 0, 255), [WIDTH - 85, 35, 25, 25]),  
#         ((255, 255, 255), [WIDTH - 110, 10, 25, 25]),  
#         ((0, 0, 0), [WIDTH - 110, 35, 25, 25]),  
#     ]
    
#     color_rects = [pygame.draw.rect(screen, color, rect) for color, rect in colors]
#     color_values = [color for color, _ in colors]

#     return brush_list, color_rects, color_values

# def draw_painting(paints):
#     for i in range(1, len(paints)):
#         if paints[i-1][3] and paints[i][3]:
#             pygame.draw.line(screen, paints[i][0], paints[i-1][1], paints[i][1], paints[i][2] * 2)  
#             pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])  

# run = True    
# while run:
#     timer.tick(fps)
#     screen.fill('white')
#     mouse = pygame.mouse.get_pos()
#     left_click = pygame.mouse.get_pressed()[0]

#     if left_click and mouse[1] > 70:
#         if last_pos:  
#             pygame.draw.line(screen, active_color, last_pos, mouse, active_size * 2)  
#         last_pos = mouse  
#         painting.append((active_color, mouse, active_size, True))  
#     else:
#         last_pos = None  
#         painting.append((active_color, mouse, active_size, False))  

#     draw_painting(painting)
#     if mouse[1] > 70:
#         pygame.draw.circle(screen, active_color, mouse, active_size)

#     brushes, colors, rgbs = draw_menu(active_size, active_color)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             for i, brush in enumerate(brushes):
#                 if brush.collidepoint(event.pos):
#                     active_size = [20, 15, 10, 5][i]
#             for i, color in enumerate(colors):
#                 if color.collidepoint(event.pos):
#                     active_color = rgbs[i]
#         if event.type == pygame.MOUSEBUTTONUP:
#             last_pos = None  

#     pygame.display.flip()
# pygame.quit()

# import pygame

# pygame.init()

# fps = 60
# timer = pygame.time.Clock()
# WIDTH, HEIGHT = 800, 600
# active_size = 10
# active_color = 'black'
# active_figure = None 
# start_pos = None 
# end_pos = None 


# is_erasing = False
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Paint")
# painting = []
# last_pos = None  

# def draw_menu(size, color, erasing):  
#     pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
#     pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)

#     xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
#     pygame.draw.circle(screen, 'white', (35, 35), 20)
#     l_brush = pygame.draw.rect(screen, 'black', [70, 10, 50, 50])
#     pygame.draw.circle(screen, 'white', (95, 35), 15)
#     m_brush = pygame.draw.rect(screen, 'black', [130, 10, 50, 50])
#     pygame.draw.circle(screen, 'white', (155, 35), 10)
#     s_brush = pygame.draw.rect(screen, 'black', [190, 10, 50, 50])
#     pygame.draw.circle(screen, 'white', (215, 35), 5)
#     brush_list = [xl_brush, l_brush, m_brush, s_brush]
    
#     brush_sizes = [20, 15, 10, 5]
#     brush_positions = [10, 70, 130, 190]
#     for i, pos in enumerate(brush_positions):
#         pygame.draw.circle(screen, 'white', (pos + 25, 35), brush_sizes[i])
#         if size == brush_sizes[i] and not erasing and  active_figure is None:
#             pygame.draw.rect(screen, 'green', [pos, 10, 50, 50], 3)
    
#     eraser = pygame.draw.rect(screen, 'blue', [370, 10, 50, 50])
#     eraser_img = pygame.image.load('lab9/imagee/image.png')
#     eraser_img = pygame.transform.scale(eraser_img, (40, 40))
#     screen.blit(eraser_img, (375, 15))
#     if erasing:
#         pygame.draw.rect(screen, 'green', [370, 10, 50, 50], 3)
    
#     colors = [
#         ((0, 0, 255), [WIDTH - 35, 10, 25, 25]),  
#         ((255, 0, 0), [WIDTH - 35, 35, 25, 25]),  
#         ((0, 255, 0), [WIDTH - 60, 10, 25, 25]),  
#         ((255, 255, 0), [WIDTH - 60, 35, 25, 25]),  
#         ((0, 255, 255), [WIDTH - 85, 10, 25, 25]),  
#         ((255, 0, 255), [WIDTH - 85, 35, 25, 25]),  
#         ((255, 255, 255), [WIDTH - 110, 10, 25, 25]),  
#         ((0, 0, 0), [WIDTH - 110, 35, 25, 25]),  
#     ]
    
#     color_rects = [pygame.draw.rect(screen, color, rect) for color, rect in colors]
#     color_values = [color for color, _ in colors]
    
#     rectanglee = pygame.draw.rect(screen , 'blue' , [250 , 10 , 50 , 50] )
#     pygame.draw.rect(screen, 'white', [260 , 20 , 30 , 30])
#     circlee = pygame.draw.rect(screen , 'blue' , [310 , 10 , 50 , 50] )
#     pygame.draw.circle(screen , 'white' ,(335 , 35 ) , 18 )
#     squaree = pygame.draw.rect(screen , 'blue' , [430 , 10 , 50 , 50] )
#     pygame.draw.rect(screen, 'white', [440, 20, 30, 30])  
#     r_triangle = pygame.draw.rect(screen , 'blue' , [490 , 10 , 50 , 50] )
#     pygame.draw.polygon(screen, 'white', [(500, 50), (500, 15), (530, 50)])  
#     e_triangle = pygame.draw.rect(screen , 'blue' , [550 , 10 , 50 , 50] )
#     pygame.draw.polygon(screen, 'white', [(575, 15), (555, 50), (595, 50)])  
#     rhombuss = pygame.draw.rect(screen , 'blue' , [610 , 10 , 50 , 50] )
#     pygame.draw.polygon(screen, 'white', [(635, 15), (655, 35), (635, 55), (615, 35)])
#     figure_dict = {
#         'rectangle': rectanglee, 'circle': circlee,
#         'square': squaree, 'right_triangle': r_triangle, 
#         'equilateral_triangle': e_triangle, 'rhombus': rhombuss
#     }
#     if active_figure:
#         pygame.draw.rect(screen, 'green', figure_dict[active_figure], 3)
#     return brush_list, color_rects, color_values, eraser , figure_dict 

# def draw_painting(paints):
#     for i in range(1, len(paints)):
#         if paints[i-1][3] and paints[i][3]:
#             pygame.draw.line(screen, paints[i][0], paints[i-1][1], paints[i][1], paints[i][2] * 2)
#             pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])

# run = True    
# while run:
#     timer.tick(fps)
#     screen.fill('white')
#     mouse = pygame.mouse.get_pos()
#     left_click = pygame.mouse.get_pressed()[0]

#     # if left_click and mouse[1] > 70:
#     #     if last_pos:  
#     #         pygame.draw.line(screen, active_color, last_pos, mouse, active_size * 2)
#     #     last_pos = mouse  
#     #     if is_erasing:
#     #         painting = [p for p in painting if (p[1][0] - mouse[0])**2 + (p[1][1] - mouse[1])**2 > (active_size * 2) ** 2]
#     #     else:
#     #         painting.append((active_color, mouse, active_size, True))  
#     # else:
#     #     last_pos = None  
#     #     painting.append((active_color, mouse, active_size, False))  

    
# if left_click and mouse[1] > 70:
#     x, y = mouse
#     if active_figure:  # Если выбрана фигура, рисуем ее контур
#         if active_figure == 'rectangle':
#             pygame.draw.rect(screen, active_color, (x - 25, y - 15, 50, 30), 3)
#         elif active_figure == 'circle':
#             pygame.draw.circle(screen, active_color, (x, y), 20, 3)
#         elif active_figure == 'square':
#             pygame.draw.rect(screen, active_color, (x - 20, y - 20, 40, 40), 3)
#         elif active_figure == 'right_triangle':
#             pygame.draw.polygon(screen, active_color, [(x, y), (x, y - 40), (x + 40, y)], 3)
#         elif active_figure == 'equilateral_triangle':
#             pygame.draw.polygon(screen, active_color, [(x, y - 30), (x - 25, y + 15), (x + 25, y + 15)], 3)
#         elif active_figure == 'rhombus':
#             pygame.draw.polygon(screen, active_color, [(x, y - 30), (x + 20, y), (x, y + 30), (x - 20, y)], 3)

#             # Сохраняем фигуру в список, чтобы она не исчезала
#         painting.append((active_color, mouse, active_figure, True))  

#     else:  # Если не выбрана фигура — рисуем кистью
#         if last_pos:  
#             pygame.draw.line(screen, active_color, last_pos, mouse, active_size * 2)
#         last_pos = mouse  
#         if is_erasing:
#             painting = [p for p in painting if (p[1][0] - mouse[0])**2 + (p[1][1] - mouse[1])**2 > (active_size * 2) ** 2]
#         else:
#             painting.append((active_color, mouse, active_size, True))
# else:
#     last_pos = None  
#     painting.append((active_color, mouse, active_size, False))

        
    
#     draw_painting(painting)
#     if mouse[1] > 70:
#         pygame.draw.circle(screen, active_color, mouse, active_size)

#     brushes, colors, rgbs, eraser  , figures = draw_menu(active_size, active_color, is_erasing)

#     # for event in pygame.event.get():
#     #     if event.type == pygame.QUIT:
#     #         run = False
#     #     if event.type == pygame.MOUSEBUTTONDOWN:
#     #         for i, brush in enumerate(brushes):
#     #             if brush.collidepoint(event.pos):
#     #                 active_size = [20, 15, 10, 5][i]
#     #                 is_erasing = False
#     #                 active_figure = None
#     #         for i, color in enumerate(colors):
#     #             if color.collidepoint(event.pos):
#     #                 active_color = rgbs[i]
#     #                 is_erasing = False
#     #         for figure_name, figure_rect in figures.items():
#     #             if figure_rect.collidepoint(event.pos):
#     #                 active_figure = figure_name
#     #                 is_erasing = False
#     #                 active_size = None
#     #         if eraser.collidepoint(event.pos):
#     #             is_erasing = True
#     #             active_figure = None
#     #     if event.type == pygame.MOUSEBUTTONUP:
#     #         last_pos = None  

# for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#         run = False

#     if event.type == pygame.MOUSEBUTTONDOWN:
#         for i, brush in enumerate(brushes):
#             if brush.collidepoint(event.pos):
#                 active_size = [20, 15, 10, 5][i]
#                 is_erasing = False
#                 active_figure = None

#         for i, color in enumerate(colors):
#             if color.collidepoint(event.pos):
#                 active_color = rgbs[i]
#                 is_erasing = False

#         for figure_name, figure_rect in figures.items():
#             if figure_rect.collidepoint(event.pos):
#                 active_figure = figure_name
#                 is_erasing = False
#                 active_size = None

#         if eraser.collidepoint(event.pos):
#             is_erasing = True
#             active_figure = None

#         if active_figure and event.pos[1] > 70:  # Запоминаем начальную точку рисования фигуры
#             start_pos = event.pos

#     if event.type == pygame.MOUSEBUTTONUP:
#         if start_pos and active_figure:
#             x1, y1 = start_pos
#             x2, y2 = event.pos
#             width, height = abs(x2 - x1), abs(y2 - y1)

#             if active_figure == 'rectangle':
#                 pygame.draw.rect(screen, active_color, (min(x1, x2), min(y1, y2), width, height), 3)
#             elif active_figure == 'circle':
#                 center = ((x1 + x2) // 2, (y1 + y2) // 2)
#                 radius = min(width, height) // 2
#                 pygame.draw.circle(screen, active_color, center, radius, 3)
#             elif active_figure == 'square':
#                 size = min(width, height)
#                 pygame.draw.rect(screen, active_color, (min(x1, x2), min(y1, y2), size, size), 3)
#             elif active_figure == 'right_triangle':
#                 pygame.draw.polygon(screen, active_color, [(x1, y1), (x1, y2), (x2, y2)], 3)
#             elif active_figure == 'equilateral_triangle':
#                 pygame.draw.polygon(screen, active_color, [(x1, y2), ((x1 + x2) // 2, y1), (x2, y2)], 3)
#             elif active_figure == 'rhombus':
#                 center_x, center_y = (x1 + x2) // 2, (y1 + y2) // 2
#                 pygame.draw.polygon(screen, active_color, [(center_x, y1), (x2, center_y), (center_x, y2), (x1, center_y)], 3)

#             painting.append((active_color, (x1, y1, x2, y2), active_figure, True))  # Сохраняем фигуру
#             start_pos = None  # Сбрасываем начальную точку после рисования

#         last_pos = None  # Сбрасываем последнюю позицию для кисти

#     pygame.display.flip()
# pygame.quit()
