import pygame, sys
from bullet import Bullet
from ino import Ino
import time


def events(screen, gun, bullets): #обработка нажатий клавиш
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d: # смещение вправо
                gun.mr = True
            elif event.key == pygame.K_a: # смещение влево
                gun.ml = True
            elif event.key == pygame.K_w: # смещение влево
                gun.move_w = True
            elif event.key == pygame.K_s: # смещение вправо
                gun.move_s = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d: # смещение вправо
                gun.mr = False
            elif event.key == pygame.K_a: # смещение влево
                gun.ml = False
            elif event.key == pygame.K_w: # смещение влево
                gun.move_w = False
            elif event.key == pygame.K_s: # смещение вправо
                gun.move_s = False


def update(bg_color, screen, stats, sc, gun, inos, bullets): #обновление экрана
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, inos, bullets): # позиции пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():
            stats.score += 10 * len(inos)
        sc.image_score()
        sc.image_guns()
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)


def gun_kill(stats, screen, sc, gun, inos, bullets): #столкновение пушки и армии
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_inos(stats, screen, sc, gun, inos, bullets): # позицию свиней
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, sc,  gun, inos, bullets)
    inos_check(stats, screen, sc, gun, inos, bullets)


def inos_check(stats, screen, sc,gun, inos, bullets): # добралась ли армия до края экрана
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, inos, bullets)
            break


def create_army(screen, inos): # создание армии
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((900 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 100 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y - 1):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino)