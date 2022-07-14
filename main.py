import pygame
import random
pygame.init()
from button import Button
from rectangle import Rectangle
from balle import Balle

# Important
WIDTH = 1920
HEIGHT = 630
STAT = "menu"

# Images
menu = pygame.image.load("assets/menu.png")
barre = pygame.image.load("assets/rectangle.jpg")
barre = pygame.transform.scale(barre, (8, 630))

# Variables
button = Button()
rectangle = Rectangle()
balle = Balle()
clock = pygame.time.Clock()

# Texte
score_left = 0
score_right = 0
myfont = pygame.font.Font(None,72)
score_text_left = myfont.render(str(int(score_left)), 1, (0, 0, 0))
score_text_right = myfont.render(str(int(score_right)), 1, (0, 0, 0))

# Déplacement Balle
position = 1 #0 left / 1 right

screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
while running:

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Actualisation
    button.bot = pygame.image.load("assets/bot.png")
    button.onevsone = pygame.image.load("assets/1v1.png")
    button.solo = pygame.image.load("assets/solo.png")
    score_text_left = myfont.render(str(int(score_left)), 1, (255, 255, 255))
    score_text_right = myfont.render(str(int(score_right)), 1, (255, 255, 255))

    ''' Evenements '''
    for event in pygame.event.get():
        # Quitter
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
        # EVENT MENU
        if STAT == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect.collidepoint(button.bot_rect, (mouse_x, mouse_y)):
                    STAT = "bot"
                if pygame.Rect.collidepoint(button.onevsone_rect, (mouse_x, mouse_y)):
                    STAT = "onevsone"
                if pygame.Rect.collidepoint(button.solo_rect, (mouse_x, mouse_y)):
                    STAT = "solo"

    ''' Jeux '''
    # Déplacement balle
    if STAT == "onevsone":
        if position == 0:
            balle.move_left()
        if position == 1:
            balle.move_right()

        ''' Collisions barre '''
        if pygame.Rect.colliderect(balle.rect, rectangle.droite_rect):
            balle.move_left()
            position = 0
            balle.speed += 0.2
        if pygame.Rect.colliderect(balle.rect, rectangle.gauche_rect):
            balle.move_right()
            position = 1
            balle.speed += 0.2

        ''' Score '''
        if balle.rect.x <= 0:
            score_right += 1
            balle.rect.x = 949
            balle.rect.y = 285
            balle.speed = 2
        if balle.rect.x >= 1920:
            score_left += 1
            balle.rect.x = 949
            balle.rect.y = 285
            balle.speed = 2

        ''' Reset game'''
        if score_left >= 5 or score_right >= 5:
            STAT = "menu"
            score_left = 0
            score_right = 0
            rectangle.gauche_rect.y = 250
            rectangle.droite_rect.y = 250

        ''' Déplacement '''
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            if rectangle.droite_rect.y >= 0:
                rectangle.droite_rect.y -= rectangle.speed

        if pressed[pygame.K_DOWN]:
            if rectangle.droite_rect.y <= 480:
                rectangle.droite_rect.y += rectangle.speed

        if pressed[pygame.K_z]:
            if rectangle.gauche_rect.y >= 0:
                rectangle.gauche_rect.y -= rectangle.speed

        if pressed[pygame.K_s]:
            if rectangle.gauche_rect.y <= 480:
                rectangle.gauche_rect.y += rectangle.speed

        '''Direction balle'''
        # direction balle bas
        if balle.direction == 0:
            balle.move_down()
        # direction balle haut
        if balle.direction == 1:
            balle.move_up()

        '''Rebonds balle'''
        if balle.rect.y >= 600:
            balle.direction = 1
            balle.speed_y = random.randint(int(balle.speed), int(balle.speed + 1))
        if balle.rect.y <= 0:
            balle.direction = 0
            balle.speed_y = random.randint(int(balle.speed), int(balle.speed + 1))

    if STAT  == "bot":
        if position == 0:
            balle.move_left()
        if position == 1:
            balle.move_right()

        ''' Collisions barre '''
        if pygame.Rect.colliderect(balle.rect, rectangle.droite_rect):
            balle.move_left()
            position = 0
            balle.speed += 0.2
        if pygame.Rect.colliderect(balle.rect, rectangle.gauche_rect):
            balle.move_right()
            position = 1
            balle.speed += 0.2

        ''' Score '''
        if balle.rect.x <= 0:
            score_right += 1
            balle.rect.x = 949
            balle.rect.y = 285
            balle.speed = 2
        if balle.rect.x >= 1920:
            score_left += 1
            balle.rect.x = 949
            balle.rect.y = 285
            balle.speed = 2

        ''' Reset game'''
        if score_left >= 10 or score_right >= 10:
            STAT = "menu"
            score_left = 0
            score_right = 0
            rectangle.gauche_rect.y = 250
            rectangle.droite_rect.y = 250

        ''' Déplacement '''
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_z]:
            if rectangle.gauche_rect.y >= 0:
                rectangle.gauche_rect.y -= rectangle.speed

        if pressed[pygame.K_s]:
            if rectangle.gauche_rect.y <= 480:
                rectangle.gauche_rect.y += rectangle.speed

        '''Direction balle, rectangle'''
        # direction balle bas
        if balle.direction == 0:
            balle.move_down()
        # direction balle haut
        if balle.direction == 1:
            balle.move_up()

        '''Direction rectangle'''
        if rectangle.droite_rect.y >= -1 :
            rectangle.droite_rect.y = balle.rect.y
        if rectangle.droite_rect.y >= 485:
            rectangle.droite_rect.y = 485

        '''Rebonds balle'''
        if balle.rect.y >= 600:
            balle.direction = 1
            balle.speed_y = random.randint(int(balle.speed), int(balle.speed + 1))
        if balle.rect.y <= 0:
            balle.direction = 0
            balle.speed_y = random.randint(int(balle.speed), int(balle.speed + 1))

    if STAT == "solo":
        if position == 0:
            balle.move_left()
        if position == 1:
            balle.move_right()

        ''' Collisions barre '''
        if pygame.Rect.colliderect(balle.rect, rectangle.droite_rect):
            balle.move_left()
            position = 0
            balle.speed += 0.2
        if pygame.Rect.colliderect(balle.rect, rectangle.gauche_rect):
            balle.move_right()
            position = 1
            balle.speed += 0.2

        ''' Score '''
        if balle.rect.x <= 0:
            score_right += 1
            balle.rect.x = 949
            balle.rect.y = 285
            balle.speed = 2
        if balle.rect.x >= 1920:
            score_left += 1
            balle.rect.x = 949
            balle.rect.y = 285
            balle.speed = 2

        ''' Reset game'''
        if score_left >= 10 or score_right >= 10:
            STAT = "menu"
            score_left = 0
            score_right = 0
            rectangle.gauche_rect.y = 250
            rectangle.droite_rect.y = 250

        ''' Déplacement '''
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_z]:
            if rectangle.gauche_rect.y >= 0:
                rectangle.gauche_rect.y -= rectangle.speed
                rectangle.droite_rect.y -= rectangle.speed

        if pressed[pygame.K_s]:
            if rectangle.gauche_rect.y <= 480:
                rectangle.gauche_rect.y += rectangle.speed
                rectangle.droite_rect.y += rectangle.speed

        '''Direction balle'''
        # direction balle bas
        if balle.direction == 0:
            balle.move_down()
        # direction balle haut
        if balle.direction == 1:
            balle.move_up()

        '''Rebonds balle'''
        if balle.rect.y >= 600:
            balle.direction = 1
            balle.speed_y = random.randint(int(balle.speed), int(balle.speed + 1))
        if balle.rect.y <= 0:
            balle.direction = 0
            balle.speed_y = random.randint(int(balle.speed), int(balle.speed + 1))

    # Bouton effect
    if pygame.Rect.collidepoint(button.bot_rect, (mouse_x, mouse_y)):
        button.bot = pygame.transform.scale(button.bot, (240, 69))
        button.bot_rect.x = 835
        button.bot_rect.y = 275
    else:
        button.bot = pygame.transform.scale(button.bot, (230, 59))
        button.bot_rect.x = 840
        button.bot_rect.y = 280

    if pygame.Rect.collidepoint(button.onevsone_rect, (mouse_x, mouse_y)):
        button.onevsone = pygame.transform.scale(button.onevsone, (240, 69))
        button.onevsone_rect.x = 835
        button.onevsone_rect.y = 395
    else:
        button.onevsone = pygame.transform.scale(button.onevsone, (230, 59))
        button.onevsone_rect.x = 840
        button.onevsone_rect.y = 400

    if pygame.Rect.collidepoint(button.solo_rect, (mouse_x, mouse_y)):
        button.solo = pygame.transform.scale(button.solo, (240, 69))
        button.solo_rect.x = 835
        button.solo_rect.y = 515
    else:
        button.solo = pygame.transform.scale(button.solo, (230, 59))
        button.solo_rect.x = 840
        button.solo_rect.y = 520

    ''' Affichage '''
    screen.blit(screen, (0, 0))
    screen.fill([0, 0, 0])
    if STAT == "menu":
        screen.blit(menu, (520, 0))
        screen.blit(button.bot, button.bot_rect)
        screen.blit(button.onevsone, button.onevsone_rect)
        screen.blit(button.solo, button.solo_rect)
    if STAT == "onevsone":
        screen.blit(barre, (960, 0))
        screen.blit(rectangle.gauche, (rectangle.gauche_rect))
        screen.blit(rectangle.droite, (rectangle.droite_rect))
        screen.blit(balle.image, balle.rect)
        screen.blit(score_text_left, (900, 20))
        screen.blit(score_text_right, (1000, 20))
    if STAT == "bot":
        screen.blit(barre, (960, 0))
        screen.blit(rectangle.gauche, (rectangle.gauche_rect))
        screen.blit(rectangle.droite, (rectangle.droite_rect))
        screen.blit(balle.image, balle.rect)
        screen.blit(score_text_left, (900, 20))
        screen.blit(score_text_right, (1000, 20))
    if STAT == "solo":
        screen.blit(barre, (960, 0))
        screen.blit(rectangle.gauche, (rectangle.gauche_rect))
        screen.blit(rectangle.droite, (rectangle.droite_rect))
        screen.blit(balle.image, balle.rect)
        screen.blit(score_text_left, (900, 20))
        screen.blit(score_text_right, (1000, 20))
    pygame.display.flip()
    clock.tick(144)

pygame.quit()
