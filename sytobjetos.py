import pygame
import random

vec2 = pygame.math.Vector2


class CachoSnake:
    def __init__(self, game):
        self.game = game
        self.ancho = self.game.ANCHO
        self.rect = pygame.rect.Rect([0, 0, self.ancho, self.ancho])
        self.elegir_rnd = game.RESOLUCION // self.ancho
        self.rect.center = self.obtener_rnd()
        self.direccion = vec2(0, 0)
        self.largo_serp = 1
        self.segmentos = []
        self.direcciones = {pygame.K_UP: 1, pygame.K_DOWN: 1, pygame.K_LEFT: 1, pygame.K_RIGHT: 1}

    def leer_teclado(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.direcciones[pygame.K_UP]:
                self.direccion = vec2(0, -self.ancho)
                self.direcciones = {pygame.K_UP: 1, pygame.K_DOWN: 0, pygame.K_LEFT: 1, pygame.K_RIGHT: 1}

            if event.key == pygame.K_DOWN and self.direcciones[pygame.K_DOWN]:
                self.direccion = vec2(0, self.ancho)
                self.direcciones = {pygame.K_UP: 0, pygame.K_DOWN: 1, pygame.K_LEFT: 1, pygame.K_RIGHT: 1}

            if event.key == pygame.K_LEFT and self.direcciones[pygame.K_LEFT]:
                self.direccion = vec2(-self.ancho, 0)
                self.direcciones = {pygame.K_UP: 1, pygame.K_DOWN: 1, pygame.K_LEFT: 1, pygame.K_RIGHT: 0}

            if event.key == pygame.K_RIGHT and self.direcciones[pygame.K_RIGHT]:
                self.direccion = vec2(self.ancho, 0)
                self.direcciones = {pygame.K_UP: 1, pygame.K_DOWN: 1, pygame.K_LEFT: 0, pygame.K_RIGHT: 1}


    def obtener_rnd(self):
        return [random.randrange(self.elegir_rnd) * self.ancho + self.ancho // 2,
                random.randrange(self.elegir_rnd) * self.ancho + self.ancho // 2]

    def check_limites(self):
        if self.rect.left < 0 or self.rect.right > self.game.RESOLUCION:
            self.game.new_game()

        if self.rect.top < 0 or self.rect.bottom > self.game.RESOLUCION:
            self.game.new_game() 

    def check_comermanzana(self):
        if self.rect.center == self.game.manzana.rect.center:
            self.game.manzana.rect.center = self.obtener_rnd()
            self.largo_serp +=1
            self.game.puntos += 1

    def check_autocolision(self):
        if len(self.segmentos) != len(set(segmento.center for segmento in self.segmentos)):
            self.new_game()

    def mover_serpiente(self):
        self.rect.move_ip(self.direccion)
        self.segmentos.append(self.rect.copy())
        self.segmentos = self.segmentos[-self.largo_serp:]

    def update(self):
        self.mover_serpiente()
        self.check_autocolision()
        self.check_limites()
        self.check_comermanzana()

    def dibuja_serpiente(self):
        for segmento in segmentos:
            pygame.draw.rect(self.game.pantalla, self.game.VERDE, segmento)

class Manzana:
    def __init__(self, game):
        self.game = game
        self.ancho = self.game.ANCHO
        self.rect = pygame.rect.Rect([0, 0, self.ancho, self.ancho])
        self.rect.center = self.game.cachoSnake.obtener_rnd()

    def dibuja_manzana(self):
        #pygame.draw.rect(self.game.pantalla, self.game.ROJO, self.rect)
        pygame.draw.circle(self.game.pantalla, self.game.ROJO, self.rect.center, self.ancho // 2)

