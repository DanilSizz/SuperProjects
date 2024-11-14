import pygame
import random
import sys
import math

# Инициализация Pygame
pygame.init()

# Параметры окна
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bouncing Colorful Balls')

# Часы для контроля FPS
clock = pygame.time.Clock()

# Класс для шарика
class Ball:
    def __init__(self, x, y):
        self.radius = random.randint(30, 50)
        self.base_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color = list(self.base_color)
        self.x = x
        self.y = y
        self.vx = random.choice([2, 1]) * random.uniform(1, 5)
        self.vy = random.choice([2, 1]) * random.uniform(1, 5)
        self.time = 0  # Время для изменения цвета

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Проверка на столкновение со стенками
        if self.x - self.radius < 0 or self.x + self.radius > width:
            self.vx = -self.vx
        if self.y - self.radius < 0 or self.y + self.radius > height:
            self.vy = -self.vy

    def draw(self, surface):
        # Изменение цвета шарика
        self.time += 0.05  # Увеличиваем время для изменения цвета
        self.color[0] = (self.base_color[0] + int(127 * math.sin(self.time))) % 256
        self.color[1] = (self.base_color[1] + int(127 * math.sin(self.time + 2))) % 256
        self.color[2] = (self.base_color[2] + int(127 * math.sin(self.time + 4))) % 256
        
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

    def check_collision(self, other):
        # Проверка на столкновение с другим шариком
        dx = self.x - other.x
        dy = self.y - other.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance < self.radius + other.radius:
            # Простая обработка столкновения
            self.vx, other.vx = other.vx, self.vx
            self.vy, other.vy = other.vy, self.vy

# Список шариков
balls = []

# Главный цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Создание нового шарика в месте клика
            x, y = event.pos
            balls.append(Ball(x, y))

    # Обновление экрана
    screen.fill((0, 0, 0))
    for i in range(len(balls)):
        balls[i].move()
        balls[i].draw(screen)

        # Проверка столкновений между шариками
        for j in range(i + 1, len(balls)):
            balls[i].check_collision(balls[j])

    pygame.display.flip()
    clock.tick(60)