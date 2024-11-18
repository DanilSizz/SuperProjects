import pygame
class Keyhandler:

    def __init__(self):
        pass

    def handle_keyboard(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP:
                    print("Нажата клавиша ВВЕРХ")
                case pygame.K_DOWN:
                    print("Нажата клавиша ВНИЗ")
                case pygame.K_LEFT:
                    print("Нажата клавиша ВЛЕВО")
                case pygame.K_RIGHT:
                    print("Нажата клавиша ВПРАВО")
                case pygame.K_ESCAPE:
                    return False  # Выход из игры при нажатии ESC
                case _:
                    print(f"Нажата другая клавиша: {pygame.key.name(event.key)}")

