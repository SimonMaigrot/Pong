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
    button.image = pygame.image.load("assets/play.png")
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
                if pygame.Rect.collidepoint(button.rect, (mouse_x, mouse_y)):
                    STAT = "play"

    ''' Jeux '''
    # Déplacement balle
    if STAT == "play":
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

    # Bouton effect
    if pygame.Rect.collidepoint(button.rect, (mouse_x, mouse_y)):
        button.image = pygame.transform.scale(button.image, (242, 89))
        button.rect.x = 835
        button.rect.y = 275
    else:
        button.image = pygame.transform.scale(button.image, (232, 79))
        button.rect.x = 840
        button.rect.y = 280

    ''' Affichage '''
    screen.blit(screen, (0, 0))
    screen.fill([0, 0, 0])
    if STAT == "menu":
        screen.blit(menu, (520, 0))
        screen.blit(button.image, button.rect)
    if STAT == "play":
        screen.blit(barre, (960, 0))
        screen.blit(rectangle.gauche, (rectangle.gauche_rect))
        screen.blit(rectangle.droite, (rectangle.droite_rect))
        screen.blit(balle.image, balle.rect)
        screen.blit(score_text_left, (900, 20))
        screen.blit(score_text_right, (1000, 20))
    pygame.display.flip()
    clock.tick(144)

pygame.quit()
