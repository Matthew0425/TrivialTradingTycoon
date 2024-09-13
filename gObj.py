import pygame

class gameObj:
    def __init__(self, x, y, path):
        self.x = x
        self.y = y
        self.path = path
        self.sprite = pygame.image.load(self.path)
        self.rect = self.sprite.get_rect()
        self.width = self.rect.w
        self.length = self.rect.h
    def loadImage(self, path):
        self.sprite = pygame.image.load(path)
        self.rect = self.sprite.get_rect()
    def draw(self, sc):
        sc.blit(self.sprite, (self.x, self.y))
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_w(self):
        return self.width
    def get_h(self):
        return self.length
    def set_x(self, a):
        self.x = a
    def set_y(self, a):
        self.y = a
    def set_w(self, a):
        self.width = a
    def set_h(self, a):
        self.length = a
