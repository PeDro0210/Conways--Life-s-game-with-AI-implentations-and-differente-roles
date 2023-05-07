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
        return [self.x, self.y]

    def point_state(self, grid):
        if self.x and self.y not in grid:
            return True
        else:
            return False
    
    
    def coord_detection(self):

        display_coords=[]
        for i in range(3):
            x = self.x - 10
            y = self.y - 10 + 10*i
            for j in range(3):
                display_coords.append([x, y])
                x += 10

            
        return display_coords

    def limit_detector(self,grid):
        doot_coords = [self.x, self.y]
        if doot_coords not in grid.get_limits_coords():
            return True         
        else:
            return False
    #[[first_row_coords], [first_col_coords], [last_row_coords], [last_col_coords]]
    #first_row_coords= [[x,y],[x,y],[x,y],[x,y],[x,y],[x,y],[x,y],[x,y],[x,y],[x,y]] asi con todos, por eso va tan lento


class bluedot(dot):
    def __init__(self, x, y, R, G, B, radius):
        super().__init__(x, y, R, G, B, radius)

class reddot(dot):
    def __init__(self, x, y, R, G, B, radius):
        super().__init__(x, y, R, G, B, radius)