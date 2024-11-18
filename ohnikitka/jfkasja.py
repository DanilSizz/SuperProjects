import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1920, 1080
BACKGROUND_COLOR = (0, 0, 0)
TEXT_COLOR = (0, 255, 0)
FONT_SIZE = 35
COLUMN_WIDTH = 5
FALL_SPEED = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Заставка из Матрицы")

font = pygame.font.Font(None, FONT_SIZE)

columns = [0] * (WIDTH // COLUMN_WIDTH)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    for i in range(len(columns)):
        if random.random() < 0.1:  
            columns[i] = 0  

        if columns[i] < HEIGHT:
            text = font.render(random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"), True, TEXT_COLOR)
            screen.blit(text, (i * COLUMN_WIDTH, columns[i]))
            columns[i] += FALL_SPEED

    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()