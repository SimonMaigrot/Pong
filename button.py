import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("assets/play.png")
        self.rect = self.image.get_rect()
        self.rect.x = 840
        self.rect.y = 280
