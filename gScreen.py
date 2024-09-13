import pygame

class gameScreen:
    def __init__(self, width, length):
        self.screen = pygame.display.set_mode((width, length))
        pygame.display.set_caption("DistSysPro")
        self.length = length
        self.width = width
        self.background = None
        self.updated = False
    def setBackground(self, r, g, b):
        self.background = (r, g, b)
        self.screen.fill(self.background)
    def drawBackground(self):
        self.screen.fill(self.background)
    def setTitle(self, t):
        pygame.display.set_caption("DistSysPro")
    def update(self):
        pygame.display.update()
    def quit(self):
        pygame.display.quit()
