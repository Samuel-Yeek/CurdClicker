import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1200, 800
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Load cheese images
cheese_curd_image = pygame.image.load('assets/CheddarCurd.png')
cheese_curd_image = pygame.transform.scale(cheese_curd_image, (cheese_curd_image.get_width() // 5, cheese_curd_image.get_height() // 5))
cow_image = pygame.image.load('assets/cow.png')
cow_image = pygame.transform.scale(cow_image, (cow_image.get_width() // 15, cow_image.get_height() // 15))

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cheese Curd Clicker")

# Fonts
font = pygame.font.SysFont(None, 40)

# Game variables
curds = 0
curds_per_click = 1
curds_per_second = 0
cow_count = 0
cow_cost = 100
cow_production = 5

# Buttons
click_button = pygame.Rect(WIDTH//2 - 50, HEIGHT//2 - 50, 100, 100)
buy_cow_button = pygame.Rect(WIDTH - 150, 50, 100, 50)

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
                # Check if click is on the buy cow button
                elif buy_cow_button.collidepoint(event.pos):
                    if curds >= cow_cost:
                        curds -= cow_cost
                        cow_count += 1
                        cow_cost += cow_cost*0.1
                        curds_per_second += cow_production

    # Update game logic
    current_time = time.time()
    if current_time - last_time >= 1:
        last_time = current_time
        curds += curds_per_second

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, click_button)
    pygame.draw.rect(screen, GRAY, buy_cow_button)

    # Render text and images
    click_text = font.render("Create Curd", True, BLACK)
    buy_cow_text = font.render("Buy Cow", True, BLACK)
    curds_text = font.render(f"Cheese Curds: {curds}", True, BLACK)
    cow_count_text = font.render(f"Cow Count: {cow_count}", True, BLACK)
    screen.blit(click_text, (click_button.centerx - click_text.get_width() // 2, click_button.centery - click_text.get_height() // 2))
    screen.blit(buy_cow_text, (buy_cow_button.centerx - buy_cow_text.get_width() // 2, buy_cow_button.centery - buy_cow_text.get_height() // 2))
    screen.blit(curds_text, (10, 10))
    screen.blit(cow_count_text, (10, 50))
    screen.blit(cheese_curd_image, (click_button.centerx - cheese_curd_image.get_width() // 2, click_button.centery - cheese_curd_image.get_height() // 2))
    for i in range(cow_count):
        screen.blit(cow_image, (20 + i * (cow_image.get_width() + 5), 100))

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)

pygame.quit()
sys.exit()
