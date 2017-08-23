####################################
##
##Jerry Aska
##
##Tic-Tac-Toe
##
##    Coordinates in this program are written in terms of **height** and **width**, 
##      variables which store the height and width of the screen. This is done so that
##      The size of the screen can be adjusted by changing the values for **height**
##      and width in the code
##
####################################

import pygame, sys, time
from pygame.locals import *

# colour   R    G    B

WHITE  = (255, 255, 255)
BLACK  = (  0,   0,   0)

############################## #Assist With Readability of Code
height = 500 #height of screen                    
width = 500 #width of screen
third_height = height//3
third_width = width//3
sixth_height = height//6
sixth_width = width//6
############################## 

############################## #Initialises Game Screen
pygame.init()
pygame.display.set_caption('Tic Tac Toe')
DISPLAYSURF = pygame.display.set_mode((width, height))
DISPLAYSURF.fill(BLACK)
##############################

class Sector:
    """Object for Sectors

    The screen will be divided into 9 objects, called sectors.
    Each sector will represent a block which can depict a state
    of either an "X" or an "0". The sector object will be assigned
    to a state when clicked and will keep this state until either
    player has won the game. At this stage each sector will be
    destroyed and replaced with a new stateless sector.
    """
    def __init__(self,sector_pos):
        self.pos_x = third_width * ((sector_pos) % 3)
        self.pos_y = third_height * ((sector_pos) // 3)
        self.len_x = third_width
        self.len_y = third_height
        self.mid_x = self.pos_x + sixth_width
        self.mid_y = self.pos_y + sixth_height
        self.radius = min(self.len_x,self.len_y) // 2
        self.width = min(width, height)//100
        self.state = False
        self.type = "None"
    def set_state(self,player):
        """
        Sets sector state

        Sets sector state to True and type to be indicative
        of the player who clicked it. i.e. sets type to "X"
        if "X" clicked it and to "Circle" if "Circle" clicked
        it
        """
        if not self.state:
            self.state = True
            self.type = player
    def display_self(self):
        if self.type == "Circle":
            pygame.draw.circle(DISPLAYSURF, WHITE, (self.mid_x, self.mid_y), self.radius, self.width)
        if self.type == "X":
            pygame.draw.line(DISPLAYSURF, WHITE, (self.pos_x, self.pos_y), (self.pos_x + self.len_x, self.pos_y + self.len_y), self.width)
            pygame.draw.line(DISPLAYSURF, WHITE, (self.pos_x + self.len_x, self.pos_y), (self.pos_x, self.pos_y + self.len_y), self.width)

def check_sector(mouse_pos_x, mouse_pos_y):
    """Checks sector position of mouse

    Function checks the sector position of a cursor given
    its X and Y coordinate positions. It views the screen
    as split into 3 rows and 3 columns. It identifies the
    column of the mouse using the X coordinate as 0, 1 or
    2 and identifies the mouse row using the Y coordinate
    as 0, 3 or 6. It then returns the sum of these 2 values
    which is representative of the sector number.
    """
    if (mouse_pos_x < third_width):
        sector_x = 0
    elif (mouse_pos_x < 2*third_width):
        sector_x = 1
    else:
        sector_x = 2
        
    if (mouse_pos_y < third_height):
        sector_y = 0
    elif (mouse_pos_y < 2*third_height):
        sector_y = 3
    else:
        sector_y = 6

    return sector_x + sector_y 

def update_player(player):
    """Updates Player

    Checks the current player type and converts it to
    the opposite type, i.e. if the previous player was
    "X", the new player will be "Circle" and vice versa.
    """
    if player == "Circle":
        return "X"
    if player == "X":
        return "Circle"

def draw_grid():
    """Draw Grid

    Draws four lines representative of the Tic Tac Toe
    Grid
    """
    pygame.draw.line(DISPLAYSURF, WHITE, (third_width, 0), (third_width, height), width//45)
    pygame.draw.line(DISPLAYSURF, WHITE, (2*third_width, 0), (2*third_width, height), width//45)
    pygame.draw.line(DISPLAYSURF, WHITE, (0, third_height), (width, third_height), height//45)
    pygame.draw.line(DISPLAYSURF, WHITE, (0, 2*third_height), (width, 2*third_height), height//45)


list_of_sectors = [] 

for x in range(9): #initialises sectors
    list_of_sectors.append(Sector(x))

player = "X"

a, b, c = [0,3,6,0,1,2,0,2],[1,4,7,3,4,5,4,4],[2,5,8,6,7,8,8,6]
#Stores the different combinations for winning a game in tic tac toe.
#In order to win, three sectors in either the same row, column, diagonal
#or reverse diagonal must be of the same type. Also at least one must be
#set to avoid any issues as sectors all begin with the same type "None"
#The list above store the indexes for combinations for 3 rows, 3 columns,
#one diagonal and one reverse diagonal (8 in total). Variable **a**
#stores the index of the first sector in the combination. **b** stores
#the index of the second and **c** stores the third.

draw_grid()

f=pygame.font.SysFont("comicsansmc", min(sixth_width,sixth_height)) 

end_of_game = False

########################################################################################################################
########################################################################################################################

while True: #main game loops
    for x in range(9): #checks if each sector is activated
        if not list_of_sectors[x].type == "None":
            end_of_game = True
            text = "Draw" 
            continue
        end_of_game = False #if one sector is empty then it breaks out of the loop
        break
    
    for x in range(8): #loops through all 8 predefined winning conditions to test if someone has won
        if list_of_sectors[a[x]].type == list_of_sectors[b[x]].type == list_of_sectors[c[x]].type and list_of_sectors[a[x]].state:
            end_of_game = True
            text = list_of_sectors[a[x]].type+" Wins!!!"            
                            
    if end_of_game == True: #displays the results screen if the game has ended
        DISPLAYSURF.fill(BLACK)
        time.sleep(1)
        END_GAME_SCREEN = pygame.font.Font.render(f, text, False, WHITE)
        DISPLAYSURF.blit(END_GAME_SCREEN,(sixth_width,sixth_height))
        pygame.display.update()
        time.sleep(3)
        DISPLAYSURF.fill(BLACK)
        draw_grid()
        list_of_sectors = [] #deletes existing sectors
        for x in range(9):
            list_of_sectors.append(Sector(x)) #creates new sector
            
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:            
            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
            sector_i = check_sector(mouse_pos_x, mouse_pos_y)
            if not list_of_sectors[sector_i].state:
                player = update_player(player)
            list_of_sectors[sector_i].set_state(player)            
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    for sector_i in list_of_sectors:        
        if sector_i.state == True:
            sector_i.display_self()
            
    pygame.display.update()
