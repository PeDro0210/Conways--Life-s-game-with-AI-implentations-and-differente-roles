                game=game_of_life(blue_dot,red_dot,blue_coords,red_coords)
                game.neighboar_checking() #dude, leave this here, it would start with the main loop    
                #I was just trying how did the state atributes worked, it worked pretty well


                new_gen_blue=[]
                new_gen_coords_blue=[]
                new_gen_red=[]
                new_gen_coords_red=[]

                for b_dot, r_dot in zip(game.blue_dots, game.red_dots):
                    
                    
                    
                    
                    intersection=game.inteserction_betwean_dots_blue(b_dot)     
                    intersection_r=game.inteserction_betwean_dots_red(r_dot)
                    
                    if None != intersection: 
                        for j in intersection:
                            new_dot_b=bluedot(j[0],j[1],0,0,255,4,True,[],[],[])
                            print(new_dot_b.x,new_dot_b.y)
                            new_gen_blue.append(new_dot_b)
                            new_gen_coords_blue.append([new_dot_b.x,new_dot_b.y])
                            draw=new_dot_b.draw(window)
                            
                    
                    if None != intersection_r:
                        for i in intersection_r:
                            new_dot_r=reddot(i[0],i[1],255,0,0,4,True,[],[],[])
                            print(new_dot_r.x,new_dot_r.y)
                            new_gen_red.append(new_dot_r)
                            new_gen_coords_red.append([new_dot_r.x,new_dot_r.y])
                            draw_2=new_dot_r.draw(window)

                    b_dot.point_state()
                    r_dot.point_state()
            

                    if b_dot.state:
                        pass
                    else:
                        if [b_dot.x,b_dot.y] in game.blue_coords:
                            game.blue_coords.remove([b_dot.x,b_dot.y])
                            b_dot.remove(window)
                        else:
                            pass
                        
                    
                    if r_dot.state:
                        pass
                    else:
                        if [r_dot.x,r_dot.y] in game.red_coords:
                            game.red_coords.remove([r_dot.x,r_dot.y])
                            r_dot.remove(window)
                        else:
                            pass

                for new_blue, new_b_coords in zip(new_gen_blue, new_gen_coords_blue):
                    game.blue_dots.append(new_blue)
                    game.blue_coords.append(new_b_coords)
                
                for new_red, new_r_coords in zip(new_gen_red, new_gen_coords_red):
                    game.red_dots.append(new_red)
                    game.red_coords.append(new_r_coords)