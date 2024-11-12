import pygame
import random
from player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player1 = Player(pygame.image.load("หมากขาว.png"))
        self.player2 = Player(pygame.image.load("หมากดำ.png"))
        self.button_rect = pygame.Rect(500, 620, 200, 50)
        self.dice_value = None
        self.current_player = 1

    def roll_dice(self):
        self.dice_value = random.randint(1, 6)
        return self.dice_value

    #ปุมทดสอบ
    def draw_button(self):
        pygame.draw.rect(self.screen, (0, 255, 0), self.button_rect)
        font = pygame.font.Font(None, 36)
        text = font.render("Roll Dice", True, (255, 255, 255))
        self.screen.blit(text, (self.button_rect.x + 10, self.button_rect.y + 10))

        if self.dice_value:
            dice_text = font.render(f"Dice: {self.dice_value}", True, (0, 0, 0))
            self.screen.blit(dice_text, (700, 630))

    def draw_players(self):
        if self.player1.position == self.player2.position:
            self.player1.draw(self.screen)
            self.player2.draw(self.screen, offset_x=20)
        else:
            self.player1.draw(self.screen)
            self.player2.draw(self.screen)

    def play_turn(self):
        steps = self.roll_dice()
        if self.current_player == 1:
            self.player1.move(steps)
            self.current_player = 2
        else:
            self.player2.move(steps)
            self.current_player = 1