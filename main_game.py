import pygame
from pygame.locals import *
from dot_classes import reddot, bluedot, dot
from game_classes import MiniGrid, button, game_of_life  
from itertools import zip_longest
import time

grid= MiniGrid(10, 1920/16, 1080/8)
window=pygame.display.set_mode((1920,1080))
background=pygame.draw.rect(window,(255,255,255),(0,0,1920,1080),0)
button1=button(350,825,50,0,0,0)
running_main_loop=False

#I have to fix the zip function

blue_dot=[] 
blue_coords=[]
red_dot=[]
red_coords=[]

fill_value_dot=dot(0,0,150,150,150,0,True,[],[],[])
fill_value_coord=[0,0]

#main loop  
while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        mouse_pos = pygame.mouse.get_pos()
        button1.draw(window)
        
        if event.type == pygame.MOUSEBUTTONDOWN or running_main_loop==True:
            
            if grid.clicked_death_point(mouse_pos,window):
                keys=pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    
                    punto_blue = bluedot(mouse_pos, mouse_pos, 0, 0, 255, 4, True , [],[],[])
                    point_blue=punto_blue.center_snap(grid.clicked_death_point(mouse_pos,window)[1:])

                    
                    if point_blue not in blue_coords:
                        blue_coords.append(point_blue)# I'm really thinking if is really necessary to have an specif array for the coords, this was made in a pretty early stage
                        blue_dot.append(punto_blue)
                        punto_blue.draw(window)
                    else:
                        print('not valid')
                 
                #same shit        
                if keys[pygame.K_k]:
                    
                    punto_red = reddot(mouse_pos, mouse_pos, 255, 0, 0, 4,True ,[],[],[])
                    point_red=punto_red.center_snap(grid.clicked_death_point(mouse_pos,window)[1:])
                          
                    if point_red not in red_coords:
                        red_coords.append(point_red)
                        red_dot.append(punto_red)
                        punto_red.draw(window)
                    else:
                        print('not valid')



            if button1.clicked(mouse_pos) or running_main_loop==True:
                pygame.display.update()
                running_main_loop=True
                time.sleep(1.5)
                print('clicked' )
                game=game_of_life(blue_dot,red_dot,blue_coords,red_coords)

                game.neighboar_checking()
                
                
                
                

            
                new_gen_blue=[]
                new_gen_coords_blue=[]
                new_gen_red=[]
                new_gen_coords_red=[]
                
                erase_blue=[]
                erase_coords_blue=[]
                erase_red=[]
                erase_coords_red=[]
                

                for b_dot, r_dot in zip_longest(blue_dot, red_dot, fillvalue=fill_value_dot):
                    game=game_of_life(blue_dot,red_dot,blue_coords,red_coords)
                    #sola da problema para un patron, pero para el resto va bastate bien
                    
                    
                    intersection=game.inteserction_betwean_dots_blue(b_dot)     
                    intersection_r=game.inteserction_betwean_dots_red(r_dot)
                    
                    if None != intersection: 
                        for j in intersection:
                            new_dot_b=bluedot(j[0],j[1],0,0,255,4,True,[],[],[])
                            print(new_dot_b.x,new_dot_b.y)
                            if [new_dot_b.x, new_dot_b.y]in new_gen_coords_blue:
                                print('not valid')
                                del new_dot_b
                            else:
                                new_gen_blue.append(new_dot_b)
                                new_gen_coords_blue.append([new_dot_b.x,new_dot_b.y])
                                new_dot_b.draw(window)
                            
                    
                    if None != intersection_r:
                        for i in intersection_r:
                            new_dot_r=reddot(i[0],i[1],255,0,0,4,True,[],[],[])
                            if [new_dot_r.x, new_dot_r.y] in new_gen_coords_red:
                                del new_dot_r
                            else:

                                new_gen_red.append(new_dot_r)
                                new_gen_coords_red.append([new_dot_r.x,new_dot_r.y])
                                new_dot_r.draw(window)
                            

                    b_dot.point_state()
                    r_dot.point_state()
                
                print(new_gen_blue)
                                    
                for new_blue in new_gen_blue:
                    if new_blue in blue_dot:
                        pass
                    else:

                        blue_dot.append(new_blue)

                for new_b_coords in new_gen_coords_blue:
                    if new_b_coords in blue_coords:
                        pass
                    else:
                        blue_coords.append(new_b_coords)

                for new_red in new_gen_red:
                    if new_red in red_dot:
                        pass
                    else:
                        red_dot.append(new_red)

                for new_r_coords in new_gen_coords_red:
                    if new_r_coords in red_coords:
                        pass
                    else:
                        red_coords.append(new_r_coords)

                
                
                for b_dot, r_dot in zip_longest(blue_dot, red_dot, fillvalue=fill_value_dot):
                    if b_dot.state:
                        pass
                    else:
                        erase_blue.append(b_dot)
                        erase_coords_blue.append([b_dot.x,b_dot.y])
                        b_dot.remove(window)
                    
                    if r_dot.state:
                        pass
                    else:
                        erase_red.append(r_dot)
                        erase_coords_red.append([r_dot.x,r_dot.y])
                        r_dot.remove(window)
                
            
                
                



                for erase_b in erase_blue:
                    if erase_b in blue_dot:
                        blue_dot.remove(erase_b)

                for erase_b_coords in erase_coords_blue:
                    if erase_b_coords in blue_coords:
                        blue_coords.remove(erase_b_coords)

                for erase_r in erase_red:
                    if erase_r in red_dot:
                        red_dot.remove(erase_r)

                for erase_r_coords in erase_coords_red:
                    if erase_r_coords in red_coords:
                        red_coords.remove(erase_r_coords)


                
                for b_dot, r_dot in zip_longest(blue_dot, red_dot, fillvalue=fill_value_dot):
                    b_dot.coords_neigbor=[]
                    r_dot.coords_neigbor=[]
                    b_dot.same_neigbor=[]
                    r_dot.same_neigbor=[]
                
                print('finish')
                    
                    




                        

                    
    MiniGrid.draw(grid, window) 
    pygame.display.update()


