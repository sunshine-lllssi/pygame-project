import pygame
from pygame.sprite import Sprite


class Gun(Sprite):

    def __init__(self, screen):
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0 (3).png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mr = False
        self.ml = False
        self.move_w = False
        self.move_s = False

    def output(self): # рисование пушки
        self.screen.blit(self.image, self.rect)

    def update_gun(self): # позиции пушки
        if self.mr:
            self.center += 1.5
        if self.ml:
            self.center -= 1.5
        elif self.move_w:
            self.center -= 1.5
        elif self.move_s:
            self.center += 1.5

        self.rect.centerx = self.center

    def create_gun(self): # размещение пушки
        self.center = self.screen_rect.centerx