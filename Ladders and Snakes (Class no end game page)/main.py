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

#โหลดรูปภาพปุ่ม
def load_images():
    image_paths = {
        "play": "button_play.png",
        "option": "button_option.png",
        "how": "button_how.png",
        "quit": "button_quit.png",
        "back": "button_back.png",
        "pause": "button_pause.png",
        "resume": "button_resume.png",
        "options": "button_options.png",
        "home": "button_home.png",
        "thirty": "button_30.png",
        "sixty": "button_60.png",
        "twenty": "button_120.png",
        "hd": "button_hd.png",
        "fullhd": "button_fullhd.png",
        "on": "button_on.png",
        "off": "button_off.png",
        "random": "button_random.png"
    }

    images = {}
    for name, path in image_paths.items():
        images[name] = pygame.image.load(path).convert_alpha()

    return images

images = load_images()

play_img = images["play"]
option_img = images["option"]
how_img = images["how"]
quit_img = images["quit"]
back_img = images["back"]
pause_img = images["pause"]
resume_img = images["resume"]
options_img = images["options"]
home_img = images["home"]
thirty_img = images["thirty"]
sixty_img = images["sixty"]
twenty_img = images["twenty"]
hd_img = images["hd"]
fullhd_img = images["fullhd"]
on_img = images["on"]
off_img = images["off"]
random_img = images["random"]

buttons = {}

#ขนาดฟอนต์และสเกลของปุ่มและลูกเต๋าเริ่มต้น
font_size = 28
button_scale = 1
dice_scale = (60,60)
player_scale = (50, 60)

#ค่าเริ่มต้นของปุ่ม
def init_buttons():
    global buttons
    buttons = {
        "play": button.Button(752, 463, play_img, 1),
        "option": button.Button(752, 619, option_img, 1),
        "how": button.Button(751, 774, how_img, 1),
        "quit": button.Button(752, 928, quit_img, 1),
        "back": button.Button(58, 1005, back_img, 1/2),
        "pause": button.Button(836, 5, pause_img, 1),
        "resume": button.Button(748, 215, resume_img, 1),
        "options": button.Button(748, 485, options_img, 1),
        "home": button.Button(748, 761, home_img, 1),
        "thirty": button.Button(448, 198, thirty_img, 1),
        "sixty": button.Button(825, 198, sixty_img, 1),
        "twenty": button.Button(1201, 198, twenty_img, 1),
        "hd": button.Button(635, 427, hd_img, 1),
        "fullhd": button.Button(1013, 427, fullhd_img, 1),
        "on_music": button.Button(636, 657, on_img, 1),
        "off_music": button.Button(1012, 657, off_img, 1),
        "on_sound": button.Button(636, 886, on_img, 1),
        "off_sound": button.Button(1013, 886, off_img, 1),
    }

def resize_screen():
    global screen, buttons, button_scale, dice_scale, font_size, player_scale
    screen = pygame.display.set_mode((x, y))
    update_position_calculations()
    game.update_roll_and_dice(button_scale)
    game.player1.update_scale(player_scale)  #ปรับขนาดตัวละครของ player1
    game.player2.update_scale(player_scale)  #ปรับขนาดตัวละครของ player2
    game.player1.position = game.player1.position  #คำนวณตำแหน่งใหม่ของ Player 1
    game.player2.position = game.player2.position  #คำนวณตำแหน่งใหม่ของ Player 2
    #สร้างปุ่มตามขนาดหน้าจอ
    if x == 1920 and y == 1080:
        buttons["play"] = button.Button(752, 463, play_img, 1)
        buttons["option"] = button.Button(752, 619, option_img, 1)
        buttons["how"] = button.Button(751, 774, how_img, 1)
        buttons["quit"] = button.Button(752, 928, quit_img, 1)
        buttons["back"] = button.Button(58, 1005, back_img, 1/2)
        buttons["pause"] = button.Button(836, 5, pause_img, 1)
        buttons["resume"] = button.Button(748, 215, resume_img, 1)
        buttons["options"] = button.Button(748, 485, options_img, 1)
        buttons["home"] = button.Button(748, 761, home_img, 1)
        buttons["thirty"] = button.Button(448, 198, thirty_img, 1)
        buttons["sixty"] = button.Button(825, 198, sixty_img, 1)
        buttons["twenty"] = button.Button(1201, 198, twenty_img, 1)
        buttons["hd"] = button.Button(635, 427, hd_img, 1)
        buttons["fullhd"] = button.Button(1013, 427, fullhd_img, 1)
        buttons["on_music"] = button.Button(636, 657, on_img, 1)
        buttons["off_music"] = button.Button(1012, 657, off_img, 1)
        buttons["on_sound"] = button.Button(636, 886, on_img, 1)
        buttons["off_sound"] = button.Button(1013, 886, off_img, 1)

    elif x == 1280 and y == 720:
        buttons["play"] = button.Button(501, 309, play_img, 1/1.5)
        buttons["option"] = button.Button(501, 413, option_img, 1/1.5)
        buttons["how"] = button.Button(501, 517, how_img, 1/1.5)
        buttons["quit"] = button.Button(501, 619, quit_img, 1/1.5)
        buttons["back"] = button.Button(45, 670, back_img, 1/3)
        buttons["pause"] = button.Button(557, 3, pause_img, 1/1.5)
        buttons["resume"] = button.Button(499, 143, resume_img, 1/1.5)
        buttons["options"] = button.Button(499, 323, options_img, 1/1.5)
        buttons["home"] = button.Button(499, 507, home_img, 1/1.5)
        buttons["thirty"] = button.Button(299, 132, thirty_img, 1/1.5)
        buttons["sixty"] = button.Button(550, 132, sixty_img, 1/1.5)
        buttons["twenty"] = button.Button(801, 132, twenty_img, 1/1.5)
        buttons["hd"] = button.Button(423, 285, hd_img, 1/1.5)
        buttons["fullhd"] = button.Button(675, 285, fullhd_img, 1/1.5)
        buttons["on_music"] = button.Button(424, 438, on_img, 1/1.5)
        buttons["off_music"] = button.Button(675, 438, off_img, 1/1.5)
        buttons["on_sound"] = button.Button(424, 591, on_img, 1/1.5)
        buttons["off_sound"] = button.Button(675, 591, off_img, 1/1.5)

#กำหนดพื้นหลัง
def bg(img):
    background = pygame.image.load(img)
    background_fixed = pygame.transform.scale(background,(x,y))
    screen.blit(background_fixed,(0,0))

def draw_board():
    bg("Background.png")

#การแสดงผลหน้าต่าง
init_buttons()
def draw_home():
    bg("Home.png")
    if buttons["play"].draw(screen):
        pygame.time.delay(100)
        return 'game'
    if buttons["option"].draw(screen):
        pygame.time.delay(100)
        return 'option_home'
    if buttons["how"].draw(screen):
        pygame.time.delay(100)
        return 'how'
    if buttons["quit"].draw(screen):
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
    if buttons["pause"].draw(screen):
        pygame.time.delay(100)
        return 'pause'
    return 'game'

def draw_option_home():
    global FPS, x, y
    bg("Option.png")
    if buttons["back"].draw(screen):
        pygame.time.delay(100)
        return 'home'
    if buttons["thirty"].draw(screen):
        pygame.time.delay(100)
        FPS = 30
    if buttons["sixty"].draw(screen):
        pygame.time.delay(100)
        FPS = 60
    if buttons["twenty"].draw(screen):
        pygame.time.delay(100)
        FPS = 120
    if buttons["hd"].draw(screen):
        pygame.time.delay(100)
        x = 1280
        y = 720
        resize_screen()
        draw_board()
        game.draw_players()
    if buttons["fullhd"].draw(screen):
        pygame.time.delay(100)
        x = 1920
        y = 1080
        resize_screen()
        draw_board()
        game.draw_players()
    if buttons["on_music"].draw(screen):
        pygame.time.delay(100)
        return 'home'
    if buttons["off_music"].draw(screen):
        pygame.time.delay(100)
        return 'home'
    if buttons["on_sound"].draw(screen):
        pygame.time.delay(100)
        return 'home'
    if buttons["off_sound"].draw(screen):
        pygame.time.delay(100)
        return 'home'
    return 'option_home'

def draw_option_game():
    global FPS, x, y
    bg("Option.png")
    if buttons["back"].draw(screen):
        pygame.time.delay(100)
        return 'pause'
    if buttons["thirty"].draw(screen):
        pygame.time.delay(100)
        FPS = 30
    if buttons["sixty"].draw(screen):
        pygame.time.delay(100)
        FPS = 60
    if buttons["twenty"].draw(screen):
        pygame.time.delay(100)
        FPS = 120
    if buttons["hd"].draw(screen):
        pygame.time.delay(100)
        x = 1280
        y = 720
        resize_screen()
    if buttons["fullhd"].draw(screen):
        pygame.time.delay(100)
        x = 1920
        y = 1080
        resize_screen()
    if buttons["on_music"].draw(screen):
        pygame.time.delay(100)
        return 'home'
    if buttons["off_music"].draw(screen):
        pygame.time.delay(100)
        return 'home'
    if buttons["on_sound"].draw(screen):
        pygame.time.delay(100)
        return 'home'
    if buttons["off_sound"].draw(screen):
        pygame.time.delay(100)
        return 'home'
    return 'option_game'

def draw_how():
    bg("HowToPlay.png")
    if buttons["back"].draw(screen):
        pygame.time.delay(100)
        return 'home'
    return 'how'

def draw_pause():
    bg("Background_pause.png")
    if buttons["resume"].draw(screen):
        pygame.time.delay(100)
        return 'game'
    if buttons["options"].draw(screen):
        pygame.time.delay(100)
        return 'option_game'
    if buttons["home"].draw(screen):
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
win = {204}

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

#อัปเดตposition และ scale เมื่อมีการเปลี่ยนขนาดหน้าจอ
def update_position_calculations():
    global edge_x, edge_y, button_scale, dice_scale, font_size, player_scale
    if x == 1920 and y == 1080:
        edge_x = 296
        edge_y = 209
        button_scale = 1
        dice_scale = (60, 60)
        font_size = 28
        player_scale = (50, 60)

    elif x == 1280 and y == 720:
        edge_x = 200
        edge_y = 145
        button_scale = 0.5
        dice_scale = (40, 40)
        font_size = 16
        player_scale = (30, 40)
    

#คลาสplayer
class Player:
    def __init__(self, image, scale):
        self.position = 1
        self.last_checkpoint = 1
        self.skip_turn = False
        self.has_shield = False
        self.image = pygame.transform.scale(image, scale)

    def update_scale(self, scale):
        self.image = pygame.transform.scale(self.image, scale)

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

        #เช็ค presents
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

        #เช็ค end game
        elif self.position in win:
            message = "You are winner!"

        return message

    #วาดตัวละคร
    def draw(self, screen, offset_x=0, offset_y=0):
        pos_x, pos_y = get_position_coordinates(self.position)
        if x == 1920 and y == 1080:
            offset_x += 20
            offset_y += 30
        elif x == 1280 and y == 720:
            offset_x += 5
            offset_y += 15
        screen.blit(self.image, (pos_x + offset_x, pos_y + offset_y))

#คลาสเกม
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player1 = Player(pygame.image.load("player_01.png"), player_scale)
        self.player2 = Player(pygame.image.load("player_02.png"), player_scale)
        self.button_rect = pygame.Rect(10, 10, 120 * button_scale, 50 * button_scale)
        self.dice_value = None
        self.current_player = 1
        self.current_message = ""
        self.roll_button = button.Button(20, 20, random_img, button_scale)
        self.dice_images = self.load_dice_images()

    def load_dice_images(self):
        return {
            1: pygame.transform.scale(pygame.image.load("dice_1.png"), dice_scale),
            2: pygame.transform.scale(pygame.image.load("dice_2.png"), dice_scale),
            3: pygame.transform.scale(pygame.image.load("dice_3.png"), dice_scale),
            4: pygame.transform.scale(pygame.image.load("dice_4.png"), dice_scale),
            5: pygame.transform.scale(pygame.image.load("dice_5.png"), dice_scale),
            6: pygame.transform.scale(pygame.image.load("dice_6.png"), dice_scale)
        }
    
    def update_roll_and_dice(self, button_scale):
        #ปรับขนาดปุ่ม random
        self.roll_button = button.Button(20, 20, random_img, button_scale)
        #ปรับภาพลูกเต๋า
        self.dice_images = self.load_dice_images()

    def roll_dice(self):
        self.dice_value = random.randint(1, 6)
        return self.dice_value
    
    def draw_roll_button_and_player_turn(self):
        #วาดปุ่มทอยลูกเต๋า
        if self.roll_button.draw(self.screen):
            self.roll_dice()

        # การแสดงภาพลูกเต๋า
        if self.dice_value:
            dice_image = self.dice_images[self.dice_value]
        else:
            dice_image = self.dice_images[1]

        dice_rect = dice_image.get_rect()
        dice_rect.midleft = (self.roll_button.rect.right + 20, self.roll_button.rect.centery)
        self.screen.blit(dice_image, dice_rect)

        #แสดงข้อความ "Player Turn:"
        font = pygame.font.Font("Chewy.ttf", font_size)
        turn_text = font.render("Player Turn:", True, (255, 255, 255))
        text_rect = turn_text.get_rect()

        #แสดงภาพเจ้าของเทิร์น
        if self.current_player == 1:
            current_player_image = self.player1.image
        else:
            current_player_image = self.player2.image
        player_image_rect = current_player_image.get_rect()

        #คำนวณพื้นที่รวมของข้อความและภาพผู้เล่น
        combined_width = text_rect.width + player_image_rect.width + 10  #ระยะห่างระหว่างข้อความและภาพ
        combined_height = max(text_rect.height, player_image_rect.height)
        background_rect = pygame.Rect(
            dice_rect.right + 20,  #เริ่มที่ด้านขวาของลูกเต๋า
            dice_rect.top - 10,  # ระดับเดียวกับด้านบนของลูกเต๋า
            combined_width + 20,  #ความกว้างรวมของข้อความและภาพ + padding
            combined_height + 20  #ความสูงรวม + padding
        )

        #วาดพื้นหลังสีดำสำหรับข้อความและภาพ
        pygame.draw.rect(self.screen, (0, 0, 0), background_rect)

        #วาดข้อความ "Player Turn:" บนพื้นหลัง
        text_rect.midleft = (background_rect.left + 10, background_rect.centery)
        self.screen.blit(turn_text, text_rect)

        #วาดภาพผู้เล่นบนพื้นหลัง
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
            font = pygame.font.Font("Chewy.ttf", font_size)
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
        self.player1 = Player(pygame.image.load("player_01.png"), player_scale)
        self.player2 = Player(pygame.image.load("player_02.png"), player_scale)
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