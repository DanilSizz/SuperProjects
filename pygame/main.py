import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 1920, 1080
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пин-понг")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Параметры ракетки
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 200
paddle_speed = 30

# Параметры мяча
BALL_SIZE = 40
ball_speed_x = 20 * random.choice((1, -1))
ball_speed_y = 20 * random.choice((1, -1))

# Игровые объекты
player1 = pygame.Rect(50, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)

# Основной игровой цикл
running = True
while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= paddle_speed
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += paddle_speed
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= paddle_speed
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += paddle_speed

    # Движение мяча
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Проверка столкновений с верхней и нижней стенками
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Проверка столкновений с ракетками
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    # Проверка выхода мяча за границы
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    # Отрисовка объектов
    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, player1)
    pygame.draw.rect(win, WHITE, player2)
    pygame.draw.ellipse(win, WHITE, ball)
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()