import pygame

class Rectangle(pygame.sprite.Sprite):
    def __init__(self):
        self.gauche = pygame.image.load("assets/rectangle.jpg")
        self.gauche = pygame.transform.scale(self.gauche, (30, 150))
        self.gauche_rect = self.gauche.get_rect()
        self.gauche_rect.x = 10
        self.gauche_rect.y = 250
        self.droite = pygame.image.load("assets/rectangle.jpg")
        self.droite = pygame.transform.scale(self.droite, (30, 150))
        self.droite_rect = self.droite.get_rect()
        self.droite_rect.x = 1882
        self.droite_rect.y = 250
        self.speed = 2
