import os
import pygame
import button
import random
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

#กำหนดชื่อเกมและไอคอน
pygame.display.set_caption("Snakes and Ladders")
icon = pygame.image.load("Picture/icon.png")
pygame.display.set_icon(icon)

#กำหนด FPS
clock = pygame.time.Clock()
FPS = 120

#กำหนดขนาดหน้าจอ
w = 1920
h = 1080
screen = pygame.display.set_mode((w,h))
def resize_screen():
    screen = pygame.display.set_mode((w, h))
    create_button()

#กำหนดพื้นหลัง
def bg(img):
    background = pygame.image.load(img)
    background_fixed = pygame.transform.scale(background,(w,h))
    screen.blit(background_fixed,(0,0))
    create_button()

#กำหนดชนิดและขนาดของ font 
f = pygame.font.Font("Chewy.ttf",52)
f2 = pygame.font.Font("Chewy.ttf",100)

#กำหนดสีข้อความ
txt_color = (0,21,1)

#กำหนดการสร้างข้อความ
def draw_text(text,font,text_color,x,y):
    write = font.render(text,True,text_color)
    if w == 1920 and h == 1080:
        screen.blit(write,(x,y))
    else:
        screen.blit(write,(x/1.5,y/1.5))

#โหลดรูปภาพ
play_img = pygame.image.load("Picture/button_play.png").convert_alpha()
option_img = pygame.image.load("Picture/button_option.png").convert_alpha()
how_img = pygame.image.load("Picture/button_how.png").convert_alpha()
quit_img = pygame.image.load("Picture/button_quit.png").convert_alpha()
back_img = pygame.image.load("Picture/button_back.png").convert_alpha()
pause_img = pygame.image.load("Picture/button_pause.png").convert_alpha()
resume_img = pygame.image.load("Picture/button_resume.png").convert_alpha()
options_img = pygame.image.load("Picture/button_options.png").convert_alpha()
home_img = pygame.image.load("Picture/button_home.png").convert_alpha()
thirty_img = pygame.image.load("Picture/button_30.png").convert_alpha()
sixty_img = pygame.image.load("Picture/button_60.png").convert_alpha()
twenty_img = pygame.image.load("Picture/button_120.png").convert_alpha()
hd_img = pygame.image.load("Picture/button_hd.png").convert_alpha()
fullhd_img = pygame.image.load("Picture/button_fullhd.png").convert_alpha()
on_img = pygame.image.load("Picture/button_on.png").convert_alpha()
off_img = pygame.image.load("Picture/button_off.png").convert_alpha()
random_img = pygame.image.load("Picture/button_random.png").convert_alpha()
player_01_img = pygame.image.load("Picture/player_01.png").convert_alpha()
player_02_img = pygame.image.load("Picture/player_02.png").convert_alpha()
player_03_img = pygame.image.load("Picture/player_03.png").convert_alpha()
player_04_img = pygame.image.load("Picture/player_04.png").convert_alpha()
dice_img = [pygame.image.load(f"Picture/dice_{i}.png") for i in range(1, 7)]

#ตัวละคร
def chr(x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        rect = image.get_rect()
        rect.topleft = (x, y)
        return image, rect.x, rect.y
def create_chr(player):
    if w == 1920 and h == 1080:
        if player == 1:
            image, x, y = chr(x1, y1, player_01_img, 1)
        elif player == 2:
            image, x, y = chr(x2, y2, player_02_img, 1)
        elif player == 3:  
            image, x, y = chr(x3, y3, player_03_img, 1)
        elif player == 4:
            image, x, y = chr(x4, y4, player_04_img, 1)
    elif w == 1280 and h == 720:
        if player == 1:
            image, x, y = chr(x1/1.5, y1/1.5, player_01_img, 1/1.5)
        elif player == 2:
            image, x, y = chr(x2/1.5, y2/1.5, player_02_img, 1/1.5)
        elif player == 3: 
            image, x, y = chr(x3/1.5, y3/1.5, player_03_img, 1/1.5)
        elif player == 4:
            image, x, y = chr(x4/1.5, y4/1.5, player_04_img, 1/1.5)
    screen.blit(image, (x, y))

#สร้างปุ่ม
def create_button():
    global random_button,screen,play_button,home_button,options_button,resume_button,pause_button,option_button,quit_button,how_button,back_button,thirty_button,sixty_button,twenty_button,hd_button,fullhd_button,on_music_button,off_music_button,on_sound_button,off_sound_button
    if w == 1920 and h == 1080:
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
        random_button = button.Button(859, 1010, random_img, 1)
    elif w == 1280 and h == 720:
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
        random_button = button.Button(573, 673, random_img, 1/1.5)

#ลุกเต๋า
def roll_dice():
    return random.randint(1, 10)

#บันได
def ladder():
    global x1, y1, x2, y2, x3, y3, x4, y4
    if x1 == 233 and y1 == 915:
        x1 = 328
        y1 = 845
    elif x2 == 283 and y2 == 925:
        x2 = 378
        y2 = 853
    elif x3 == 225 and y3 == 879:
        x3 = 320
        y3 = 810
    elif x4 == 287 and y4 == 879:
        x4 = 382
        y4 = 810
    elif x1 == 1088 and y1 == 915:
        x1 = 1183
        y1 = 845
    elif x2 == 1138 and y2 == 925:
        x2 = 1233
        y2 = 853
    elif x3 == 1080 and y3 == 879:
        x3 = 1175
        y3 = 810
    elif x4 == 1142 and y4 == 879:
        x4 = 1237
        y4 = 810
    elif x1 == 1088 and y1 == 775:
        x1 = 993
        y1 = 705
    elif x2 == 1138 and y2 == 781:
        x2 = 1043
        y2 = 709
    elif x3 == 1080 and y3 == 741:
        x3 = 985
        y3 = 672
    elif x4 == 1142 and y4 == 741:
        x4 = 1047
        y4 = 672
    elif x1 == 233 and y1 == 705:
        x1 = 423
        y1 = 425
    elif x2 == 283 and y2 == 709:
        x2 = 473
        y2 = 421
    elif x3 == 225 and y3 == 672:
        x3 = 415
        y3 = 396
    elif x4 == 287 and y4 == 672:
        x4 = 477
        y4 = 396
    elif x1 == 898 and y1 == 705:
        x1 = 993
        y1 = 635
    elif x2 == 948 and y2 == 709:
        x2 = 1043
        y2 = 637
    elif x3 == 890 and y3 == 672:
        x3 = 985
        y3 = 603
    elif x4 == 952 and y4 == 672:
        x4 = 1047
        y4 = 603
    elif x1 == 1563 and y1 == 705:
        x1 = 1658
        y1 = 565
    elif x2 == 1613 and y2 == 709:
        x2 = 1708
        y2 = 565
    elif x3 == 1555 and y3 == 672:
        x3 = 1650
        y3 = 534
    elif x4 == 1617 and y4 == 672:
        x4 = 1712
        y4 = 534
    elif x1 == 1468 and y1 == 635:
        x1 = 993
        y1 = 215
    elif x2 == 1518 and y2 == 637:
        x2 = 1043
        y2 = 205
    elif x3 == 1460 and y3 == 603:
        x3 = 985
        y3 = 189
    elif x4 == 1522 and y4 == 603:
        x4 = 1047
        y4 = 189
    elif x1 == 613 and y1 == 565:
        x1 = 708
        y1 = 425
    elif x2 == 663 and y2 == 565:
        x2 = 758
        y2 = 421
    elif x3 == 605 and y3 == 534:
        x3 = 700
        y3 = 396
    elif x4 == 667 and y4 == 534:
        x4 = 762
        y4 = 396
    elif x1 == 1563 and y1 == 495:
        x1 = 1563
        y1 = 425
    elif x2 == 1613 and y2 == 493:
        x2 = 1613
        y2 = 421
    elif x3 == 1555 and y3 == 465:
        x3 = 1555
        y3 = 396
    elif x4 == 1617 and y4 == 465:
        x4 = 1617
        y4 = 396
    elif x1 == 1088 and y1 == 495:
        x1 = 993
        y1 = 425
    elif x2 == 1138 and y2 == 493:
        x2 = 1043
        y2 = 421
    elif x3 == 1080 and y3 == 465:
        x3 = 985
        y3 = 396
    elif x4 == 1142 and y4 == 465:
        x4 = 1047
        y4 = 396
    elif x1 == 328 and y1 == 355:
        x1 = 233
        y1 = 285
    elif x2 == 378 and y2 == 349:
        x2 = 283
        y2 = 277
    elif x3 == 320 and y3 == 327:
        x3 = 225
        y3 = 258
    elif x4 == 382 and y4 == 327:
        x4 = 287
        y4 = 258
    elif x1 == 1563 and y1 == 285:
        x1 = 1468
        y1 = 145
    elif x2 == 1613 and y2 == 277:
        x2 = 1518
        y2 = 133
    elif x3 == 1555 and y3 == 258:
        x3 = 1460
        y3 = 120
    elif x4 == 1617 and y4 == 258:
        x4 = 1522
        y4 = 120
    elif x1 == 138 and y1 == 215:
        x1 = 233
        y1 = 145
    elif x2 == 188 and y2 == 205:
        x2 = 283
        y2 = 133
    elif x3 == 130 and y3 == 189:
        x3 = 225
        y3 = 120
    elif x4 == 192 and y4 == 189:
        x4 = 287
        y4 = 120
    elif x1 == 518 and y1 == 215:
        x1 = 613
        y1 = 145
    elif x2 == 568 and y2 == 205:
        x2 = 663
        y2 = 133
    elif x3 == 510 and y3 == 189:
        x3 = 605
        y3 = 120
    elif x4 == 572 and y4 == 189:
        x4 = 667
        y4 = 120

#งู
def snake():
    global x1, y1, x2, y2, x3, y3, x4, y4  
    if x1 == 423 and y1 == 775:
        x1 = 328
        y1 = 915
    elif x2 == 473 and y2 == 781:
        x2 = 378
        y2 = 925
    elif x3 == 415 and y3 == 741:
        x3 = 320
        y3 = 879
    elif x4 == 477 and y4 == 741:
        x4 = 477
        y4 = 879
    elif x1 == 803 and y1 == 705:
        x1 = 708
        y1 = 845
    elif x2 == 853 and y2 == 709:
        x2 = 758
        y2 = 853
    elif x3 == 795 and y3 == 672:
        x3 = 700
        y3 = 810
    elif x4 == 857 and y4 == 672:
        x4 = 762
        y4 = 810
    elif x1 == 1278 and y1 == 705:
        x1 = 1468
        y1 = 915
    elif x2 == 1328 and y2 == 709:
        x2 = 1518
        y2 = 925
    elif x3 == 1270 and y3 == 672:
        x3 = 1460
        y3 = 879
    elif x4 == 1332 and y4 == 672:
        x4 = 1522
        y4 = 879
    elif x1 == 1658 and y1 == 775:
        x1 = 1563
        y1 = 845
    elif x2 == 1708 and y2 == 781:
        x2 = 1613
        y2 = 853
    elif x3 == 1650 and y3 == 741:
        x3 = 1555
        y3 = 810
    elif x4 == 1712 and y4 == 741:
        x4 = 1617
        y4 = 810
    elif x1 == 803 and y1 == 215:
        x1 = 803
        y1 = 635
    elif x2 == 853 and y2 == 205:
        x2 = 853
        y2 = 637
    elif x3 == 795 and y3 == 189:
        x3 = 795
        y3 = 603
    elif x4 == 857 and y4 == 189:
        x4 = 857
        y4 = 603
    elif x1 == 993 and y1 == 425:
        x1 = 898
        y1 = 565
    elif x2 == 1043 and y2 == 421:
        x2 = 948
        y2 = 565
    elif x3 == 985 and y3 == 396:
        x3 = 890
        y3 = 534
    elif x4 == 1047 and y4 == 396:
        x4 = 952
        y4 = 534
    elif x1 == 1563 and y1 == 425:
        x1 = 1278
        y1 = 565
    elif x2 == 1613 and y2 == 421:
        x2 = 1328
        y2 = 565
    elif x3 == 1555 and y3 == 396:
        x3 = 1270
        y3 = 534
    elif x4 == 1617 and y4 == 396:
        x4 = 1332
        y4 = 534
    elif x1 == 328 and y1 == 145:
        x1 = 613
        y1 = 355
    elif x2 == 378 and y2 == 133:
        x2 = 663
        y2 = 349
    elif x3 == 320 and y3 == 120:
        x3 = 605
        y3 = 327
    elif x4 == 382 and y4 == 120:
        x4 = 667
        y4 = 327
    elif x1 == 803 and y1 == 145:
        x1 = 708
        y1 = 215
    elif x2 == 853 and y2 == 133:
        x2 = 758
        y2 = 205
    elif x3 == 795 and y3 == 120:
        x3 = 700
        y3 = 189
    elif x4 == 857 and y4 == 120:
        x4 = 762
        y4 = 189
    elif x1 == 898 and y1 == 215:
        x1 = 993
        y1 = 285
    elif x2 == 948 and y2 == 205:
        x2 = 1043
        y2 = 277
    elif x3 == 890 and y3 == 189:
        x3 = 985
        y3 = 258
    elif x4 == 952 and y4 == 189:
        x4 = 1047
        y4 = 258
    elif x1 == 1278 and y1 == 145:
        x1 = 1373
        y1 = 285
    elif x2 == 1328 and y2 == 133:
        x2 = 1423
        y2 = 277
    elif x3 == 1270 and y3 == 120:
        x3 = 1365
        y3 = 258
    elif x4 == 1332 and y4 == 120:
        x4 = 1427
        y4 = 258

#ระเบิด
def bomb():
    global x1, y1, x2, y2, x3, y3, x4, y4
    if x1 == 898 and y1 == 915:
        x1 = 613
        y1 = 915
    elif x2 == 948 and y2 == 925:
        x2 = 663
        y2 = 925
    elif x3 == 890 and y3 == 879:
        x3 = 605
        y3 = 879
    elif x4 == 952 and y4 == 879:
        x4 = 667
        y4 = 879
    elif x1 == 708 and y1 == 845:
        x1 = 993
        y1 = 845
    elif x2 == 758 and y2 == 853:
        x2 = 1043
        y2 = 853
    elif x3 == 700 and y3 == 810:
        x3 = 985
        y3 = 810
    elif x4 == 762 and y4 == 810:
        x4 = 1047
        y4 = 810
    elif x1 == 708 and y1 == 285:
        x1 = 993
        y1 = 285
    elif x2 == 758 and y2 == 277:
        x2 = 1043
        y2 = 277
    elif x3 == 700 and y3 == 258:
        x3 = 985
        y3 = 258
    elif x4 == 762 and y4 == 258:
        x4 = 1047
        y4 = 258
    elif x1 == 1183 and y1 == 215:
        x1 = 898
        y1 = 215
    elif x2 == 1233 and y2 == 205:
        x2 = 948
        y2 = 205
    elif x3 == 1175 and y3 == 189:
        x3 = 890
        y3 = 189
    elif x4 == 1237 and y4 == 189:
        x4 = 952
        y4 = 189
    elif x1 == 1088 and y1 == 145:
        x1 = 1373
        y1 = 145
    elif x2 == 1138 and y2 == 133:
        x2 = 1423
        y2 = 133
    elif x3 == 1080 and y3 == 120:
        x3 = 1365
        y3 = 120
    elif x4 == 1142 and y4 == 120:
        x4 = 1427
        y4 = 120

#กลับไปจุด checkpoints
def checkpoints():
    global x1, y1, x2, y2, x3, y3, x4, y4
    if x1 == 993 and y1 == 845:
        x1 = 138
        y1 = 915
    elif x2 == 1043 and y2 == 853:
        x2 = 188
        y2 = 925
    elif x3 == 985 and y3 == 810:
        x3 = 130
        y3 = 879
    elif x4 == 1047 and y4 == 810:
        x4 = 192
        y4 = 879
    elif x1 == 233 and y1 == 635:
        x1 = 138
        y1 = 705
    elif x2 == 283 and y2 == 637:
        x2 = 188
        y2 = 709
    elif x3 == 225 and y3 == 603:
        x3 = 130
        y3 = 672
    elif x4 == 287 and y4 == 603:
        x4 = 192
        y4 = 672
    elif x1 == 138 and y1 == 355:
        x1 = 1563
        y1 = 565
    elif x2 == 188 and y2 == 349:
        x2 = 1613
        y2 = 565
    elif x3 == 130 and y3 == 327:
        x3 = 1555
        y3 = 534
    elif x4 == 192 and y4 == 327:
        x4 = 1617
        y4 = 534
    elif x1 == 518 and y1 == 145:
        x1 = 898
        y1 = 215
    elif x2 == 568 and y2 == 133:
        x2 = 948
        y2 = 205
    elif x3 == 510 and y3 == 120:
        x3 = 890
        y3 = 189
    elif x4 == 572 and y4 == 120:
        x4 = 952
        y4 = 189

#คุก
time_break = 0
def stop_turn():
    global time_break  
    if x1 == 518 and y1 == 705:
        time_break = 1
    elif x2 == 568 and y2 == 709:
        time_break = 1
    elif x3 == 510 and y3 == 672:
        time_break = 1
    elif x4 == 572 and y4 == 672:
        time_break = 1
    elif x1 == 1183 and y1 == 705:
        time_break = 1
    elif x2 == 1233 and y2 == 709:
        time_break = 1
    elif x3 == 1175 and y3 == 672:
        time_break = 1    
    elif x4 == 1237 and y4 == 672:
        time_break = 1
    elif x1 == 803 and y1 == 495:
        time_break = 1    
    elif x2 == 853 and y2 == 493:
        time_break = 1   
    elif x3 == 795 and y3 == 465:
        time_break = 1   
    elif x4 == 857 and y4 == 465:
        time_break = 1
    elif x1 == 1373 and y1 == 145:
        time_break = 1
    elif x2 == 1423 and y2 == 133:
        time_break = 1
    elif x3 == 1365 and y3 == 120:
        time_break = 1    
    elif x4 == 1427 and y4 == 120: 
        time_break = 1

#การแสดงผลหน้าต่างๆ
def draw_home():
    global turn, order, x1, y1, x2, y2, x3, y3, x4, y4
    bg("Picture/Home.png")
    if play_button.draw(screen):
        pygame.time.delay(150)
        turn = 1
        order = 0
        x1 = 138
        y1 = 915
        x2 = 188
        y2 = 925
        x3 = 130
        y3 = 879
        x4 = 192
        y4 = 879
        return 'game'
    if option_button.draw(screen):
        pygame.time.delay(150)
        return 'option_home'
    if how_button.draw(screen):
        pygame.time.delay(150)
        return 'how'
    if quit_button.draw(screen):
        pygame.time.delay(150)
        return 'quit'
    return 'home'
turn = 1
order = 0
x1 = 138
y1 = 915
x2 = 188
y2 = 925
x3 = 130
y3 = 879
x4 = 192
y4 = 879
def draw_game():
    global turn, order, x1, y1, x2, y2, x3, y3, x4, y4, time_break
    bg("Picture/Background.png")
    if pause_button.draw(screen):
        pygame.time.delay(100)
        return 'pause'
    if random_button.draw(screen):
        pygame.time.delay(100)
        if turn == 1:
            if order < 4 :
                dice = roll_dice()
                order += 1
                bg("Picture/Background.png")
                draw_text(str(dice),f2,(0,0,0),0,0)
                pygame.display.update()
                pygame.time.delay(1000)
            else:
                turn += 1
                order = 0
        else:
            if order < 4 :
                if order == 0 :
                    dice = roll_dice()
                    order += 1
                    for i in range(dice):
                        if y1 in (915, 775, 635, 495, 355, 215):
                            x1 += 95
                            if x1 > 1658:
                                y1 -= 70
                                x1 = 1658
                        elif y1 in (845, 705, 565, 425, 285, 145):
                            x1 -= 95
                            if x1 < 138:
                                y1 -= 70
                                x1 = 138
                        bg("Picture/Background.png")
                        draw_text(str(dice),f2,(0,0,0),0,0)
                        create_chr(3)
                        create_chr(4)
                        create_chr(1)
                        create_chr(2)
                        pygame.display.update()
                        pygame.time.delay(500)
                    ladder()
                    snake()
                    bomb()
                    checkpoints()
                elif order == 1 :
                    dice = roll_dice()
                    order += 1
                    for i in range(dice):
                        if y2 in (925, 781, 637, 493, 349, 205):
                            x2 += 95
                            if x2 > 1708:
                                y2 -= 72
                                x2 = 1708
                        elif y2 in (853, 709, 565, 421, 277, 133):
                            x2 -= 95
                            if x2 < 188:
                                y2 -= 72
                                x2 = 188
                        bg("Picture/Background.png")
                        draw_text(str(dice),f2,(0,0,0),0,0)
                        create_chr(3)
                        create_chr(4)
                        create_chr(1)
                        create_chr(2)
                        pygame.display.update()
                        pygame.time.delay(500)
                    ladder()
                    snake()
                    bomb()
                    checkpoints()
                elif order == 2 :
                    dice = roll_dice()
                    order += 1
                    for i in range(dice):
                        if y3 in (879, 741, 603, 465, 327, 189):
                            x3 += 95
                            if x3 > 1650:
                                y3 -= 69
                                x3 = 1650
                        elif y3 in (810, 672, 534, 396, 258, 120):
                            x3 -= 95
                            if x3 < 130:
                                y3 -= 69
                                x3 = 130
                        bg("Picture/Background.png")
                        draw_text(str(dice),f2,(0,0,0),0,0)
                        create_chr(3)
                        create_chr(4)
                        create_chr(1)
                        create_chr(2)
                        pygame.display.update()
                        pygame.time.delay(500)
                    ladder()
                    snake()
                    bomb()
                    checkpoints()
                elif order == 3 :
                    dice = roll_dice()
                    order += 1
                    for i in range(dice):
                        if y4 in (879, 741, 603, 465, 327, 189):
                            x4 += 95
                            if x4 > 1712:
                                y4 -= 69
                                x4 = 1712
                        elif y4 in (810, 672, 534, 396, 258, 120):
                            x4 -= 95
                            if x4 < 192:
                                y4 -= 69
                                x4 = 192
                        bg("Picture/Background.png")
                        draw_text(str(dice),f2,(0,0,0),0,0)
                        create_chr(3)
                        create_chr(4)
                        create_chr(1)
                        create_chr(2)
                        pygame.display.update()
                        pygame.time.delay(500)
                    ladder()
                    snake()
                    bomb()
                    checkpoints()
            elif order == 4 :
                order = 0
                turn += 1
    return 'game'
def draw_option_home():
    global FPS, w, h
    bg("Picture/Option.png")
    if back_button.draw(screen):
        pygame.time.delay(150)
        return 'home'
    if thirty_button.draw(screen):
        pygame.time.delay(150)
        FPS = 30
        draw_text('Successful !',f,(0,255,0),1670,0)
        pygame.display.update()
        pygame.time.delay(1000)
    if sixty_button.draw(screen):
        pygame.time.delay(150)
        FPS = 60
        draw_text('Successful !',f,(0,255,0),1670,0)
        pygame.display.update()
        pygame.time.delay(1000)
    if twenty_button.draw(screen):
        pygame.time.delay(150)
        FPS = 120
        draw_text('Successful !',f,(0,255,0),1670,0)
        pygame.display.update()
        pygame.time.delay(1000)
    if hd_button.draw(screen):
        pygame.time.delay(150)
        w = 1280
        h = 720
        resize_screen()
    if fullhd_button.draw(screen):
        pygame.time.delay(150)
        w = 1920
        h = 1080
        resize_screen()
    if on_music_button.draw(screen):
        pygame.time.delay(150)
        return 'home'
    if off_music_button.draw(screen):
        pygame.time.delay(150)
        return 'home'
    if on_sound_button.draw(screen):
        pygame.time.delay(150)
        return 'home'
    if off_sound_button.draw(screen):
        pygame.time.delay(150)
        return 'home'
    return 'option_home'
def draw_option_game():
    global FPS, w, h
    bg("Picture/Option.png")
    if back_button.draw(screen):
        pygame.time.delay(150)
        return 'pause'
    if thirty_button.draw(screen):
        pygame.time.delay(150)
        FPS = 30
        draw_text('Successful !',f,(0,255,0),1670,0)
        pygame.display.update()
        pygame.time.delay(1000)
    if sixty_button.draw(screen):
        pygame.time.delay(150)
        FPS = 60
        draw_text('Successful !',f,(0,255,0),1670,0)
        pygame.display.update()
        pygame.time.delay(1000)
    if twenty_button.draw(screen):
        pygame.time.delay(150)
        FPS = 120
        draw_text('Successful !',f,(0,255,0),1670,0)
        pygame.display.update()
        pygame.time.delay(1000)
    if hd_button.draw(screen):
        pygame.time.delay(150)
        w = 1280
        h = 720
        resize_screen()
    if fullhd_button.draw(screen):
        pygame.time.delay(150)
        w = 1920
        h = 1080
        resize_screen()
    if on_music_button.draw(screen):
        pygame.time.delay(150)
        return 'home'
    if off_music_button.draw(screen):
        pygame.time.delay(150)
        return 'home'
    if on_sound_button.draw(screen):
        pygame.time.delay(150)
        return 'home'
    if off_sound_button.draw(screen):
        pygame.time.delay(150)
        return 'home'
    return 'option_game'
def draw_how():
    bg("Picture/HowToPlay.png")
    if back_button.draw(screen):
        pygame.time.delay(150)
        return 'home'
    return 'how'
def draw_pause():
    bg("Picture/Background_pause.png")
    if resume_button.draw(screen):
        pygame.time.delay(150)
        return 'game'
    if options_button.draw(screen):
        pygame.time.delay(150)
        return 'option_game'
    if home_button.draw(screen):
        pygame.time.delay(150)
        return 'home'
    return 'pause'

page = 'home'
running = True
while running:
   
    if page == 'home':
        page = draw_home()
    elif page == 'game':
        page = draw_game()
        create_chr(3)
        create_chr(4)
        create_chr(1)
        create_chr(2)
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
            if event.key == pygame.K_ESCAPE:
                if page == 'pause':
                    page = 'game'
                elif page == 'game':
                    page = 'pause'
                elif page == 'option_home':
                    page = 'home'
                elif page == 'option_game':
                    page = 'pause'
                elif page == 'how':
                    page = 'home'
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()