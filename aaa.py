import pygame
pygame.init()
# инициализирует все модули pygame (графику, звук, события и т. д.).
# Без этой команды pygame не будет работать

screen = pygame.display.set_mode((500  , 400))

pygame.display.set_caption("My first work ")

running = True 
while running :
    for event in pygame.event.get():#получает список событий (например, клик мыши, нажатие клавиш).
        if event.type == pygame.QUIT:#– если пользователь закрыл окно, программа останавливается.
            running = False 
    #Без этого цикла окно зависнет и не будет реагировать на действия!
    screen.fill((50, 50, 50))
    pygame.display.flip()
#     Обновляет окно и показывает изменения.
# 💡 Если не использовать pygame.display.flip(), то экран не будет обновляться!
    
pygame.quit()
# Очищает память и корректно завершает pygame.
# 💡 Без pygame.quit() могут остаться ошибки или "висящие" процессы.




# def draw_clock():
#     # screen.fill((255, 255, 255))  
#     pygame.draw.circle(screen, (0, 0, 0), (250, 250), 200, 5) 
#     pygame.draw.circle(screen, (0, 0, 0), (250, 250), 5) 

#     t = time.localtime()
#     sec = t.tm_sec
#     minute = t.tm_min
#     hour = t.tm_hour % 12

    
#     sec_angle = math.radians(270 + sec * 6)
#     min_angle = math.radians(270 + minute * 6)
#     hour_angle = math.radians(270 + hour * 30 + minute * 0.5)

    
#     sec_hand = (250 + 150 * math.cos(sec_angle), 250 + 150 * math.sin(sec_angle))
#     min_hand = (250 + 120 * math.cos(min_angle), 250 + 120 * math.sin(min_angle))
#     hour_hand = (250 + 90 * math.cos(hour_angle), 250 + 90 * math.sin(hour_angle))

#     pygame.draw.line(screen, (255, 0, 0), (250, 250), sec_hand, 2)  
#     pygame.draw.line(screen, (0, 0, 255), (250, 250), min_hand, 5)  
#     pygame.draw.line(screen, (0, 255, 0), (250, 250), hour_hand, 8)  




