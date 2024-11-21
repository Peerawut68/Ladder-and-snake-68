import pygame
import random
from pyvidplayer import Video
pygame.init()

#โหลดรูปภาพ
player_01_img = pygame.image.load("Picture/player_01.png").convert_alpha()
player_02_img = pygame.image.load("Picture/player_02.png").convert_alpha()
player_03_img = pygame.image.load("Picture/player_03.png").convert_alpha()
player_04_img = pygame.image.load("Picture/player_04.png").convert_alpha()

#โหลดวิดีโอ
vid = Video("Video/dice_roll.mp4")
vid.set_size((w, h))

#ลุกเต๋า
def roll_dice():
    random.randint(1, 10) = dice
    vid.draw(screen, (0, 0))
    pygame.display.update()
    return 

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


def 
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