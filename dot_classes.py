import pygame

#main class
class dot:
    
    def __init__(self, x, y, R, G, B, radius):
        self.x = x
        self.y = y
        self.color = (R, G, B)
        self.radius = radius
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
    
    def center_snap(self, coords):
        self.x, self.y = coords 
        return self.x, self.y

