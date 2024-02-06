import pygame
import sys
import random
import os

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
curd_per_second = 1

# Check if SaveData.txt exists
if os.path.exists("SaveData.txt"):
    with open("SaveData.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if "Curd Count" in line:
                curd_count = int(line.split(":")[1])
            elif "Curd per Click" in line:
                curd_per_click = int(line.split(":")[1])
            elif "Curd per Second" in line:
                curd_per_second = int(line.split(":")[1])

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cheese Curd Clicker")
pygame_icon = pygame.image.load('assets/CurdClickerIcon.png')
clock = pygame.time.Clock()
font = pygame.font.Font(None, FONT_SIZE)

# Load cheese curd image
cheese_curd_image = pygame.image.load('assets/CheddarCurd.png')

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
    
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("SaveData.txt", "w") as file:
                file.write(f"Curd Count: {int(curd_count)}\n")
                file.write(f"Curd per Click: {curd_per_click}\n")
                file.write(f"Curd per Second: {curd_per_second}\n")
            running = False
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            curd_count += curd_per_click

    generate_curd()

    # Draw cheese curd image
    screen.blit(cheese_curd_image, (WIDTH // 2 - 25, HEIGHT // 2 - 25))

    draw_text(f"Curd Count: {int(curd_count)}", 20, 20)
    draw_text(f"Curd per Click: {curd_per_click}", 20, 60)
    draw_text(f"Curd per Second: {curd_per_second}", 20, 100)

    pygame.display.flip()

pygame.quit()