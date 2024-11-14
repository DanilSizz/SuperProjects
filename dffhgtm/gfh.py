import pygame
import random
import sys
import math

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 1920, 1080
FPS = 165

# Цвета
BLACK = (0, 0, 0)


# Класс для шарика
class Ball:
    def __init__(self, x, y):
        self.radius = random.randint(10, 50)  # Случайный размер
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Случайный цвет
        self.x = x
        self.y = y
        self.dx = random.choice([-1, 1]) * random.uniform(2, 5)  # Случайное направление и скорость
        self.dy = random.choice([-1, 1]) * random.uniform(2, 5)

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Проверка на столкновение со стенками
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.dx *= -1  # Отскок от левой/правой стенки
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.dy *= -1  # Отскок от верхней/нижней стенки

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def check_collision(self, other):
        # Проверка коллизии с другим шариком
        distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        if distance < self.radius + other.radius:
            # Простая обработка коллизии: меняем направление
            self.dx *= -1
            self.dy *= -1
            other.dx *= -1
            other.dy *= -1

# Основная функция
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bouncing Balls")
    clock = pygame.time.Clock()
    balls = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Создание нового шарика при клике
                mouse_x, mouse_y = event.pos
                balls.append(Ball(mouse_x, mouse_y))

        screen.fill(BLACK)

        # Движение и отрисовка шариков
        for ball in balls:
            ball.move()
            ball.draw(screen)

        # Проверка коллизий между шариками
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                balls[i].check_collision(balls[j])

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()