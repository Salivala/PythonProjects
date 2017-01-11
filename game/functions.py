import pygame, sys, classes, colors, heapq
from colors import *
from classes import *
from random import randint
from random import uniform


def generate_platforms():
    platforms = []
    for x in range(0, randint(30, 50)):
        platforms.append(MoveableGameObject(uniform(0, 800), randint(0, 600), randint(10, 70), randint(5, 70)))
    for plat in platforms:
        # plat.xv = uniform(0, 2)
        # plat.yv = uniform(0, 2)
        None

    return platforms


def paint_platforms(scr, platforms):
    for plat in platforms:
        pygame.draw.rect(scr, OTHER, plat.get_rect())


def dampen_speed(var, damp_amount):
    tmp = var
    if var > 0 and var > 0 + .2:
        tmp = var - damp_amount
    elif var < 0 and var < 0 - .2:
        tmp = var + damp_amount
    else:
        tmp = 0
    return tmp


def solid_collision(mov_obj, stati_obj):
    jumpable = False
    if mov_obj.get_rect().colliderect(stati_obj.get_rect()):
        top_dif = abs(mov_obj.get_rect().bottom - stati_obj.get_rect().top)
        bottom_dif = abs(stati_obj.get_rect().bottom - mov_obj.get_rect().top)
        right_dif = abs(mov_obj.get_rect().left - stati_obj.get_rect().right)
        left_def = abs(stati_obj.get_rect().left - mov_obj.get_rect().right)
        dif_list = [top_dif, bottom_dif, right_dif, left_def]
        print(top_dif)
        print(bottom_dif)
        smallest = heapq.nsmallest(1, dif_list)

        mov_obj.xv = 0
        print(smallest)
        if top_dif in smallest:
            print("top bound")
            mov_obj.y += -1
            mov_obj.yv = stati_obj.yv
            mov_obj.xv = stati_obj.xv
            jumpable = True
            mov_obj.onGround = True
        elif bottom_dif in smallest:
            print("bottom bound")
            mov_obj.y += 1
            mov_obj.yv = 0
        if right_dif in smallest:
            print("right bound")
            mov_obj.x += 2
            mov_obj.xv = stati_obj.xv
        # mov_obj.yv = 0
        elif left_def in smallest:
            print("left bound")
            mov_obj.x += -2
            mov_obj.xv += stati_obj.xv
        # mov_obj.yv = 0

        return jumpable
