
import pygame
from pygame.locals import *
import time
import random

class Player():
    def __init__(self, bomb):
        self.__speed: int
        self.__direction:list
        self.__image: str
        self.__location :list
        self.__player_score: int
        self.__player_remaining_lives: int
        
    def __move():
        pass

    def __place_bomb():
        pass

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
        self.__bomb_image : str
        self.__bomb_location : list
        self.__wating_duration: int

    def __trigger_explosion():
        pass

    def __draw_bomb():
        pass

    def __explosion():
        pass


class Monster():

    def __init__(self):
        self.__monster_speed: int
        self.__monster_remaining_lives:int

    
    def __kill():
        pass

    def __are_monsters_hit():
        pass

    def __monster_die():
        pass

    def __draw_me():
        pass

    def __reduce_remaining_lives():
        pass




class Pawn(Monster):
    
    def __init__(self):
        super().__init__()
        self.__pawn_direction:list
        self.__pawn_image: str
        self.__pawn_location :list

    def __pawn_move():
        pass

class Boss(Monster):

    def __init__(self):
        super().__init__()
        self.__boss_direction:list
        self.__boss_image: str
        self.__boss_location :list
        self.__monster_remaining_lives:int

    def __boss_move():
        pass

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

    def __draw_stationaries(self,screen,image,x,y):
        screen.blit(image,(x,y))

 

class Collectible(Stationary):
    
    def __init__(self):
        super().__init__()
        self.__location_of_collectible:list
        self.__collectible_image: str

    def __is_there_a_collectible():
        pass

    def __delete_collectible():
        pass

        


class Wall(Stationary):
    
    def __init__(self, location,image): #?
        super().__init__() #?
        # new
        self.__location_of_wall=location
        self.__wall_image=image
    
    def __is_there_a_wall():
        pass

    def __are_there_walls():
        pass
    


class Brick(Stationary):
    
    def __init__(self):
        super().__init__()
        self.__brick_location:list
        self.__brick_image:str

    
    def __delete_bricks():
        pass

    def __are_bricks_hit():
        pass



class Gate(Stationary):

    def __init__(self):
        super().__init__()
        self.__gate_location : list
        self.__gate_image : str
    
    def __is_there_a_gate():
        pass



class Game():#
    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Bomberman")

        #icon = pygame.image.load('spaceship (1).png')
        #pygame.display.set_icon(icon)

        self.__window_height = 650
        self.__window_width = 920
        self.__window_color = (255,0,0)

        self.__background1 = pygame.image.load('bg1.jpg') #yeni eklendi
        self.__background2 = pygame.image.load('bg2.jpg')
        self.__background3 = pygame.image.load('bg3.jpg')

        self.__starting_screen_attributes = [self.__window_width, self.__window_height, self.__window_color, self.__background1] # yeni eklendi
        self.__screen_attributes = [self.__window_width, self.__window_height, self.__window_color, self.__background2]
        self.__finishing_screen_attributes=[self.__window_width, self.__window_height, self.__window_color, self.__background3]

        self.__all_screen_attribues = [self.__starting_screen_attributes,self.__screen_attributes,self.__finishing_screen_attributes]
        self.__screen_number=0
        self.__show_screen(self.__all_screen_attribues[self.__screen_number])

        ####
        #self.__starting_screen = pygame.display.set_mode((self.__window_width, self.__window_width))
        #self.__finishing_screen =pygame.display.set_mode((self.__window_width, self.__window_width))


        ### new
        self.__wall_list=[]


        a=1 #$$$$$$$$$44
        self.__player=Player(a)
        self.__ghost=Ghost()
        self.__ghost=Pawn()
        self.__ghost=Boss() 
        self.__collectible=Collectible() 
        self.__brick=Brick()
        self.__gate=Gate()

        
        ### new fonksiyon içine al...
        for i in range(21):
            for j in range(15):
                if i==0 or j==0 or i==20 or j==14:
                    self.__wall_list.append(Wall([i*40,j*40],pygame.transform.scale(self.__background1, (40, 40))))
        
        random_x=40
        random_y=40
        for i in range(20):
            #random_x=random.randint(random_x,random_x+40+)

            pass

    

    def __run(self): #$$$$$$$$$$$$$$$$$$$$$4
        running = True
        while running:

           

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__end_game()
                    


                elif event.type == KEYDOWN:

                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_DOWN:
                        pass

                    if event.key == K_RIGHT:
                        pass

                    if event.key == K_LEFT:
                        pass

                    if event.key == K_RETURN:
                            self.__screen_number=1
                            self.__show_screen(self.__all_screen_attribues[self.__screen_number])

                    for i in range(56):#??????????????????????
                            self.__wall_list[i]._Stationary__draw_stationaries(self.__screen, self.__wall_list[i]._Wall__wall_image, self.__wall_list[i]._Wall__location_of_wall[0], self.__wall_list[i]._Wall__location_of_wall[1])


                    """for i in range(57,66):#??????????????????????
                            self.__wall_list[i]._Stationary__draw_stationaries(self.__screen, self.__wall_list[i]._Wall__wall_image, self.__wall_list[i]._Wall__location_of_wall[0], self.__wall_list[i]._Wall__location_of_wall[1])
                            print("q")"""
            #end of game.run
            pygame.display.update()

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

    def __is_there_a_wall(self):
        pass

    def __is_there_a_gate(self):
        pass
    
    def __are_there_walls(self):
        pass

    def __win_game(self):
        pass

    def __create_bomb(self):
        pass

    def __chechk_boundaries(self):
        pass

    def __are_bricks_hit(self):
        pass

    def __are_monsters_hit(self):
        pass

    def __is_player_hit_by_mons(self):
        pass



game=Game()
game._Game__run()