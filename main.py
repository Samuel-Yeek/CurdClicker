import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1366, 768
FPS = 60
WHITE = (255, 255, 255)
FONT_SIZE = 36

# Game variables
curd_count = 0
curd_per_click = 1
curd_per_second = 0

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cheese Curd Clicker")
clock = pygame.time.Clock()
font = pygame.font.Font(None, FONT_SIZE)

# Load cheese curd image
cheese_curd_image = pygame.image.load("CheddarCurd.png")
cheese_curd_image = pygame.transform.scale(cheese_curd_image, (50, 50))

# Upgrade class
class Upgrade:
    def __init__(self, name, cost, curds_per_second):
        self.name = name
        self.cost = cost
        self.curds_per_second = curds_per_second

# Upgrades
upgrade1 = Upgrade("Upgrade 1", 10, 1)
upgrade2 = Upgrade("Upgrade 2", 50, 5)

upgrades = [upgrade1, upgrade2]

# Functions
def draw_text(text, x, y, color=WHITE):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

def generate_curd():
    global curd_count
    curd_count += curd_per_second / FPS

# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            curd_count += curd_per_click

    generate_curd()

    # Draw cheese curd image
    screen.blit(cheese_curd_image, (WIDTH // 2 - 25, HEIGHT // 2 - 25))

    draw_text(f"Curd Count: {int(curd_count)}", 20, 20)
    draw_text(f"Curd per Click: {curd_per_click}", 20, 60)
    draw_text(f"Curd per Second: {curd_per_second}", 20, 100)

    draw_text("Upgrades:", 20, 150)
    y_offset = 180
    for upgrade in upgrades:
        draw_text(f"{upgrade.name}: Cost - {upgrade.cost}, +{upgrade.curds_per_second} per second", 20, y_offset)
        y_offset += 40

    pygame.display.flip()

pygame.quit()