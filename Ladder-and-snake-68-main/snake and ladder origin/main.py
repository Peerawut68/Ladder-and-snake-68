import pygame
from game import Game

pygame.init()

#กำหนดขนาดหน้าจอ
x, y = 1280, 720
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Snakes and Ladders")

#โหลดพื้นหลัง
background = pygame.image.load("Background.png")
background = pygame.transform.scale(background, (x, y))

#วาดพื้นหลัง
def draw_board():
    screen.blit(background, (0, 0))

game = Game(screen)
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