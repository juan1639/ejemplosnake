import pygame
import sys
from objetos import *


class Game:
    def __init__(self):
        pygame.init()
        self.AZUL_OSC = (0, 0, 90)
        self.AMARILLO = (220, 190, 0)
        self.BLANCO = (240, 240, 240)
        self.GRIS_C = (50, 50, 50)
        self.ROJO = (230, 0, 0)
        self.VERDE = (0, 230, 0)
        self.VERDE_C = (0, 150, 0)
        self.gameover = False
        self.RESOLUCION = 600
        self.FPS = 15
        self.ANCHO = 40
        self.pantalla = pygame.display.set_mode([self.RESOLUCION] * 2)
        self.reloj = pygame.time.Clock()
        self.new_game()

    def dibuja_cuadricula(self):
        for x in range(0, self.RESOLUCION, self.ANCHO):
            pygame.draw.line(self.pantalla, self.GRIS_C, (x, 0), (x, self.RESOLUCION))

        for y in range(0, self.RESOLUCION, self.ANCHO):
            pygame.draw.line(self.pantalla, self.GRIS_C, (0, y), (self.RESOLUCION, y))

    def dibuja_texto(self, surface, texto, size, x, y):
        font = pygame.font.SysFont("serif", size)
        text_surface = font.render(texto, True, self.AMARILLO)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surface.blit(text_surface, text_rect)

    def new_game(self):
        self.puntos = 0
        self.cachoSnake = CachoSnake(self)
        self.manzana = Manzana(self)

    def update(self):
        self.cachoSnake.update()
        pygame.display.flip()
        self.reloj.tick(self.FPS)

    def draw(self):
        self.pantalla.fill(self.AZUL_OSC)
        self.dibuja_cuadricula()
        self.manzana.dibuja_manzana()
        self.cachoSnake.dibuja_serpiente()
        self.dibuja_texto(self.pantalla, f'Manzanas: {str(self.puntos)}', 25, self.RESOLUCION // 2, 10)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.cachoSnake.leer_teclado(event)

    def run(self):
        while not self.gameover:
            self.check_event()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()