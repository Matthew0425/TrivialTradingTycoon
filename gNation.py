import gClickable

class nation(gClickable.clickableObj):
    def __init__(self, x, y, path):
        super().__init__(x, y, path)
        pygame.font.init()
        self.keys = ["FOOD", "RAW_MATS", "ENERGY"]
        self.resources = {"FOOD": 20,
                          "RAW_MATS": 20,
                          "ENERGY": 20}
        self.f = pygame.font.SysFont("timesnewroman", 30)
        self.menu = []
    def onClick(self):
        if self.get_clicked():
            print("not done yet")
            self.showMenu()
