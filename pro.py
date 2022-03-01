import pygame, control
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def start():
    pygame.init()
    screen = pygame.display.set_mode((900, 800))
    pygame.display.set_caption("Proswing")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    control.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        control.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            control.update(bg_color, screen, stats, sc, gun, inos, bullets)
            control.update_bullets(screen, stats, sc, inos, bullets)
            control.update_inos(stats, screen, sc, gun, inos, bullets)


start()
