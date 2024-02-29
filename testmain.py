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
cow_image = pygame.transform.scale(cow_image, (cow_image.get_width() // 20, cow_image.get_height() // 20))

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cheese Curd Clicker")

# Fonts
font = pygame.font.SysFont(None, 40)

# Game variables
curds = 500000
cash = 0
curds_per_click = 1
curds_per_second = 0
cow_count = 0
cow_cost = 100
cow_production = 5
curd_value = 5.99

# Curd Market variables
curd_market_cost = 5000
curd_market_units = 0
curd_market_income = 1
curd_market_interval = 1  # in seconds
last_curd_market_time = time.time()

# Buttons
click_button = pygame.Rect(WIDTH//2 - 500, HEIGHT//2 - 200, 100, 100)
buy_cow_button = pygame.Rect(WIDTH - 150, 50, 100, 50)
sell_button = pygame.Rect(WIDTH//2 - 500, HEIGHT//2 - 50, 100, 100)
buy_curd_market_button = pygame.Rect(WIDTH - 150, 120, 150, 50)  # New button for buying curd market units

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
                    if cash >= cow_cost:
                        cash -= cow_cost
                        cow_count += 1
                        cow_cost += cow_cost * 0.1
                        curds_per_second += cow_production
                # Check if click is on the sell button
                elif sell_button.collidepoint(event.pos):
                    if curds > 0:
                        curds -= 1
                        cash += curd_value
                # Check if click is on the buy curd market button
                elif buy_curd_market_button.collidepoint(event.pos):
                    if curds >= curd_market_cost:
                        curds -= curd_market_cost
                        curd_market_units += 1

    # Update game logic
    current_time = time.time()
    if current_time - last_time >= 1:
        last_time = current_time
        curds += curds_per_second

        # Check if it's time to generate income from the curd market
        if current_time - last_curd_market_time >= curd_market_interval:
            last_curd_market_time = current_time
            curds += curd_market_income * curd_market_units
            cash += curd_market_income * curd_value * curd_market_units

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, click_button)
    pygame.draw.rect(screen, GRAY, buy_cow_button)
    pygame.draw.rect(screen, GRAY, sell_button)
    pygame.draw.rect(screen, GRAY, buy_curd_market_button)  # Draw the buy curd market button

    # Render text and images
    click_text = font.render("Create Curd", True, BLACK)
    buy_cow_text = font.render("Buy Cow", True, BLACK)
    sell_text = font.render("Sell Curd", True, BLACK)
    buy_curd_market_text = font.render("Buy Curd Market", True, BLACK)  # New text for buy curd market button
    curds_text = font.render(f"Cheese Curds: {curds}", True, BLACK)
    cash_text = font.render(f"Cash: {cash}", True, BLACK)
    cow_count_text = font.render(f"Cow Count: {cow_count}", True, BLACK)
    curd_market_units_text = font.render(f"Curd Market Units: {curd_market_units}", True, BLACK)  # Display the number of curd market units
    screen.blit(click_text, (click_button.centerx - click_text.get_width() // 2, click_button.centery - click_text.get_height() // 2))
    screen.blit(buy_cow_text, (buy_cow_button.centerx - buy_cow_text.get_width() // 2, buy_cow_button.centery - buy_cow_text.get_height() // 2))
    screen.blit(sell_text, (sell_button.centerx - sell_text.get_width() // 2, sell_button.centery - sell_text.get_height() // 2))
    screen.blit(buy_curd_market_text, (buy_curd_market_button.centerx - buy_curd_market_text.get_width() // 2, buy_curd_market_button.centery - buy_curd_market_text.get_height() // 2))  # New text position
    screen.blit(curds_text, (10, 10))
    screen.blit(cash_text, (10, 50))
    screen.blit(cow_count_text, (10, 90))
    screen.blit(curd_market_units_text, (10, 130))  # Display the number of curd market units
    screen.blit(cheese_curd_image, (click_button.centerx - cheese_curd_image.get_width() // 2, click_button.centery - cheese_curd_image.get_height() // 2))
    Hei = 150
    for i in range(cow_count):
        wid = cow_image.get_width()
        if wid >= 1920:
            Hei -= 100
            wid = 0
        screen.blit(cow_image, (300 + i * (wid + 5), Hei))

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)

pygame.quit()
sys.exit()
