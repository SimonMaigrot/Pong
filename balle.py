import pygame
import random

class Balle(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("assets/balle.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = 949
        self.rect.y = 285
        self.speed = 2
        self.speed_y = 2
        self.direction = random.randint(0, 1)

    def move_left(self):
        if self.rect.x <= 1890:
            self.rect.x -= self.speed

    def move_right(self):
        if self.rect.x >= 0:
            self.rect.x += self.speed

    def move_up(self):
        if self.rect.y >= 0:
            self.rect.y -= self.speed_y

    def move_down(self):
        if self.rect.y <= 1050:
            self.rect.y += self.speed_y
