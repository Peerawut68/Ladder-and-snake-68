import pygame
import button
pygame.init()

#กำหนดชื่อเกมและไอคอน
pygame.display.set_caption("Snakes and Ladders")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#กำหนดขนาดหน้าจอ
x = 1280
y = 720
screen = pygame.display.set_mode((x,y))

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
option_img = pygame.image.load("button_options.png").convert_alpha()
how_img = pygame.image.load("button_how.png").convert_alpha()
quit_img = pygame.image.load("button_quit.png").convert_alpha()
back_img = pygame.image.load("button_back.png").convert_alpha()

#สร้างปุ่ม
if x == 1920 and y == 1080:
    play_button = button.Button(752, 463, play_img, 1)
    option_button = button.Button(752, 619, option_img, 1)
    how_button = button.Button(751, 774, how_img, 1)
    quit_button = button.Button(752, 928, quit_img, 1)
    back_button = button.Button(58, 1005, back_img, 1/2)
elif x == 1280 and y == 720:
    play_button = button.Button(501, 309, play_img, 1/1.5)
    option_button = button.Button(501, 413, option_img, 1/1.5)
    how_button = button.Button(501, 517, how_img, 1/1.5)
    quit_button = button.Button(501, 619, quit_img, 1/1.5)
    back_button = button.Button(45, 670, back_img, 1/3)

#การแสดงผลหน้าต่างๆ
def draw_home():
    bg("Home.png")
    if play_button.draw(screen):
        return 'game'
    if option_button.draw(screen):
        return 'option'
    if how_button.draw(screen):
        return 'how'
    if quit_button.draw(screen):
        return 'quit'
    return 'home'
def draw_game():
    bg("Background.png")
    
def draw_option():
    bg("Option.png")

    return 'option'

def draw_how():
    bg("HowToPlay.png")
    if back_button.draw(screen):
        return 'home'
    return 'how'

page = 'home'
running = True
while running:
   
    if page == 'home':
        page = draw_home()
    elif page == 'game':
        page = draw_game()
    elif page == 'option':
        page = draw_option()
    elif page == 'how':
        page = draw_how()
    elif page == 'quit':
        running = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()