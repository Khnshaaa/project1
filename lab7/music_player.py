import pygame
import os  

pygame.init()

width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Playlist")
clock = pygame.time.Clock()

playlist = []
music_folder = "lab7/music_folder"

if not os.path.exists(music_folder):
    print(f"Error: Folder '{music_folder}' not found.")
    exit()

allmusic = os.listdir(music_folder)
for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))

if not playlist:
    print("Error: No MP3 files found in 'lab7/music_folder'.")
    exit()

image_folder = "lab7/imagee"
if not os.path.exists(image_folder):
    print(f"Error: Folder '{image_folder}' not found.")
    exit()

try:
    background_main = pygame.image.load(os.path.join(image_folder, "bgg.png"))
    background_main = pygame.transform.scale(background_main, (width, height))
    background = pygame.image.load(os.path.join(image_folder, "backgroundd.png"))
    playb = pygame.image.load(os.path.join(image_folder, "play.png"))
    pausb = pygame.image.load(os.path.join(image_folder, "pause.png"))
    nextb = pygame.image.load(os.path.join(image_folder, "next.png"))
    prevb = pygame.image.load(os.path.join(image_folder, "back.png"))
except FileNotFoundError as e:
    print(f"Error loading images: {e}")
    exit()

playb = pygame.transform.scale(playb, (70, 70))
pausb = pygame.transform.scale(pausb, (70, 70))
nextb = pygame.transform.scale(nextb, (70, 70))
prevb = pygame.transform.scale(prevb, (75, 75))

button_positions = {
    "prev": (273, 585),
    "play_pause": (370, 590),
    "next": (460, 587),
}

index = 0
isplay = False  

pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play(-1)
isplay = True 

font2 = pygame.font.SysFont(None, 20)

run = True
while run:
    screen.blit(background_main, (0, 0))
    
    bg_width, bg_height = background.get_size()
    bg_x = (width - bg_width) // 2
    bg_y = 50
    screen.blit(background, (bg_x, bg_y))

    bg = pygame.Surface((500, 200))
    bg.fill((255, 182, 193))
    screen.blit(bg, (155, 500))

    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))
    text_x = 155 + (500 - text2.get_width()) // 2
    screen.blit(text2, (text_x, 520))

    screen.blit(prevb, button_positions["prev"])  
    screen.blit(nextb, button_positions["next"])  
    if isplay:
        screen.blit(pausb, button_positions["play_pause"])  
    else:
        screen.blit(playb, button_positions["play_pause"])  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if isplay:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                isplay = not isplay

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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            buttons = {
                "prev": prevb,
                "play_pause": playb,
                "next": nextb,
            }
            for key, pos in button_positions.items():
                btn_x, btn_y = pos
                btn_width, btn_height = buttons[key].get_size()
                if btn_x <= x <= btn_x + btn_width and btn_y <= y <= btn_y + btn_height:
                    if key == "play_pause":
                        if isplay:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
                        isplay = not isplay
                    elif key == "next":
                        index = (index + 1) % len(playlist)
                        pygame.mixer.music.load(playlist[index])
                        pygame.mixer.music.play(-1)
                    elif key == "prev":
                        index = (index - 1) % len(playlist)
                        pygame.mixer.music.load(playlist[index])
                        pygame.mixer.music.play(-1)
    
    pygame.display.update()
    clock.tick(24)

pygame.mixer.music.stop()
pygame.quit()