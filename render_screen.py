import pygame
from pygame.locals import *
from dot_classes import reddot, bluedot


#creating the grid in first place

class MiniGrid:
    def __init__(self, cell_size, width, height):
        self.rows = round(height/2)
        self.cols = round(width/2)
        self.cell_size = cell_size
        self.width = self.rows * cell_size
        self.height = self.cols * cell_size
        self.grid = self.create_grid()
        self.width = width
        self.height = height
        
        
    def create_grid(self):
        grid = []
        for i in range(self.rows):
            grid.append([])
            for _ in range(self.cols):
                grid[i].append(0)
                print(_)
        
        return grid
    
    def draw(self, window):
        important_coords = []
        for i in range(self.rows):
            for j in range(self.cols):
                x = i * self.cell_size + self.width * 5
                y = j * self.cell_size + self.height * 2
                pygame.draw.rect(window, (255, 255, 255), (x, y, self.cell_size, self.cell_size), 1)
                important_coords.append((x+5, y+5))
        return important_coords

    def clicked_death_point(self, pos):
        x, y = pos
        for cell_x, cell_y in self.draw(window):
            if cell_x - 5 <= x <= cell_x + 5 and cell_y - 5<= y <= cell_y + 5:
                return True, cell_x, cell_y
        return False




class button:
    def __init__(self,x,y,dim, R,G,B):
        self.x=x
        self.y=y
        self.dim=dim
        self.color=(R,G,B)
        
    def draw(self,window):
        pygame.draw.rect(window,(self.color),(self.x,self.y,self.dim,self.dim),0)
    
    def clicked(self,pos):
        x,y=pos
        if self.x<=x<=self.x+self.dim and self.y<=y<=self.y+self.dim:
            return True
        else:
            return False
    

    
grid= MiniGrid(10, 1920/16, 1080/8)
window=pygame.display.set_mode((1920,1080))
running=True
button1=button(350,825,50,255,255,255)

blue_dot=[]
blue_coords=[]
red_dot=[]
red_coords=[]


while running:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        mouse_pos = pygame.mouse.get_pos()
        button1.draw(window)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if grid.clicked_death_point(mouse_pos):
                keys=pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                        punto = bluedot(mouse_pos, mouse_pos, 0, 0, 255, 4)
                        point=punto.center_snap(grid.clicked_death_point(mouse_pos)[1:])
                        blue_coords.append(point)
                        blue_dot.append(punto)
                        punto.draw(window)
                        
                if keys[pygame.K_k]:
                    punto = reddot(mouse_pos, mouse_pos, 255, 0, 0, 4)
                    punto.center_snap(grid.clicked_death_point(mouse_pos)[1:])
                    red_coords.append(point)
                    red_dot.append(punto)
                    punto.draw(window)
                    
            if button1.clicked(mouse_pos):
                #keep checking the rules
                for i in blue_dot:
                    if i.point_state(blue_coords):
                        punto=bluedot(i.x+10, i.y+10, 0, 0, 255, 4)
                        print(punto.x, punto.y)
                        punto.draw(window)
                    

    
    MiniGrid.draw(grid, window)
    pygame.display.update()

