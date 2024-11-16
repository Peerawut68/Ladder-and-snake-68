import os
import pygame
import button
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

#กำหนดชื่อเกมและไอคอน
pygame.display.set_caption("Snakes and Ladders")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#กำหนด FPS
clock = pygame.time.Clock()
FPS = 120

#กำหนดขนาดหน้าจอ
x = 1920
y = 1080
screen = pygame.display.set_mode((x,y))

def resize_screen():
    global screen,play_button,home_button,options_button,resume_button,pause_button,option_button,quit_button,how_button,back_button,thirty_button,sixty_button,twenty_button,hd_button,fullhd_button,on_music_button,off_music_button,on_sound_button,off_sound_button
    screen = pygame.display.set_mode((x, y))
    if x == 1920 and y == 1080:
        play_button = button.Button(752, 463, play_img, 1)
        option_button = button.Button(752, 619, option_img, 1)
        how_button = button.Button(751, 774, how_img, 1)
        quit_button = button.Button(752, 928, quit_img, 1)
        back_button = button.Button(58, 1005, back_img, 1/2)
        pause_button = button.Button(836, 5, pause_img, 1)
        resume_button = button.Button(748, 215, resume_img, 1)
        options_button = button.Button(748, 485, options_img, 1)
        home_button = button.Button(748, 761, home_img, 1)
        thirty_button = button.Button(448, 198, thirty_img, 1)
        sixty_button = button.Button(825, 198, sixty_img, 1)
        twenty_button = button.Button(1201, 198, twenty_img, 1)
        hd_button = button.Button(635, 427, hd_img, 1)
        fullhd_button = button.Button(1013, 427, fullhd_img, 1)
        on_music_button = button.Button(636, 657, on_img, 1)
        off_music_button = button.Button(1012, 657, off_img, 1)
        on_sound_button = button.Button(636, 886, on_img, 1)
        off_sound_button = button.Button(1013, 886, off_img, 1)
    elif x == 1280 and y == 720:
        play_button = button.Button(501, 309, play_img, 1/1.5)
        option_button = button.Button(501, 413, option_img, 1/1.5)
        how_button = button.Button(501, 517, how_img, 1/1.5)
        quit_button = button.Button(501, 619, quit_img, 1/1.5)
        back_button = button.Button(45, 670, back_img, 1/3)
        pause_button = button.Button(557, 3, pause_img, 1/1.5)
        resume_button = button.Button(499, 143, resume_img, 1/1.5)
        options_button = button.Button(499, 323, options_img, 1/1.5)
        home_button = button.Button(499, 507, home_img, 1/1.5)
        thirty_button = button.Button(299, 132, thirty_img, 1/1.5)
        sixty_button = button.Button(550, 132, sixty_img, 1/1.5)
        twenty_button = button.Button(801, 132, twenty_img, 1/1.5)
        hd_button = button.Button(423, 285, hd_img, 1/1.5)
        fullhd_button = button.Button(675, 285, fullhd_img, 1/1.5)
        on_music_button = button.Button(424, 438, on_img, 1/1.5)
        off_music_button = button.Button(675, 438, off_img, 1/1.5)
        on_sound_button = button.Button(424, 591, on_img, 1/1.5)
        off_sound_button = button.Button(675, 591, off_img, 1/1.5)

#กำหนดพื้นหลัง
def bg(img):
    background = pygame.image.load(img)
    background_fixed = pygame.transform.scale(background,(x,y))
    screen.blit(background_fixed,(0,0))

#กำหนดชนิดและขนาดของ font 
f = pygame.font.Font("Chewy.ttf",52)

#กำหนดสีข้อความ
txt_color = (0,21,1)

#กำหนดการสร้างข้อความ
def draw_text(text,font,text_color,x,y):
    write = font.render(text,True,text_color)
    screen.blit(write,(x,y))

#โหลดรูปภาพปุ่ม
play_img = pygame.image.load("button_play.png").convert_alpha()
option_img = pygame.image.load("button_option.png").convert_alpha()
how_img = pygame.image.load("button_how.png").convert_alpha()
quit_img = pygame.image.load("button_quit.png").convert_alpha()
back_img = pygame.image.load("button_back.png").convert_alpha()
pause_img = pygame.image.load("button_pause.png").convert_alpha()
resume_img = pygame.image.load("button_resume.png").convert_alpha()
options_img = pygame.image.load("button_options.png").convert_alpha()
home_img = pygame.image.load("button_home.png").convert_alpha()
thirty_img = pygame.image.load("button_30.png").convert_alpha()
sixty_img = pygame.image.load("button_60.png").convert_alpha()
twenty_img = pygame.image.load("button_120.png").convert_alpha()
hd_img = pygame.image.load("button_hd.png").convert_alpha()
fullhd_img = pygame.image.load("button_fullhd.png").convert_alpha()
on_img = pygame.image.load("button_on.png").convert_alpha()
off_img = pygame.image.load("button_off.png").convert_alpha()

#สร้างปุ่ม
if x == 1920 and y == 1080:
    play_button = button.Button(752, 463, play_img, 1)
    option_button = button.Button(752, 619, option_img, 1)
    how_button = button.Button(751, 774, how_img, 1)
    quit_button = button.Button(752, 928, quit_img, 1)
    back_button = button.Button(58, 1005, back_img, 1/2)
    pause_button = button.Button(836, 5, pause_img, 1)
    resume_button = button.Button(748, 215, resume_img, 1)
    options_button = button.Button(748, 485, options_img, 1)
    home_button = button.Button(748, 761, home_img, 1)
    thirty_button = button.Button(448, 198, thirty_img, 1)
    sixty_button = button.Button(825, 198, sixty_img, 1)
    twenty_button = button.Button(1201, 198, twenty_img, 1)
    hd_button = button.Button(635, 427, hd_img, 1)
    fullhd_button = button.Button(1013, 427, fullhd_img, 1)
    on_music_button = button.Button(636, 657, on_img, 1)
    off_music_button = button.Button(1012, 657, off_img, 1)
    on_sound_button = button.Button(636, 886, on_img, 1)
    off_sound_button = button.Button(1013, 886, off_img, 1)
elif x == 1280 and y == 720:
    play_button = button.Button(501, 309, play_img, 1/1.5)
    option_button = button.Button(501, 413, option_img, 1/1.5)
    how_button = button.Button(501, 517, how_img, 1/1.5)
    quit_button = button.Button(501, 619, quit_img, 1/1.5)
    back_button = button.Button(45, 670, back_img, 1/3)
    pause_button = button.Button(557, 3, pause_img, 1/1.5)
    resume_button = button.Button(499, 143, resume_img, 1/1.5)
    options_button = button.Button(499, 323, options_img, 1/1.5)
    home_button = button.Button(499, 507, home_img, 1/1.5)
    thirty_button = button.Button(299, 132, thirty_img, 1/1.5)
    sixty_button = button.Button(550, 132, sixty_img, 1/1.5)
    twenty_button = button.Button(801, 132, twenty_img, 1/1.5)
    hd_button = button.Button(423, 285, hd_img, 1/1.5)
    fullhd_button = button.Button(675, 285, fullhd_img, 1/1.5)
    on_music_button = button.Button(424, 438, on_img, 1/1.5)
    off_music_button = button.Button(675, 438, off_img, 1/1.5)
    on_sound_button = button.Button(424, 591, on_img, 1/1.5)
    off_sound_button = button.Button(675, 591, off_img, 1/1.5)

#การแสดงผลหน้าต่างๆ
def draw_home():
    bg("Home.png")
    if play_button.draw(screen):
        pygame.time.delay(100)
        return 'game'
    if option_button.draw(screen):
        pygame.time.delay(100)
        return 'option_home'
    if how_button.draw(screen):
        pygame.time.delay(100)
        return 'how'
    if quit_button.draw(screen):
        pygame.time.delay(100)
        return 'quit'
    return 'home'
def draw_game():
    bg("Background.png")
    if pause_button.draw(screen):
        pygame.time.delay(100)
        return 'pause'
    return 'game'
    
def draw_option_home():
    global FPS, x, y
    bg("Option.png")
    if back_button.draw(screen):
        pygame.time.delay(100)
        return 'home'
    if thirty_button.draw(screen):
        pygame.time.delay(100)
        FPS = 30
    if sixty_button.draw(screen):
        pygame.time.delay(100)
        FPS = 60
    if twenty_button.draw(screen):
        pygame.time.delay(100)
        FPS = 120
    if hd_button.draw(screen):
        pygame.time.delay(100)
        x = 1280
        y = 720
        resize_screen()
    if fullhd_button.draw(screen):
        pygame.time.delay(100)
        x = 1920
        y = 1080
        resize_screen()
    if on_music_button.draw(screen):
        pygame.time.delay(100)
        return 'home'
    if off_music_button.draw(screen):
        pygame.time.delay(100)
        return 'home'
    if on_sound_button.draw(screen):
        pygame.time.delay(100)
        return 'home'
    if off_sound_button.draw(screen):
        pygame.time.delay(100)
        return 'home'
    return 'option_home'

def draw_option_game():
    global FPS, x, y
    bg("Option.png")
    if back_button.draw(screen):
        pygame.time.delay(100)
        return 'pause'
    if thirty_button.draw(screen):
        pygame.time.delay(100)
        FPS = 30
    if sixty_button.draw(screen):
        pygame.time.delay(100)
        FPS = 60
    if twenty_button.draw(screen):
        pygame.time.delay(100)
        FPS = 120
    if hd_button.draw(screen):
        pygame.time.delay(100)
        x = 1280
        y = 720
        resize_screen()
    if fullhd_button.draw(screen):
        pygame.time.delay(100)
        x = 1920
        y = 1080
        resize_screen()
    if on_music_button.draw(screen):
        pygame.time.delay(100)
        return 'home'
    if off_music_button.draw(screen):
        pygame.time.delay(100)
        return 'home'
    if on_sound_button.draw(screen):
        pygame.time.delay(100)
        return 'home'
    if off_sound_button.draw(screen):
        pygame.time.delay(100)
        return 'home'
    return 'option_game'

def draw_how():
    bg("HowToPlay.png")
    if back_button.draw(screen):
        pygame.time.delay(100)
        return 'home'
    return 'how'

def draw_pause():
    bg("Background_pause.png")
    if resume_button.draw(screen):
        pygame.time.delay(100)
        return 'game'
    if options_button.draw(screen):
        pygame.time.delay(100)
        return 'option_game'
    if home_button.draw(screen):
        pygame.time.delay(100)
        return 'home'
    return 'pause'

page = 'home'
running = True
while running:
   
    if page == 'home':
        page = draw_home()
    elif page == 'game':
        page = draw_game()
    elif page == 'option_home':
        page = draw_option_home()
    elif page == 'option_game':
        page = draw_option_game()
    elif page == 'how':
        page = draw_how()
    elif page == 'pause':
        page = draw_pause()
    elif page == 'quit':
        running = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()