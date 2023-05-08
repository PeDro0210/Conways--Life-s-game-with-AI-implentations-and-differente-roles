import pygame
from pygame.locals import *
from dot_classes import reddot, bluedot
import random as rd 

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


    def get_limits_coords(self):
        limits = []
        rows= self.rows-8
        cols= self.cols+8

        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                    x = j * self.cell_size + self.width * 5 + 5
                    y = i * self.cell_size + self.height * 2 + 5
                    limits.append([x, y])

        return limits
 
        
    def create_grid(self):
        grid = []
        for i in range(self.rows):
            grid.append([])
            for _ in range(self.cols):
                grid[i].append(0)
        
        return grid
    
    def draw(self, window):
        important_coords = []
        for i in range(self.rows):
            for j in range(self.cols):
                x = i * self.cell_size + self.width * 5
                y = j * self.cell_size + self.height * 2
                pygame.draw.rect(window, (255, 255, 255), (x, y, self.cell_size, self.cell_size), 1)
                important_coords.append([x+5, y+5])
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
        
class game_of_life:
    def __init__(self,blue_dots,red_dots,blue_coords,red_coords):
        self.blue_dots=blue_dots
        self.red_dots=red_dots 
        self.blue_coords=blue_coords
        self.red_dots=red_coords
        
    
    def neighboar_checking(self,dot):
        neigboar_count=0
        coords=coord_detection(dot)
        
        for coord in coords:
            if coord in blue_coords:
                neigboar_count+=1
            if coord in red_coords:
                neigboar_count+=1

        
        return neigboar_count
    
    
        
        
        

def coord_detection(dot):
    
    
    display_coords=[]
    for i in range(3):
        x = dot.x - 10
        y = dot.y - 10 + 10*i
        for j in range(3):
            display_coords.append([x, y])
            x += 10
    
        
    return display_coords

        
    

    
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
                    
                    punto_blue = bluedot(mouse_pos, mouse_pos, 0, 0, 255, 4)
                    point_blue=punto_blue.center_snap(grid.clicked_death_point(mouse_pos)[1:])
                    
                    if point_blue not in blue_coords:
                        blue_coords.append(point_blue)
                        blue_dot.append(punto_blue)
                        punto_blue.draw(window)
                    else:
                        print('not valid')
                        
                if keys[pygame.K_k]:
                    
                    punto_red = reddot(mouse_pos, mouse_pos, 255, 0, 0, 4)
                    point_red=punto_red.center_snap(grid.clicked_death_point(mouse_pos)[1:])
                    
                    if point_red not in red_coords:
                        red_coords.append(point_red)
                        red_dot.append(punto_red)
                        punto_red.draw(window)
                    else:
                        print('not valid')


            if button1.clicked(mouse_pos):
                print('clicked' )
                game=game_of_life(blue_dot,red_dot,blue_coords,red_coords)

                
                for dot in blue_dot:
                    coords = coord_detection(dot)
                    
                    for coord in coords:
                        

                        # in here it will sort if the coord is in the list of blue coords
                        if coord not in blue_coords:
                            if dot.limit_detector(grid):
                                punto_azul = bluedot(coord[0], coord[1], 0, 225, 0, 4)
                                blue_coords.append(coord)
                                blue_dot.append(punto_azul)
                                punto_azul.draw(window)
                                pygame.display.flip()
                            else:
                                pass
                        else:
                            print('not valid')
                        


                        
                        
                            
                        
                
                
                    

    
    MiniGrid.draw(grid, window)
    pygame.display.update()

