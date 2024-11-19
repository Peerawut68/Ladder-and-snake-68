import os
import pygame
import button
import random
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
    update_position_calculations()
    game.player1.position = game.player1.position  #คำนวณตำแหน่งใหม่ของ Player 1
    game.player2.position = game.player2.position  #คำนวณตำแหน่งใหม่ของ Player 2
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

def draw_board():
    bg("Background.png")

#กำหนดชนิดและขนาดของ font 
font = pygame.font.Font("Chewy.ttf",36)

#กำหนดสีข้อความ
txt_color = (0,21,1)
black = (0,0,0)

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
random_img = pygame.image.load("button_random.png").convert_alpha()

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
    game.reset_game()
    return 'home'

def draw_game():
    draw_board()
    game.draw_roll_button_and_player_turn()
    game.draw_players()
    game.draw_message()
    mouse_pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:  # ตรวจสอบการกดปุ่มซ้ายของเมาส์
        if game.button_rect.collidepoint(mouse_pos):
            game.play_turn(draw_board)
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
        draw_board()
        game.draw_players()
    if fullhd_button.draw(screen):
        pygame.time.delay(100)
        x = 1920
        y = 1080
        resize_screen()
        draw_board()
        game.draw_players()
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

#กำหนดตำแหน่งช่องต่างๆ
ladders = {
    2: 32,
    11: 23,
    45: 59,
    53: 86,
    60: 78,
    67: 133,
    83: 180,
    97: 130,
    113: 127,
    118: 121,
    139: 169,
    155: 190,
    171: 203,
    175: 199
}

snakes = {
    202: 142,
    197: 177,
    192: 157,
    179: 161,
    178: 76,
    127: 94,
    121: 90,
    61: 28,
    56: 15,
    51: 19,
    38: 3
}

checkpoints = {68, 87, 179}
respawn_points = {25, 70, 137, 200}
bombs = {9, 28, 164, 182, 194}
cages = {57, 64, 110, 191}
presents = {7, 17, 20, 38, 43, 69, 74, 
    82, 94, 101, 107, 124, 133, 
    144, 153, 157, 167, 173, 189,
    196, 197, 201}

if x == 1920 and y == 1080:
    edge_x = 296
    edge_y = 209
elif x == 1280 and y == 720:
    edge_x = 200
    edge_y = 145

def get_position_coordinates(position):
    tile_width = (x - edge_x) / 17
    tile_height = (y - edge_y) / 12
    row = (position - 1) // 17
    column = (position - 1) % 17

    if row % 2 == 1:
        column = 16 - column

    pos_x = (edge_x/2) + column * tile_width
    pos_y = y - (edge_y/2) - (row + 1) * tile_height
    return int(pos_x), int(pos_y)

#อัปเดตpositionเมื่อมีการเปลี่ยนขนาดหน้าจอ
def update_position_calculations():
    global edge_x, edge_y
    if x == 1920 and y == 1080:
        edge_x = 296
        edge_y = 209
    elif x == 1280 and y == 720:
        edge_x = 200
        edge_y = 145

#คลาสplayer
class Player:
    def __init__(self, image):
        self.position = 1
        self.last_checkpoint = 1
        self.skip_turn = False
        self.has_shield = False
        self.image = pygame.transform.scale(image, (40, 50))

    def move(self, steps, screen, draw_board, draw_players):
        if self.skip_turn:
            self.skip_turn = False
            return ""

        end_position = self.position + steps
        if end_position > 204:
            end_position = 204
        self.animate_move(end_position, screen, draw_board, draw_players)
        self.position = end_position
        return self.check_action(screen, draw_board, draw_players)

    def animate_move(self, end_position, screen, draw_board, draw_players):
        while self.position < end_position:
            self.position += 1
            draw_board()          
            draw_players()         
            pygame.display.update()
            pygame.time.delay(200)

    def animate_reverse_move(self, steps, screen, draw_board, draw_players):
        for _ in range(steps):
            if self.position > 1:
                self.position -= 1
                draw_board()
                draw_players()
                pygame.display.update()
                pygame.time.delay(200)

    def check_action(self, screen, draw_board, draw_players):
        message = ""

        #เช็ค ladders
        if self.position in ladders:
            self.position = ladders[self.position]
            message = "Climbed a ladder!"

        #เช็ค snakes
        elif self.position in snakes:
            self.position = snakes[self.position]
            message = "Bitten by a snake!"

        #เช็ค checkpoint
        elif self.position in checkpoints:
            self.last_checkpoint = self.position
            message = "Checkpoint reached!"

        #เช็ค respawn
        elif self.position in respawn_points:
            self.position = self.last_checkpoint
            message = "Respawned at last checkpoint!"

        #เช็ค bomb
        elif self.position in bombs:
            self.animate_reverse_move(3, screen, draw_board, draw_players)
            message = "Hit a bomb! Move back 3 steps!"

        #เช็ค cages
        elif self.position in cages:
            self.skip_turn = True
            message = "Caged! Skip next turn!"

        # เช็ค presents
        elif self.position in presents:
            item = random.choice(["Knockback", "Freeze", "Shield", "Go Forward"])
            if item == "Knockback":
                message = "You received Knockback!"
                if not self.has_shield:
                    other_player = game.get_other_player()
                    other_player.animate_reverse_move(3, screen, draw_board, draw_players)
                    message += " ,the other player was pushed back 3 spaces!"
                else:
                    self.has_shield = False
                    message += " ,but the other player blocked it"

            elif item == "Freeze":
                message = "You received Freeze!"
                if not self.has_shield:
                    other_player = game.get_other_player()
                    other_player.skip_turn = True
                    message += " ,the other player will skip their next turn!"
                else:
                    self.has_shield = False
                    message += " ,but the other player blocked it"

            elif item == "Shield":
                self.has_shield = True
                message = "You received a Shield!"

            elif item == "Go Forward":
                message = "You received Jump boots!"
                pygame.time.delay(500)
                self.animate_move(self.position + 3, screen, draw_board, draw_players)

        return message

    #วาดตัวละคร
    def draw(self, screen, offset_x=0, offset_y=0):
        pos_x, pos_y = get_position_coordinates(self.position)
        if x == 1920 and y == 1080:
            offset_x += 20
            offset_y += 30
        elif x == 1280 and y == 720:
            offset_y += 15
        screen.blit(self.image, (pos_x + offset_x, pos_y + offset_y))

#คลาสเกม
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player1 = Player(pygame.image.load("player_01.png"))
        self.player2 = Player(pygame.image.load("player_02.png"))
        self.button_rect = pygame.Rect(10, 10, 120, 50)
        self.dice_value = None
        self.current_player = 1
        self.current_message = ""
        self.roll_button = button.Button(20, 20, random_img, 2/3)
        self.dice_images = {
            1: pygame.transform.scale(pygame.image.load("dice_1.png"), (60, 60)),
            2: pygame.transform.scale(pygame.image.load("dice_2.png"), (60, 60)),
            3: pygame.transform.scale(pygame.image.load("dice_3.png"), (60, 60)),
            4: pygame.transform.scale(pygame.image.load("dice_4.png"), (60, 60)),
            5: pygame.transform.scale(pygame.image.load("dice_5.png"), (60, 60)),
            6: pygame.transform.scale(pygame.image.load("dice_6.png"), (60, 60)),
        }

    def roll_dice(self):
        self.dice_value = random.randint(1, 6)
        return self.dice_value
    
    def draw_roll_button_and_player_turn(self):
        #วาดปุ่มทอยลูกเต๋า
        if self.roll_button.draw(self.screen):  #ตรวจสอบว่าปุ่มถูกกดหรือไม่
            self.roll_dice()  # ทอยลูกเต๋าเมื่อปุ่มถูกคลิก

        # การแสดงภาพลูกเต๋า
        if self.dice_value:
            dice_image = self.dice_images[self.dice_value]
        else:
            dice_image = self.dice_images[1]  #แสดงเป็นลูกเต๋า 1 ถ้ายังไม่ได้ทอยลูกเต๋า

        dice_rect = dice_image.get_rect()
        dice_rect.midleft = (self.roll_button.rect.right + 20, self.roll_button.rect.centery)
        self.screen.blit(dice_image, dice_rect)

        #แสดงข้อความ "Player Turn:"
        font = pygame.font.Font(None, 36)
        turn_text = font.render("Player Turn:", True, (0, 0, 0))
        text_rect = turn_text.get_rect()

        #วางข้อความ "Player Turn:" ไว้ขวาของลูกเต๋า
        text_rect.midleft = (dice_rect.right + 20, dice_rect.centery)
        self.screen.blit(turn_text, text_rect)

        #แสดงภาพเจ้าของเทิร์น
        if self.current_player == 1:
            current_player_image = self.player1.image
        else:
            current_player_image = self.player2.image
        player_image_rect = current_player_image.get_rect()

        #วางภาพผู้เล่นไว้ขวาของข้อความ "Player Turn:"
        player_image_rect.midleft = (text_rect.right + 10, text_rect.centery)
        self.screen.blit(current_player_image, player_image_rect)

    def draw_players(self):
        if self.player1.position == self.player2.position:
            self.player1.draw(self.screen)
            self.player2.draw(self.screen, offset_x=20)
        else:
            self.player1.draw(self.screen)
            self.player2.draw(self.screen)

    def draw_message(self):
        if self.current_message:
            font = pygame.font.Font(None, 32)
            text = font.render(self.current_message, True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.topright = (x - 20, 20)
            pygame.draw.rect(self.screen, (0, 0, 0), text_rect.inflate(10, 10))
            self.screen.blit(text, text_rect)

    def get_other_player(self):
        if self.current_player == 2:
            return self.player1
        else:
            return self.player2

    def play_turn(self, draw_board):
        self.current_message = ""
        steps = self.roll_dice()

        if self.current_player == 1:
            current_player = self.player1
            other_player = self.player2
        else:
            current_player = self.player2
            other_player = self.player1

        #เรียกการเดินของผู้เล่นและเก็บข้อความที่ได้จากการเดิน
        self.current_message = current_player.move(steps, self.screen, draw_board, self.draw_players)

        #เปลี่ยนผู้เล่น
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def reset_game(self):
        self.player1 = Player(pygame.image.load("player_01.png"))
        self.player2 = Player(pygame.image.load("player_02.png"))
        self.dice_value = None
        self.current_player = 1

game = Game(screen)
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