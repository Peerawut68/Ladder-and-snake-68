import pygame
from ladders_snakes_pos import ladders, snakes, get_position_coordinates

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
            pygame.display.update()
            pygame.time.delay(200)

    def check_ladders_and_snakes_instant(self):
        if self.position in ladders:
            self.position = ladders[self.position]
        elif self.position in snakes:
            self.position = snakes[self.position]

    def draw(self, screen, offset_x=0, offset_y=10):
        x, y = get_position_coordinates(self.position)
        screen.blit(self.image, (x + offset_x, y + offset_y))