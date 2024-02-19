import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cheese Curd Clicker")

# Fonts
font = pygame.font.SysFont(None, 40)

# Game variables
curds = 0
curds_per_click = 1
curds_per_second = 0
upgrade_cost = 100
upgrade_multiplier = 5
upgrade_purchased = False

# Buttons
click_button = pygame.Rect(WIDTH//2 - 50, HEIGHT//2 - 50, 100, 100)
upgrade_button = pygame.Rect(WIDTH - 150, 50, 100, 50)

# Main game loop
running = True
last_time = time.time()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Check if click is on the click button
                if click_button.collidepoint(event.pos):
                    curds += curds_per_click
                # Check if click is on the upgrade button
                elif upgrade_button.collidepoint(event.pos):
                    if curds >= upgrade_cost and not upgrade_purchased:
                        curds_per_second += upgrade_multiplier
                        curds -= upgrade_cost
                        upgrade_purchased = True

    # Update game logic
    current_time = time.time()
    if current_time - last_time >= 1:
        last_time = current_time
        curds += curds_per_second

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, click_button)
    pygame.draw.rect(screen, GRAY, upgrade_button)
    
    # Render text
    click_text = font.render("Click", True, BLACK)
    upgrade_text = font.render("Upgrade", True, BLACK)
    curds_text = font.render(f"Cheese Curds: {curds}", True, BLACK)
    screen.blit(click_text, (click_button.centerx - click_text.get_width() // 2, click_button.centery - click_text.get_height() // 2))
    screen.blit(upgrade_text, (upgrade_button.centerx - upgrade_text.get_width() // 2, upgrade_button.centery - upgrade_text.get_height() // 2))
    screen.blit(curds_text, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)

pygame.quit()
sys.exit()
