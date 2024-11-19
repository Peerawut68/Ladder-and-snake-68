import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up screen dimensions and colors
WIDTH, HEIGHT = 400, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Roller")

# Load dice images
dice_images = [
    pygame.image.load(f"dice_{i}.png") for i in range(1, 7)
]

# Resize dice images
dice_images = [pygame.transform.scale(img, (100, 100)) for img in dice_images]

# Font for displaying text
font = pygame.font.Font(None, 36)

def roll_dice():
    """Simulate rolling a dice by returning a random number between 1 and 6."""
    return random.randint(1, 6)

def main():
    clock = pygame.time.Clock()
    running = True
    dice_value = 1

    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Roll dice when spacebar is pressed
                    dice_value = roll_dice()

        # Draw the dice image
        screen.blit(dice_images[dice_value - 1], (WIDTH // 2 - 50, HEIGHT // 2 - 50))

        # Display instruction text
        text = font.render("Press SPACE to roll the dice", True, BLACK)
        screen.blit(text, (50, 50))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
