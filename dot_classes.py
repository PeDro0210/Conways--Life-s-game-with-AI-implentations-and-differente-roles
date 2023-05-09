import pygame

#main class
class dot:
    
    def __init__(self, x, y, R, G, B, radius, state, neighbor=[], dif_neighbors=[], coords_around=[]):
        self.x = x
        self.y = y
        self.color = (R, G, B)
        self.radius = radius
        self.state = state
        self.same_neigbor = neighbor
        self.different_neighbors = dif_neighbors
        self.coords_arround = coords_around
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
    
    
    def center_snap(self, coords):
        self.x, self.y = coords 
        return [self.x, self.y]


    def coord_detection(self):

        display_coords=[]
        for i in range(3):
            x = self.x - 10
            y = self.y - 10 + 10*i
            for j in range(3):
                display_coords.append([x, y])
                x += 10

            
        return display_coords

    def point_state(self):
        if len(self.same_neigbor) >= 2 and len(self.same_neigbor) <= 3:
            self.state = True
        else:
            self.state = False
        

    
    def get_out(self,window):
        pygame.draw.circle(window, (255,255,255), (self.x, self.y), self.radius)
    



class bluedot(dot):
    def __init__(self, x, y, R, G, B, radius,state, neighbor, dif_neighbors, coords_around):
        super().__init__(x, y, R, G, B, radius,state, neighbor,dif_neighbors, coords_around)

class reddot(dot):
    def __init__(self, x, y, R, G, B, radius,state, neighbor, dif_neighbors, coords_around):
        super().__init__(x, y, R, G, B, radius,state, neighbor, dif_neighbors, coords_around)