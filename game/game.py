#!/usr/bin/python
# Away Game
import pygame, sys, operator, time, colors, classes, functions
from   functions import *
from   pygame.locals import *
from   pygame.time import *
from   colors import *
from   classes import *

pygame.init()
# Quick Commit test
running = True

screen = pygame.display.set_mode((800, 600), RESIZABLE)
pygame.display.set_caption('Float')

player = CharacterObject(0, 0, 10, 10)
grounds = generate_platforms()


# Rendering and drawing
def draw():
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    screen.fill(BLACK)
    background.fill(BLACK)
    screen.blit(background, (0, 0))

    pygame.draw.rect(screen, WHITE, player.get_rect())
    paint_platforms(screen, grounds)
    pygame.display.update()


def main():
    while running:
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            player.x += 2
            player.xv += .5
        if keys[K_LEFT]:
            player.x += -2
            player.xv += -.5
        if keys[K_DOWN]:
            player.yv += .1

        if player.onGround:
            player.yv = 0
        else:
            player.yv += .3

        player.pos_update()

        for plat in grounds:
            if player.get_rect().colliderect(plat.get_rect()):
                # player.xv = dampen_speed(player.xv, .5)
                # print("collision at " + str(player.x) + ", " + str(player.y) )
                jumpable = solid_collision(player, plat)
                if keys[K_UP] and jumpable:
                    player.yv += -7
                    player.onGround = False
                # plat.pos_update()

        if player.onGround and keys[K_UP]:
            player.yv += -7
            player.onGround = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        Clock().tick(30)

        draw()


main()
