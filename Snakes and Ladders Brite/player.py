import pygame
import random
from pyvidplayer import Video
pygame.init()

class Player:
    def __init__(self, x, y, image, w, h):
        width = image.get_width()
        height = image.get_height()
        self.w = w
        self.h = h
        if w == 1920 and h == 1080:
            self.scale = 1
        elif w == 1280 and h == 720:
            self.scale = 1/1.5
        self.x = x*self.scale
        self.y = y*self.scale
        self.image = pygame.transform.scale(image, (int(width * self.scale), int(height * self.scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        x = x
        y = y
        return x, y

    def move_to(self, new_x, new_y):
        x = new_x
        y = new_y
        return x, y

    def special(self):
        specials = [
        (233,915,328,845)
        ,(283,925,378,853)
        ,(225,879,320,810)
        ,(287,879,382,810)
        ,(1088,915,1183,845)
        ,(1138,925,1233,853)
        ,(1080,879,1175,810)
        ,(1142,879,1237,810)
        ,(1088,775,993,705)
        ,(1138,781,1043,709)
        ,(1080,741,985,672)
        ,(1142,741,1047,672)
        ,(233,705,423,425)
        ,(283,709,473,421)
        ,(225,672,415,396)
        ,(287,672,477,396)
        ,(898,705,993,635)
        ,(948,709,1043,637)
        ,(890,672,985,603)
        ,(952,672,1047,603)
        ,(1563,705,1658,565)
        ,(1613,709,1708,565)
        ,(1555,672,1650,534)
        ,(1617,672,1712,534)
        ,(1468,635,993,215)
        ,(1518,637,1043,205)
        ,(1460,603,985,189)
        ,(1522,603,1047,189)
        ,(613,565,708,425)
        ,(663,565,758,421)
        ,(605,534,700,396)
        ,(667,534,762,396)
        ,(1563,495,1563,425)
        ,(1613,493,1613,421)
        ,(1555,465,1555,396)
        ,(1617,465,1617,396)
        ,(1088,495,993,425)
        ,(1138,493,1043,421)
        ,(1080,465,985,396)
        ,(1142,465,1047,396)
        ,(328,355,233,285)
        ,(378,349,283,277)
        ,(320,327,225,258)
        ,(382,327,287,258)
        ,(1563,285,1468,145)
        ,(1613,277,1518,133)
        ,(1555,258,1460,120)
        ,(1617,258,1522,120)
        ,(138,215,233,145)
        ,(188,205,283,133)
        ,(130,189,225,120)
        ,(192,189,287,120)
        ,(518,215,613,145)
        ,(568,205,663,133)
        ,(510,189,605,120)
        ,(572,189,667,120)
        ,(423,775,328,915)
        ,(473,781,378,925)
        ,(415,741,320,879)
        ,(477,741,477,879)
        ,(803,705,708,845)
        ,(853,709,758,853)
        ,(795,672,700,810)
        ,(857,672,762,810)
        ,(1278,705,1468,915)
        ,(1328,709,1518,925)
        ,(1270,672,1460,879)
        ,(1332,672,1522,879)
        ,(1658,775,1563,845)
        ,(1708,781,1613,853)
        ,(1650,741,1555,810)
        ,(1712,741,1617,810)
        ,(803,215,803,635)
        ,(853,205,853,637)
        ,(795,189,795,603)
        ,(857,189,857,603)
        ,(993,425,898,565)
        ,(1043,421,948,565)
        ,(985,396,890,534)
        ,(1047,396,952,534)
        ,(1563,425,1278,565)
        ,(1613,421,1328,565)
        ,(1555,396,1270,534)
        ,(1617,396,1332,534)
        ,(328,145,613,355)
        ,(378,133,663,349)
        ,(320,120,605,327)
        ,(382,120,667,327)
        ,(803,145,708,215)
        ,(853,133,758,205)
        ,(795,120,700,189)
        ,(857,120,762,189)
        ,(898,215,993,285)
        ,(948,205,1043,277)
        ,(890,189,985,258)
        ,(952,189,1047,258)
        ,(1278,145,1373,285)
        ,(1328,133,1423,277)
        ,(1270,120,1365,258)
        ,(1332,120,1427,258)
        ,(898,915,613,915)
        ,(948,925,663,925)
        ,(890,879,605,879)
        ,(952,879,667,879)
        ,(708,845,993,845)
        ,(758,853,1043,853)
        ,(700,810,985,810)
        ,(762,810,1047,810)
        ,(708,285,993,285)
        ,(758,277,1043,277)
        ,(700,258,985,258)
        ,(762,258,1047,258)
        ,(1183,215,898,215)
        ,(1233,205,948,205)
        ,(1175,189,890,189)
        ,(1237,189,952,189)
        ,(1088,145,1373,145)
        ,(1138,133,1423,133)
        ,(1080,120,1365,120)
        ,(1142,120,1427,120)
        ,(993,845,138,915)
        ,(1043,853,188,925)
        ,(985,810,130,879)
        ,(1047,810,192,879)
        ,(233,635,138,705)
        ,(283,637,188,709)
        ,(225,603,130,672)
        ,(287,603,192,672)
        ,(138,355,1563,565)
        ,(188,349,1613,565)
        ,(130,327,1555,534)
        ,(192,327,1617,534)
        ,(518,145,898,215)
        ,(568,133,948,205)
        ,(510,120,890,189)
        ,(572,120,952,189)
        ]

        for x1, y1, x2, y2 in specials:
            if self.rect.topleft == (x1*self.scale, y1*self.scale):
                self.move_to(x2, y2)
                break

    f = pygame.font.Font("Chewy.ttf",215)
    def draw_text(text,font,text_color,x,y):
        write = font.render(text,True,text_color)
        if self.w == 1920 and self.h == 1080:
            screen.blit(write,(x,y))
        else:
            screen.blit(write,(x/1.5,y/1.5))

    def roll_dice_with_animation(screen):
        dice = random.randint(1, 10)
        vid = Video("Video/dice_roll.mp4")
        vid.set_position(0)
        vid.set_size((self.w, self.h))
        vid.draw(screen, (0, 0))
        pygame.display.update()
        pygame.time.delay(2900)
        draw_text(dice,f,(0,0,0),self.w//2,self.h//2)
        pygame.display.update()
        pygame.time.delay(900)
        return dice
 
    def write(self, surface, action):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        if action == True:
            roll_dice_with_animation(surface)
            if order == 0 :
                    for i in range(dice):
                        if y1 in (915, 775, 635, 495, 355, 215, 925, 781, 637, 493, 349, 205,879, 741, 603, 465, 327, 189):
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
                        if y2 in ():
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
                        if y3 in ():
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
            