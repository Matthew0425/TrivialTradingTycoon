import gObj
import pygame

class clickableObj(gObj.gameObj):
    def __init__(self, x, y, path):
        super().__init__(x, y, path)
        self.clicked = False
        self.lastcoords = (x, y)
        self.nowcoords = (x, y)
        self.timer = 1
        self.shift = False

    def get_clicked(self):
        return self.clicked

    def get_lastcoords(self):
        return self.lastcoords

    def get_nowcoords(self):
        return self.nowcoords

    def get_shift(self):
        return self.shift
    
    def get_timer(self):
        return self.timer

    def set_clicked(self, i):
        self.clicked = i

    def set_lastcoords(self, i):
        self.lastcoords = i

    def set_nowcoords(self, i):
        self.nowcoords = i

    def set_shift(self, i):
        self.shift = i
    
    def set_timer(self, i):
        self.timer = i

    def getMousePos(self):
        return pygame.mouse.get_pos()
    
    def isClicked(self):
        if pygame.mouse.get_pressed()[0]:
            print("good fstuff")
            if not self.shift:
                self.lastcoords = pygame.mouse.get_pos()
            if (self.get_x() < self.lastcoords[0] and self.get_x() + self.get_w() > self.lastcoords[0]
                and self.get_y() < self.lastcoords[1] and self.get_y() + self.get_h() > self.lastcoords[1]):
                    self.clicked = True
                    self.shift = True
                    #print("working")
        else:
            self.clicked = False

