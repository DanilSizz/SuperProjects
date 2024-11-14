import pygame

def main():
    pygame.init()

class BallGame():
    def __init__(self, screen_size, fps = 60, gameState = True):
        self.screen = pygame.display.set_mode(screen_size)
        self.framesPerSecond = fps
        self.gameState = gameState
        self.clock = pygame.time.Clock()
        
    def run(self):

        while self.gameState != False:
            self.clock.tick(self.framesPerSecond)

            self.keyboardEvents()
            
            pygame.display.update()

    def setBackground(self, imagePath):
        self.background = pygame.image.load(imagePath)
        self.background = pygame.transform.scale(self.background, self.screen.get_size())
            
    def keyboardEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameState = False



newGame = BallGame((800, 600), 60, True)
newGame.run()