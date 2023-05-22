
import pygame
from pygame.locals import *
import time
import random

class Player():
    def __init__(self, bomb):
        self.__speed=5
        self.__direction=[0,0]
        self.__image = pygame.transform.scale(pygame.image.load('wall.png'), (30,30))
        self.__player_location = [40,40]
        self.__player_score = 0
        self.__player_remaining_lives = 3
        self.__bomb = bomb
        self.__did_i_place_bomb=False
        
    def __move(self,direction):
        
        self.__player_location[0]+=direction[0]*self.__speed
        self.__player_location[1]+=direction[1]*self.__speed

        
    
    def __place_bomb(self,location):
        self.__bomb._Bomb__bomb_location=location
        self.__bomb._Bomb__am_i_placed=True
  


    def __collect():
        pass

    def __enter_gate():
        pass

    def __update_score():
        pass

    def __player_die():
        pass

    def __draw_me():
        pass

    def __reduce_remaining_lives():
        pass
    
    def __is_player_hit_by_exp():
        pass

    def __is_player_hit_by_mons():
        pass


class Bomb:

    def __init__(self): 
        self.__image=pygame.transform.scale(pygame.image.load("bomb.png"),(10,10))
        self.__bomb_location=[0,0]
        self.__wating_duration=3
        self.__am_i_placed=False
        self.__explosion_image=pygame.transform.scale(pygame.image.load("explosion.png"),(40,40))
        
    
    def __trigger_explosion(self,x):
        x+=1
        if x==100000:
            x=0
            return True
        
    def __decide_locations(self, location):
        location_list = []
        for i in range(-2,3):
            location_list.append([location[0], location[1]+i*40])
            location_list.append([location[0]+i*40, location[1]])
        return location_list
    
    def __destroy(self, location):
        pass
        


        

   


class Monster():

    def __init__(self):
        self.__monster_speed=3
        self.__monster_remaining_lives=1
        self.__monster_list=[]
    
    def __kill():
        pass

    def __are_monsters_hit():
        pass

    def __monster_die():
        pass

    def __reduce_remaining_lives():
        pass




class Pawn(Monster):
    
    def __init__(self):
        super().__init__()
        self.__speed=1 ## inherit et
        self.__pawn_direction=[1,0]
        self.__pawn_image=pygame.transform.scale(pygame.image.load("pawn.png"),(30,30))
        self.__pawn_location = [250,250]

    def __pawn_move(self,direction):

        """n=random.randint(1,1000)
        if n==1:
            self.__change_pawn_direction(direction)
            self.__pawn_location[0]+=direction[0]*self.__speed
            self.__pawn_location[1]+=direction[1]*self.__speed
        else:"""
        self.__pawn_location[0]+=direction[0]*self.__speed
        self.__pawn_location[1]+=direction[1]*self.__speed
    
    def __change_pawn_direction(self,direction): #bunu da inherit etmek lazım
        
        if direction[0]==0:
            direction[1]=0
            direction[0]=random.choice([-1,1])
            
        else:
            direction[0]=0
            direction[1]=random.choice([-1,1])
      
            

        

class Boss(Monster):

    def __init__(self):
        super().__init__()
        self.__speed=2 #inherit et
        self.__boss_direction=[1,0]
        self.__boss_image=pygame.transform.scale(pygame.image.load("stop.png"),(30,30))
        self.__boss_location = [400,400]
        self.__monster_remaining_lives = 3

    def __boss_move(self,direction):
        self.__boss_location[0]+=direction[0]*self.__speed
        self.__boss_location[1]+=direction[1]*self.__speed

    def __change_boss_direction(self,direction): #bunu da inherit etmek lazım
        
        if direction[0]==0:
            direction[1]=0
            direction[0]=random.choice([-1,1])
            
        else:
            direction[0]=0
            direction[1]=random.choice([-1,1])

class Ghost(Monster):

    def __init__(self):
        super().__init__()
        self.__ghost_direction:list
        self.__ghost_image: str
        self.__ghost_location :list

    def __ghost_move():
        pass


class Stationary:

    def __init__(self):
        self.__names_of_stationary: list


class Collectible(Stationary):
    
    def __init__(self,location):
        super().__init__()
        self.__location_of_collectible=location
        self.__collectible_image=pygame.transform.scale(pygame.image.load("gold.png"),(30,30))

    def __is_there_a_collectible():
        pass

    def __delete_collectible():
        pass

        


class Wall(Stationary):

   

    def __init__(self, location): #?
        super().__init__() #?
        self.__location_of_wall=location #class attribute sakıncalı  mı, private nasıl yapacaz
        self.__wall_image=pygame.transform.scale(pygame.image.load('wall.png'), (40,40))

    
    def __is_there_a_wall():
        pass

    def __are_there_walls():
        pass

    
    


class Brick(Stationary):
    
    def __init__(self,location):
        super().__init__()
        self.__brick_location = location
        self.__brick_image = pygame.transform.scale(pygame.image.load('brick.png'), (40,40))

    
    def __delete_bricks(self, bricks, i):
        bricks.remove(bricks[i])

    def __are_bricks_hit():
        pass



class Gate(Stationary):

    def __init__(self,location):
        super().__init__()
        self.__gate_location = location
        self.__gate_image = pygame.transform.scale(pygame.image.load("gate.png"),(30,30))
    
    def __is_there_a_gate():
        pass



class Game(): #
    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Bomberman")

        #icon = pygame.image.load('spaceship (1).png')
        #pygame.display.set_icon(icon)

        self.__window_height = 600
        self.__window_width = 920
        self.__window_color = (102,102,255)

        self.__background1 = pygame.image.load('bg1.jpg') #yeni eklendi
        self.__background2 = pygame.image.load('bg2.jpg')
        self.__background3 = pygame.image.load('bg3.jpg')

        self.__starting_screen_attributes = [self.__window_width, self.__window_height, self.__window_color, self.__background1] # yeni eklendi
        self.__screen_attributes = [self.__window_width, self.__window_height, self.__window_color, self.__background2]
        self.__finishing_screen_attributes=[self.__window_width, self.__window_height, self.__window_color, self.__background3]

        self.__all_screen_attribues = [self.__starting_screen_attributes,self.__screen_attributes,self.__finishing_screen_attributes]
        self.__screen_number=0
        self.__show_screen(self.__all_screen_attribues[self.__screen_number])

        self.__start_time=pygame.time.get_ticks()
        self.__current_time=pygame.time.get_ticks()

        ####
        #self.__starting_screen = pygame.display.set_mode((self.__window_width, self.__window_width))
        #self.__finishing_screen =pygame.display.set_mode((self.__window_width, self.__window_width))


        ### new
        self.__wall_list=[]
        self.__bricks=[]
        self.__collectibles=[]

        bomb=Bomb()
        self.__player=Player(bomb)
        self.__ghost=Ghost()
        self.__pawn=Pawn()
        self.__boss=Boss() 
        
        

        
        ### new fonksiyon içine al...
        for i in range(23):
            for j in range(15):
                if i==0 or j==0 or i==22 or j==14 or (i%2==0 and j%2==0):
                    self.__wall_list.append(Wall([i*40,j*40]))


                    random_coor_x=[i*40-40,i*40+40,i*40]
                    random_coor_y=[j*40-40,j*40+40,j*40]

                    if i%2==0 and j%2==0 and i!=0 and j!=0 and i!=22 and j!=14:
                        random_number=random.randint(0,3)
                        random_x_number=random.randint(0,2)
                        random_y_number=random.randint(0,2)
                        for k in range(random_number):
                            if not random_x_number==random_y_number==2:
                                self.__bricks.append(Brick([random_coor_x[random_x_number],random_coor_y[random_y_number]]))
                        


        r=random.randint(0,len(self.__bricks)-1)
        self.__gate=Gate(self.__bricks[r]._Brick__brick_location)

        
        k=0
        while k<5:
            r_c=random.randint(0,len(self.__bricks)-1)
            if r_c!=r:
             
                self.__collectibles.append(Collectible(self.__bricks[r_c]._Brick__brick_location))
                k+=1



        random_x=40
        random_y=40
        for i in range(20):
            #random_x=random.randint(random_x,random_x+40+)

            pass

    

    def __run(self): #$$$$$$$$$$$$$$$$$$$$$4
        running = True
        while running:

           

            

            for event in pygame.event.get():
                pygame.key.set_repeat(100,25)
               
                if event.type == pygame.QUIT:
                    self.__end_game()
                    

                

                elif event.type == KEYDOWN:

                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        if self.__is_there_a_wall(self.__wall_list, self.__get_player_location(),[0,-1])==False:
                            self.__player._Player__direction=[0,-1]
                        else:
                            self.__player._Player__direction=[0,0]
                        
                    if event.key == K_DOWN:
                        if self.__is_there_a_wall(self.__wall_list, self.__get_player_location(),[0,1])==False:
                            self.__player._Player__direction=[0,1]
                        else:
                            self.__player._Player__direction=[0,0]

                    if event.key == K_RIGHT:
                        if self.__is_there_a_wall(self.__wall_list, self.__get_player_location(),[1,0])==False:
                            self.__player._Player__direction=[1,0]
                        else:
                            self.__player._Player__direction=[0,0]
                        
                        
                    if event.key == K_LEFT:
                        if self.__is_there_a_wall(self.__wall_list, self.__get_player_location(),[-1,0])==False:
                            self.__player._Player__direction=[-1,0]
                        else:
                            self.__player._Player__direction=[0,0]

                    if event.key == K_RETURN:
                            self.__screen_number=1
                            self.__show_screen(self.__all_screen_attribues[self.__screen_number])
                            


                    if event.key == K_SPACE:
                        self.__start_time = pygame.time.get_ticks()
                        self.__player._Player__place_bomb(self.__player._Player__player_location)
                        

                
                if self.__screen_number==1:
                    self.__player._Player__move(self.__player._Player__direction)




                ########################

            if self.__screen_number==1:

                self.__screen.fill(self.__window_color)

                    
                




                if self.__is_there_a_wall(self.__wall_list, self.__get_pawn_location(),self.__pawn._Pawn__pawn_direction)==False and self.__is_there_a_brick(self.__bricks, self.__get_pawn_location(),self.__pawn._Pawn__pawn_direction)==False:
                    self.__pawn._Pawn__pawn_move(self.__pawn._Pawn__pawn_direction)
                else:
                    self.__pawn._Pawn__change_pawn_direction(self.__pawn._Pawn__pawn_direction)
                    self.__pawn._Pawn__pawn_move(self.__pawn._Pawn__pawn_direction)


                if self.__is_there_a_wall(self.__wall_list, self.__get_boss_location(),self.__boss._Boss__boss_direction)==False and self.__is_there_a_brick(self.__bricks, self.__get_boss_location(),self.__boss._Boss__boss_direction)==False:
                    self.__boss._Boss__boss_move(self.__boss._Boss__boss_direction)
                else:
                    self.__boss._Boss__change_boss_direction(self.__boss._Boss__boss_direction)
                    self.__boss._Boss__boss_move(self.__boss._Boss__boss_direction)


                self.__draw(self.__screen, self.__gate._Gate__gate_image, self.__gate._Gate__gate_location)
                


                for i in range(len(self.__collectibles)):#
                    self.__draw(self.__screen, self.__collectibles[i]._Collectible__collectible_image , self.__collectibles[i]._Collectible__location_of_collectible)


                for i in range(len(self.__bricks)):#
                        self.__draw(self.__screen, self.__bricks[i]._Brick__brick_image , self.__bricks[i]._Brick__brick_location)

                for i in range(len(self.__wall_list)):#
                        self.__draw(self.__screen, self.__wall_list[i]._Wall__wall_image, self.__wall_list[i]._Wall__location_of_wall)
                


                #alttaki ikisi silinecek
                self.__draw(self.__screen, self.__gate._Gate__gate_image, self.__gate._Gate__gate_location)

                for i in range(len(self.__collectibles)):#
                    self.__draw(self.__screen, self.__collectibles[i]._Collectible__collectible_image , self.__collectibles[i]._Collectible__location_of_collectible)

                
                
       
                    
                        
                self.__draw(self.__screen, self.__player._Player__image,self.__player._Player__player_location)
                self.__draw(self.__screen, self.__pawn._Pawn__pawn_image,self.__pawn._Pawn__pawn_location)
                self.__draw(self.__screen, self.__boss._Boss__boss_image,self.__boss._Boss__boss_location)


                if self.__player._Player__bomb._Bomb__am_i_placed:
                    #print("q")
                    self.__draw(self.__screen, self.__player._Player__bomb._Bomb__image, self.__player._Player__bomb._Bomb__bomb_location)
                     #self.__player._Player__bomb._Bomb__bomb_location bunun gibi bomb location olmalı
                    #print(self.__player._Player__bomb._Bomb__bomb_location)
                    
                    
                
                if self.__player._Player__bomb._Bomb__am_i_placed:
                    self.__current_time = pygame.time.get_ticks()

                    if self.__current_time-self.__start_time>3000 and self.__current_time-self.__start_time<6000: # alttakileri tek fonksiyona at draw_explosion
                        location_list = self.__player._Player__bomb._Bomb__decide_locations(self.__player._Player__bomb._Bomb__bomb_location)
                        
                        for i in location_list:

                            self.__draw(self.__screen, self.__player._Player__bomb._Bomb__explosion_image, i)
                            
                            x, y = self.__is_there_a_brick(self.__bricks, i, [0,0])
                            if x == True:
                                self.__bricks[y]._Brick__delete_bricks(self.__bricks, y)



                    elif self.__current_time-self.__start_time>=6000:
                        self.__current_time=0
                        self.__player._Player__bomb._Bomb__am_i_placed=False

                    

                 
            pygame.display.update()

    
    def __draw(self,screen,image,location):
        screen.blit(image,(location[0],location[1]))

 
    def __end_game(self):
        pygame.quit()


    def __start_game(self):
        pass

    def __show_screen(self, screen_attributes): #yeni eklendi
            self.__screen=pygame.display.set_mode((screen_attributes[0], screen_attributes[1]))
            self.__screen.fill(screen_attributes[2])
            self.__screen.blit(screen_attributes[3],(0,0))

    def __is_there_a_collectible(self):
        pass

    def __is_there_a_wall(self, wall_list, player_location, new_direction):

        if new_direction==[1,0]:
            forbidden_ys=[n for n in range(player_location[1]-37, player_location[1]+27)]
            for i in range(len(wall_list)):
                if wall_list[i]._Wall__location_of_wall[1] in forbidden_ys:
                    for j in range(29):#speed
                        if player_location[0]+j==wall_list[i]._Wall__location_of_wall[0]:
                            return True       
            return False
        
        elif new_direction==[-1,0]:
            forbidden_ys=[n for n in range(player_location[1]-37, player_location[1]+27)]
            for i in range(len(wall_list)):
                if wall_list[i]._Wall__location_of_wall[1] in forbidden_ys:
                    for j in range(29):#speed
                        if player_location[0]-j==wall_list[i]._Wall__location_of_wall[0]:
                            return True       
            return False
        
        elif new_direction==[0,1]:
            forbidden_xs=[n for n in range(player_location[0]-37, player_location[0]+27)]
            for i in range(len(wall_list)):
                if wall_list[i]._Wall__location_of_wall[0] in forbidden_xs:
                    for j in range(29):
                        if player_location[1]+j==wall_list[i]._Wall__location_of_wall[1]:
                            return True       
            return False
        
        elif new_direction==[0,-1]:
            forbidden_xs=[n for n in range(player_location[0]-37, player_location[0]+27)]
            for i in range(len(wall_list)):
                if wall_list[i]._Wall__location_of_wall[0] in forbidden_xs:
                    for j in range(29):
                        if player_location[1]-j==wall_list[i]._Wall__location_of_wall[1]:
                            return True       
            return False

        return False


    def __is_there_a_brick(self, bricks, player_location, new_direction):

        if new_direction==[1,0]:
            forbidden_ys=[n for n in range(player_location[1]-37, player_location[1]+27)]
            for i in range(len(bricks)):
                if bricks[i]._Brick__brick_location[1] in forbidden_ys:
                    for j in range(29):#speed
                        if player_location[0]+j==bricks[i]._Brick__brick_location[0]:
                            return True       
            return False
        
        elif new_direction==[-1,0]:
            forbidden_ys=[n for n in range(player_location[1]-37, player_location[1]+27)]
            for i in range(len(bricks)):
                if bricks[i]._Brick__brick_location[1] in forbidden_ys:
                    for j in range(29):#speed
                        if player_location[0]-j==bricks[i]._Brick__brick_location[0]:
                            return True       
            return False
        
        elif new_direction==[0,1]:
            forbidden_xs=[n for n in range(player_location[0]-37, player_location[0]+27)]
            for i in range(len(bricks)):
                if bricks[i]._Brick__brick_location[0] in forbidden_xs:
                    for j in range(29):
                        if player_location[1]+j==bricks[i]._Brick__brick_location[1]:
                            return True       
            return False
        
        elif new_direction==[0,-1]:
            forbidden_xs=[n for n in range(player_location[0]-37, player_location[0]+27)]
            for i in range(len(bricks)):
                if bricks[i]._Brick__brick_location[0] in forbidden_xs:
                    for j in range(29):
                        if player_location[1]-j==bricks[i]._Brick__brick_location[1]:
                            return True       
            return False
        
        else:
            for i in range(len(bricks)):
                if bricks[i]._Brick__brick_location == player_location:
                    return True, i


        return False, None
            
            
                    
        
                    

    def __is_there_a_gate(self):
        pass
    
    def __are_there_walls(self):
        pass

    def __win_game(self):
        pass

    def __create_bomb(self):
        pass

    def __chechk_wall_list(self):
        pass

    def __are_bricks_hit(self):
        pass

    def __are_monsters_hit(self):
        pass

    def __is_player_hit_by_mons(self):
        pass

    def __get_player_location(self):
        return self.__player._Player__player_location
    
    def __get_pawn_location(self):
        return self.__pawn._Pawn__pawn_location
    
    def __get_boss_location(self):
        return self.__boss._Boss__boss_location
    
    def __get_bomb_image(self):
        return self.__player._Player__bomb._Bomb__bomb_image


game=Game()
game._Game__run()