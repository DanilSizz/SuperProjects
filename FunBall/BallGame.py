import pygame
import Keyhandler

class BallGame:

    #width = 800
    #height = 600

    #Конструктор класса и параметры self
    def __init__(self, width = 800, height = 600, FPS = 60):
        self.set_pygame()
        self.set_screen(width, height)
        self.set_screen_mode((self.width, self.height))
        self.set_FPS(FPS)
        self.set_clock()
        self.Keyhandler = Keyhandler.Keyhandler()

    def set_FPS(self, FPS):
        self.FPS = FPS

    def set_clock(self):
        self.clock = pygame.time.Clock()

    def set_screen(self, width, height):
        self.width = width
        self.height = height

    def set_screen_mode(self, size):
        self.screen = pygame.display.set_mode(size)
    
    def set_pygame(self):
        pygame.init()

    def game_cycle(self):
        while True:
            self.clock.tick(60)
            self.screen.fill((0,0,0))
            self.Keyhandler.handle_keyboard()


        pass

BallGame().game_cycle()



