import pygame
import random
pygame.init()

#กำหนดขนาดหน้าจอ
x = 1280
y = 720
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Snakes and Ladders")

#โหลดภาพกระดานเกม
background = pygame.image.load("Background.png")
background = pygame.transform.scale(background, (x, y))

#ฟังก์ชันวาดพื้นหลัง
def draw_board():
    screen.blit(background, (0, 0))

#ตำแหน่งบันไดและงูในบอร์ด
ladders = {
    2:32,
    11:23,
    45:59,
    53:86,
    60:78,
    67:133,
    83:180,
    97:130,
    113:127,
    118:121,
    139:169,
    155:190,
    171:203,
    175:199
    }
snakes = {
    202:142,
    197:177,
    192:157,
    179:161,
    178:76,
    127:94,
    121:90,
    61:28,
    56:15,
    51:19,
    38:3
    }

class Player:
    def __init__(self, image):
        self.position = 1
        self.image = pygame.transform.scale(image, (30, 30))

    def move(self, steps):
        end_position = self.position + steps
        if end_position > 204:
            end_position = 204
        self.animate_move(end_position)
        self.position = end_position
        self.check_ladders_and_snakes_instant()
    
    def animate_move(self, end_position):
        while self.position < end_position:
            self.position += 1
            draw_board()
            game.draw_players()
            pygame.display.update()
            pygame.time.delay(200)

    def check_ladders_and_snakes_instant(self):
        if self.position in ladders:
            self.position = ladders[self.position]
        elif self.position in snakes:
            self.position = snakes[self.position]

    def draw(self, offset_x=0, offset_y=10):
        x, y = game.get_position_coordinates(self.position)
        screen.blit(self.image, (x + offset_x, y + offset_y))

class Game:
    def __init__(self):
        self.player1 = Player(pygame.image.load("หมากขาว.png"))
        self.player2 = Player(pygame.image.load("หมากดำ.png"))
        self.button_rect = pygame.Rect(500, 620, 200, 50)
        self.dice_value = None
        self.current_player = 1

    def roll_dice(self):
        self.dice_value = random.randint(1, 6)
        return self.dice_value

    def draw_button(self):
        pygame.draw.rect(screen, (0, 255, 0), self.button_rect)
        font = pygame.font.Font(None, 36)
        text = font.render("Roll Dice", True, (255, 255, 255))
        screen.blit(text, (self.button_rect.x + 10, self.button_rect.y + 10))

        if self.dice_value:
            dice_text = font.render(f"Dice: {self.dice_value}", True, (0, 0, 0))
            screen.blit(dice_text, (700, 630))

    def get_position_coordinates(self, position):
        #คำนวณความกว้างและยาวของช่อง
        tile_width = (1280 - 200) / 17
        tile_height = (720 - 145) / 12
    
        #แปลง position เป็น index ของแถวและคอลัมน์
        row = (position - 1) // 17
        column = (position - 1) % 17
    
        #ถ้าเป็นแถวที่นับจากขวาไปซ้าย ให้กลับตำแหน่งคอลัมน์
        if row % 2 == 1:
            column = 16 - column

        #คำนวณตำแหน่ง x และ y โดยพิจารณาขอบซ้ายและบน
        x = 100 + column * tile_width
        y = 720 - 56 - (row + 1) * tile_height  #นับจากล่างขึ้นบน
    
        return int(x), int(y)

    def draw_players(self):
        if self.player1.position == self.player2.position:
            # หากผู้เล่นทั้งสองอยู่ในช่องเดียวกัน ให้ player2 ขยับออกไปทางขวา
            self.player1.draw()
            self.player2.draw(offset_x=20)
        else:
            self.player1.draw()
            self.player2.draw()

    def play_turn(self):
        steps = self.roll_dice()
        if self.current_player == 1:
            self.player1.move(steps)
            self.current_player = 2
        else:
            self.player2.move(steps)
            self.current_player = 1

game = Game()
running = True
while running:
    draw_board()
    game.draw_button()
    game.draw_players()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game.button_rect.collidepoint(event.pos):
                game.play_turn()

    pygame.display.update()

pygame.quit()