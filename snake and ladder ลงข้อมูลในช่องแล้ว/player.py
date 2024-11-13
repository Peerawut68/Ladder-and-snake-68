import pygame
from ladders_snakes_pos import ladders, snakes, checkpoints , respawn_points, bombs, cages, presents, get_position_coordinates

class Player:
    def __init__(self, image):
        self.position = 1
        self.last_checkpoint = 1
        self.skip_turn = False
        self.image = pygame.transform.scale(image, (30, 30))

    def move(self, steps, screen, draw_board, draw_players):
        #เช็คการถูกข้ามเทิร์น
        if self.skip_turn:
            self.skip_turn = False
            return
        
        end_position = self.position + steps
        if end_position > 204:
            end_position = 204
        self.animate_move(end_position, screen, draw_board, draw_players)
        self.position = end_position
        self.check_action(screen, draw_board, draw_players)

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
        #เช็ค checkpoint
        if self.position in checkpoints:
            print('คุณ checkpoint')
            self.last_checkpoint = self.position

        #เช็ค respawn
        if self.position in respawn_points:
            print('คุณโดนรีเซ็ต')
            self.position = self.last_checkpoint

        #เช็ค bomb
        if self.position in bombs:
            print('คุณโดนระเบิด')
            self.animate_reverse_move(3, screen, draw_board, draw_players)

        #เช็ค cages
        elif self.position in cages:
            print('คุณอดเล่น 1 ตา')
            self.skip_turn = True
        
        #เช็ค presents
        elif self.position in presents:
            print("คุณได้รับไอเทม")
            # -- self.ฟังก์ชันสุ่มไอเทม --

        #เช็ค ladders
        if self.position in ladders:
            self.position = ladders[self.position]

        #เช็ค snakes
        if self.position in snakes:
            self.position = snakes[self.position]

    def draw(self, screen, offset_x=0, offset_y=10):
        x, y = get_position_coordinates(self.position)
        screen.blit(self.image, (x + offset_x, y + offset_y))