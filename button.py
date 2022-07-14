import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self):
        self.bot = pygame.image.load("assets/bot.png")
        self.bot = pygame.transform.scale(self.bot, (230, 59))
        self.bot_rect = self.bot.get_rect()
        self.bot_rect.x = 840
        self.bot_rect.y = 280

        self.onevsone = pygame.image.load("assets/1v1.png")
        self.onevsone = pygame.transform.scale(self.onevsone, (230, 59))
        self.onevsone_rect = self.onevsone.get_rect()
        self.onevsone_rect.x = 840
        self.onevsone_rect.y = 400

        self.solo = pygame.image.load("assets/solo.png")
        self.solo = pygame.transform.scale(self.solo, (230, 59))
        self.solo_rect = self.solo.get_rect()
        self.solo_rect.x = 840
        self.solo_rect.y = 520

