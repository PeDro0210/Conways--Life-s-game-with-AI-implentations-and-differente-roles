import pygame
from itertools import zip_longest
from dot_classes import dot

fill_value_dot=dot(0,0,150,150,150,0,True,[],[],[])
fill_value_coord=[0,0]

class MiniGrid: #don't worry about the grid, this is the things that works the best
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

    def clicked_death_point(self, pos, window):
        x, y = pos
        for cell_x, cell_y in self.draw(window):
            if cell_x - 5 <= x <= cell_x + 5 and cell_y - 5<= y <= cell_y + 5:
                return True, cell_x, cell_y
        return False
  
    
class button: #also this, it works perfectly :D
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
        for b_dot, r_dot in zip_longest(self.blue_dots, self.red_dots, fillvalue=fill_value_dot):

            coords = self.coord_detection(b_dot)
            coords.remove(coords[4])
            b_dot.coords_arround.append(coords)

            coords2 = self.coord_detection(r_dot)
            coords2.remove(coords2[4])
            r_dot.coords_arround.append(coords2)

            dots_added = []

            for b_coord, r_coord in zip_longest(coords, coords2, fillvalue=fill_value_coord):

                for blue_dot, red_dot in zip_longest(self.blue_dots, self.red_dots, fillvalue=fill_value_dot):

                    if blue_dot not in b_dot.same_neigbor and blue_dot not in dots_added:
                        if blue_dot.x == b_coord[0] and blue_dot.y == b_coord[1]:
                            dots_added.append(blue_dot)
                            b_dot.same_neigbor.append(blue_dot)

                        if red_dot.x == b_coord[0] and red_dot.y == b_coord[1]:
                            dots_added.append(red_dot)
                            b_dot.different_neighbors.append(red_dot)

                    if red_dot not in r_dot.same_neigbor and red_dot not in dots_added:
                        if red_dot.x == r_coord[0] and red_dot.y == r_coord[1]:
                            dots_added.append(red_dot)
                            r_dot.same_neigbor.append(red_dot)

                        if blue_dot.x == r_coord[0] and blue_dot.y == r_coord[1]:
                            dots_added.append(blue_dot)
                            r_dot.different_neighbors.append(blue_dot)
    

            
                    
                


   

                
                    
    def coord_detection(self,dot):
        
        #this is so perfect really, I'm so proud of myself
        display_coords=[]
        for i in range(3):                 
            x = dot.x - 10
            y = dot.y - 10 + 10*i
            for j in range(3):
                display_coords.append([x, y])
                x += 10
        

            
        return display_coords
    
    def inteserction_betwean_dots_blue(self,blue_dot):# dunno what does this do (I did this in a crisis)
        # I need to see the how are the intersections working
        if len(blue_dot.same_neigbor)==2:
            first_arround=blue_dot.coords_arround[0]
            second_arround=[]
            third_arround=[]


            for counter,neighboars in enumerate(blue_dot.same_neigbor): #gracias juande, ahveces las cosas viejas
                for neighboar_coords in neighboars.coords_arround:
                    if counter <=0:
                        second_arround=neighboar_coords
                        break
                    if counter <=1:
                        third_arround=neighboar_coords
                        break
            
        
            intersection = [value for value in first_arround if value in second_arround and value in third_arround and value not in self.blue_coords]#see intersections for
            
            if len(intersection)!=0:
                return intersection
            else:
                
                return None
        
    def inteserction_betwean_dots_red(self,red_dot):#rewrite all of this for the red dots
        if len(red_dot.same_neigbor)==2:
            
            
            first_arround=red_dot.coords_arround[0]
            second_arround=None
            third_arround=None

            for counter,neighboars in enumerate(red_dot.same_neigbor): #gracias juande, ahveces las cosas viejas
                for neighboar_coords in neighboars.coords_arround:
                    if counter <=0:
                        second_arround=neighboar_coords
                        break
                    if counter <=1:
                        third_arround=neighboar_coords
                        break
            

            intersection = [value for value in first_arround if value in second_arround and value in third_arround and value not in self.red_coords]
            
            if len(intersection)!=0:
                return intersection
            else:
                return None