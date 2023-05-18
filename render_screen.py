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
                pygame.draw.rect(window, (0, 0, 0), (x, y, self.cell_size, self.cell_size), 1)
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
        self.red_coords=red_coords
        

    #it has to be the same number of blue dots and red dots
    def neighboar_checking(self):
        #this is still good
        for b_dot, r_dot in zip(self.blue_dots, self.red_dots):
            coords = self.coord_detection(b_dot)
            coords.remove(coords[4])
            b_dot.coords_arround.append(coords)
            
            coords2 = self.coord_detection(r_dot)
            coords2.remove(coords2[4])
            r_dot.coords_arround.append(coords)
            
            
            
            for b_coord, r_coord in zip(coords, coords2):
                
                for blue_dot,red_dot in zip(self.blue_dots,self.red_dots):

                    if blue_dot.x == b_coord[0] and blue_dot.y == b_coord[1]:
                        b_dot.same_neigbor.append(blue_dot)
                    
                    if red_dot.x == b_coord[0] and red_dot.y == b_coord[1]:
                        b_dot.different_neighbors.append(red_dot)


                    if red_dot.x == r_coord[0] and red_dot.y == r_coord[1]:
                        r_dot.same_neigbor.append(red_dot)
                    
                    if blue_dot.x == r_coord[0] and blue_dot.y == r_coord[1]:
                        r_dot.different_neighbors.append(blue_dot)
                        

                
                    
    def coord_detection(self,dot):
        
        #this is the simples and effective function of all
        display_coords=[]
        for i in range(3):                 
            x = dot.x - 10
            y = dot.y - 10 + 10*i
            for j in range(3):
                display_coords.append([x, y])
                x += 10
        
            
        return display_coords
    
    
    def new_gen(self):
        #OKAY, THIS IS PROGRESS, MAYBE IS KINDA SPAGHETTI BUT IT WORKS (later, just have to see how to take aout the main dot)
        #Here's the principal issue, the way of seein the new generation
        #I have to do the flowchart to make the new generation
        for blue_dot in self.blue_dots:
            
            if len(blue_dot.same_neigbor)==3:
                first_arround=blue_dot.coords_arround[0]
                second_arround=None
                third_arround=None
                
                for neighboars in  blue_dot.same_neigbor:
                    for neighboar_coords in neighboars.coords_arround:
                        if neighboar_coords not in first_arround:
                            second_arround=neighboar_coords
                        if neighboar_coords not in first_arround and neighboar_coords not in second_arround:
                            third_arround=neighboar_coords
                            
                intersection = [value for value in first_arround if value in second_arround and value in third_arround and value not in self.blue_coords]
                
                return intersection[1]
            
                            
                            
                            
#main place
grid= MiniGrid(10, 1920/16, 1080/8)
window=pygame.display.set_mode((1920,1080))
background=pygame.draw.rect(window,(255,255,255),(0,0,1920,1080),0)
running=True
button1=button(350,825,50,0,0,0)

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
        
        #toda esta parte esta bastante bien de hecho
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if grid.clicked_death_point(mouse_pos):
                keys=pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    
                    punto_blue = bluedot(mouse_pos, mouse_pos, 0, 0, 255, 4, True , [],[], [])
                    point_blue=punto_blue.center_snap(grid.clicked_death_point(mouse_pos)[1:])

                    
                    if point_blue not in blue_coords:
                        blue_coords.append(point_blue)
                        blue_dot.append(punto_blue)
                        punto_blue.draw(window)
                    else:
                        print('not valid')
                 
                        
                if keys[pygame.K_k]:
                    
                    punto_red = reddot(mouse_pos, mouse_pos, 255, 0, 0, 4,True ,[],[], [])
                    point_red=punto_red.center_snap(grid.clicked_death_point(mouse_pos)[1:])
                          
                    if point_red not in red_coords:
                        red_coords.append(point_red)
                        red_dot.append(punto_red)
                        punto_red.draw(window)
                    else:
                        print('not valid')
            #hasta aca tambien sigue bastante bien


            if button1.clicked(mouse_pos):
                print('clicked' )
                #como siempre, esto da problema
                game=game_of_life(blue_dot,red_dot,blue_coords,red_coords)
                while True:   
                    #tambien ando con el problema aca
                    
                    for b_dot, r_dot in zip(game.blue_dots, game.red_dots):#THIS FUCKING FOR LOOP DUDE, WTF
                        game.neighboar_checking()
                        b_dot.state
                        r_dot.state
                        
                        print(game.new_gen())
                        if game.new_gen() != None:
                            
                            new_dot=bluedot(game.new_gen()[0],game.new_gen()[1],0,0,255,4,True,[],[],[])
                            new_dot.draw(window)
                            game.blue_dots.append(new_dot)
                                
                        else:
                            
                            pass
                        
                        
                        
                        if b_dot.state == True:
                            pass
                            
                        else:
                            b_dot.remove(window)
                            print('dead')
                                
                        if r_dot.state == True:
                            pass
                            
                        else:
                            r_dot.remove(window)
                            print('dead')
                            
                        pygame.display.update()
                
                    
            
    MiniGrid.draw(grid, window)
    pygame.display.update()

