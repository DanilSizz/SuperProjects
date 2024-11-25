import os
import time
import random

class Dot:
    def __init__(self):
        self.dot = '*'

    def add_dot(self):
        return self.dot

class Snake:
    DEFAULT_MOVE_DIR = 'd'

    def __init__(self, x=10, y=10):
        self.head = '*'
        self.body = []
        self.x = x
        self.y = y
        self.dir = None
        self.speed = 1
        self.b = Board(width=40, height=20)
        self.dot = Dot()

    def move(self, fruit):
        self.dir = input()
        
        if self.dir == 'a':
            self.x -= self.speed  # left
        elif self.dir == 'd':
            self.x += self.speed  # right
        elif self.dir == 'w':
            self.y -= self.speed  # up
        elif self.dir == 's':
            self.y += self.speed  # down

        # Check for fruit collision
        if self.x == fruit.x and self.y == fruit.y:
            fruit.x = random.randint(1, self.b.width - 2)
            fruit.y = random.randint(1, self.b.height - 2)
            self.body.append(self.dot.add_dot())

        # Move the snake body
        if self.body:
            self.body.insert(0, (self.x, self.y))  # add new head
            if len(self.body) > 1:
                self.body.pop()  # remove the tail

class Fruit:
    def __init__(self):
        self.b = Board(width=40, height=20)
        self.x = random.randint(1, self.b.width - 2)
        self.y = random.randint(1, self.b.height - 2)
        self.fruit = 'A'

    def print_fruit(self):
        print(self.fruit, end='')

class Board:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height

    def print_board(self, snake, fruit):
        os.system('cls')  # Clear the console for better visual effect
        for i in range(self.height):
            for j in range(self.width):
                if (snake.x, snake.y) == (j, i):
                    print(snake.head, end='')
                elif (fruit.x, fruit.y) == (j, i):
                    fruit.print_fruit()
                elif j == 0 or j == self.width - 1 or i == 0 or i == self.height - 1:
                    print('#', end='')
                elif (j, i) in snake.body:
                    print(snake.dot.add_dot(), end='')
                else:
                    print(' ', end='')
            print()

class Game:
    def __init__(self):
        pass

    def start_game(self):
        board = Board(width=40, height=20)
        snake = Snake(10, 10)
        fruit = Fruit()

        while not ((snake.x > board.width - 1 or snake.x < 1) or (snake.y > board.height - 1 or snake.y < 1)):
            board.print_board(snake, fruit)
            snake.move(fruit)
            time.sleep(0.15)
        else:
            print("GAME OVER!!!")

game = Game()
game.start_game()