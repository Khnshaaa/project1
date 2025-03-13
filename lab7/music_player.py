import pygame
import os  

pygame.init()

width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Playlist")
clock = pygame.time.Clock()

playlist = []
music_folder = "lab7/music_folder"

if os.path.exists(music_folder):
    allmusic = os.listdir(music_folder)
    for song in allmusic:
        if song.endswith(".mp3"):
            playlist.append(os.path.join(music_folder, song))
else:
    exit()

if not playlist:
    exit()

try:
    background = pygame.image.load(os.path.join("lab7/imagee/backgroundd.png"))
    playb = pygame.image.load(os.path.join("lab7/imagee/play.png"))
    pausb = pygame.image.load(os.path.join("lab7/imagee/pause.png"))
    nextb = pygame.image.load(os.path.join("lab7/imagee/next.png"))
    prevb = pygame.image.load(os.path.join("lab7/imagee/back.png"))
except FileNotFoundError:
    exit()

playb = pygame.transform.scale(playb, (70, 70))
pausb = pygame.transform.scale(pausb, (70, 70))
nextb = pygame.transform.scale(nextb, (70, 70))
prevb = pygame.transform.scale(prevb, (75, 75))

index = 0
isplay = False  

pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play(-1)
isplay = True 

font2 = pygame.font.SysFont(None, 20)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if isplay:
                    pygame.mixer.music.pause()
                    isplay = False  
                else:
                    pygame.mixer.music.unpause()
                    isplay = True 

            elif event.key == pygame.K_RIGHT:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])  
                pygame.mixer.music.play(-1)

            elif event.key == pygame.K_LEFT:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play(-1)

            elif event.key == pygame.K_s: 
                pygame.mixer.music.stop()
                isplay = False

    screen.fill((0, 0, 0))

    bg_width, bg_height = background.get_size()
    bg_x = (width - bg_width) // 2
    bg_y = 50
    screen.blit(background, (bg_x, bg_y))

    bg = pygame.Surface((500, 200))
    bg.fill((255, 255, 255))
    screen.blit(bg, (155, 500))

    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))
    text_x = 155 + (500 - text2.get_width()) // 2
    screen.blit(text2, (text_x, 520))

    screen.blit(prevb, (273, 585))  
    screen.blit(nextb, (460, 587))  
    if isplay:
        screen.blit(pausb, (370, 590))  
    else:
        screen.blit(playb, (370, 590))  

    pygame.display.update()
    clock.tick(24)

pygame.quit()
