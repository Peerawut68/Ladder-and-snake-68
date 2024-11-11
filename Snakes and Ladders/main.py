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

running = True
while running:

    bg('Home.png')

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()