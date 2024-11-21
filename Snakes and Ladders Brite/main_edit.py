import os
import pygame
import button

# กำหนดค่าพื้นฐานของเกม
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.display.set_caption("Snakes and Ladders")
icon = pygame.image.load("Picture/icon.png")
pygame.display.set_icon(icon)

# ค่าพื้นฐานและการตั้งค่า
clock = pygame.time.Clock()
FPS = 120
w, h = 1920, 1080
screen = pygame.display.set_mode((w, h))

# โหลดฟอนต์
f = pygame.font.Font("Chewy.ttf", 52)
f2 = pygame.font.Font("Chewy.ttf", 100)

# โหลดรูปภาพปุ่ม
images = {
    "play": pygame.image.load("Picture/button_play.png").convert_alpha(),
    "option": pygame.image.load("Picture/button_option.png").convert_alpha(),
    "how": pygame.image.load("Picture/button_how.png").convert_alpha(),
    "quit": pygame.image.load("Picture/button_quit.png").convert_alpha(),
    "back": pygame.image.load("Picture/button_back.png").convert_alpha(),
    "pause": pygame.image.load("Picture/button_pause.png").convert_alpha(),
    "resume": pygame.image.load("Picture/button_resume.png").convert_alpha(),
    "options": pygame.image.load("Picture/button_options.png").convert_alpha(),
    "home": pygame.image.load("Picture/button_home.png").convert_alpha(),
    "thirty": pygame.image.load("Picture/button_30.png").convert_alpha(),
    "sixty": pygame.image.load("Picture/button_60.png").convert_alpha(),
    "twenty": pygame.image.load("Picture/button_120.png").convert_alpha(),
    "hd": pygame.image.load("Picture/button_hd.png").convert_alpha(),
    "fullhd": pygame.image.load("Picture/button_fullhd.png").convert_alpha(),
    "on": pygame.image.load("Picture/button_on.png").convert_alpha(),
    "off": pygame.image.load("Picture/button_off.png").convert_alpha(),
    "random": pygame.image.load("Picture/button_random.png").convert_alpha(),
}

# ฟังก์ชันช่วยเหลือ
def resize_screen():
    global screen
    screen = pygame.display.set_mode((w, h))
    create_button()

def bg(img):
    background = pygame.image.load(img)
    background_fixed = pygame.transform.scale(background, (w, h))
    screen.blit(background_fixed, (0, 0))

def draw_text(text, font, text_color, x, y):
    write = font.render(text, True, text_color)
    scale_factor = 1.5 if w == 1280 else 1
    screen.blit(write, (x / scale_factor, y / scale_factor))

# สร้างปุ่ม
def create_button():
    global buttons
    scale = 1 if w == 1920 else 1 / 1.5
    offset = 1 if w == 1920 else 1.5

    buttons = {
        "play": button.Button(752 / offset, 463 / offset, images["play"], scale),
        "option": button.Button(752 / offset, 619 / offset, images["option"], scale),
        "how": button.Button(751 / offset, 774 / offset, images["how"], scale),
        "quit": button.Button(752 / offset, 928 / offset, images["quit"], scale),
        "back": button.Button(58 / offset, 1005 / offset, images["back"], scale / 2),
        "pause": button.Button(836 / offset, 5 / offset, images["pause"], scale),
        "resume": button.Button(748 / offset, 215 / offset, images["resume"], scale),
        "options": button.Button(748 / offset, 485 / offset, images["options"], scale),
        "home": button.Button(748 / offset, 761 / offset, images["home"], scale),
        "random": button.Button(859 / offset, 1010 / offset, images["random"], scale),
        # ปุ่มปรับเฟรมเรต
        "30fps": button.Button(448 / offset, 198 / offset, images["thirty"], scale),
        "60fps": button.Button(825 / offset, 198 / offset, images["sixty"], scale),
        "120fps": button.Button(1201 / offset, 198 / offset, images["twenty"], scale),
        # ปุ่มความละเอียด
        "hd": button.Button(635 / offset, 427 / offset, images["hd"], scale),
        "fullhd": button.Button(1013 / offset, 427 / offset, images["fullhd"], scale),
    }

# การจัดการหน้าจอ
def draw_home():
    global turn, order, x1, y1, x2, y2, x3, y3, x4, y4
    bg("Picture/Home.png")
    if buttons["play"].draw(screen):
        reset_game()
        return 'game'
    if buttons["option"].draw(screen):
        return 'option_home'
    if buttons["how"].draw(screen):
        return 'how'
    if buttons["quit"].draw(screen):
        return 'quit'
    return 'home'

def draw_game():
    bg("Picture/Background.png")
    if buttons["pause"].draw(screen):
        return 'pause'
    if buttons["random"].draw(screen):
        pygame.time.delay(100)
    return 'game'

def draw_option_home():
    global FPS, w, h
    bg("Picture/Option.png")
    if buttons["back"].draw(screen):
        return 'home'
    if buttons["30fps"].draw(screen):
        set_fps(30)
    if buttons["60fps"].draw(screen):
        set_fps(60)
    if buttons["120fps"].draw(screen):
        set_fps(120)
    if buttons["hd"].draw(screen):
        set_resolution(1280, 720)
    if buttons["fullhd"].draw(screen):
        set_resolution(1920, 1080)
    return 'option_home'

# ฟังก์ชันปรับเฟรมเรตและความละเอียด
def set_fps(new_fps):
    global FPS
    FPS = new_fps
    draw_text('Successful !', f, (0, 255, 0), 1670, 0)
    pygame.display.update()
    pygame.time.delay(1000)

def set_resolution(width, height):
    global w, h
    w, h = width, height
    resize_screen()

# ฟังก์ชันเริ่มเกมใหม่
def reset_game():
    global turn, order, x1, y1, x2, y2, x3, y3, x4, y4
    order = 0
    x1, y1, x2, y2 = 138, 915, 188, 925
    x3, y3, x4, y4 = 130, 879, 192, 879

# ลูปหลักของเกม
page = 'home'
running = True
create_button()

while running:
    if page == 'home':
        page = draw_home()
    elif page == 'game':
        page = draw_game()
    elif page == 'option_home':
        page = draw_option_home()
    elif page == 'quit':
        running = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if page == 'game':
                page = 'pause'
            elif page == 'pause':
                page = 'game'
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
