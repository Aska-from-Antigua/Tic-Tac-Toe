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

import pygame, sys, time, Values_for_Tic_Tac_Toe
from pygame.locals import *
from Values_for_Tic_Tac_Toe import *

############################## #Assist With Readability of Code
height = SCR_WIDTH - SCR_WIDTH % 3 #height of screen                    
width = SCR_HEIGHT - SCR_HEIGHT % 3 #width of screen
third_height = height//3
third_width = width//3
sixth_height = height//6
sixth_width = width//6
############################## 

############################## #Initialises Game Screen
pygame.init()
pygame.display.set_caption('Tic Tac Toe')
DISPLAYSURF = pygame.display.set_mode((width, height))
DISPLAYSURF.fill(BG_COLOR)
##############################    

        
f=pygame.font.SysFont(END_SCREEN_FONT, min(third_width,third_height))

list_of_sectors = []

a, b, c = [0,3,6,0,1,2,0,2],[1,4,7,3,4,5,4,4],[2,5,8,6,7,8,8,6]
#Stores the different combinations for winning a game in tic tac toe.
#In order to win, three sectors in either the same row, column, diagonal
#or reverse diagonal must be of the same type. Also at least one must be
#set to avoid any issues as sectors all begin with the same type "None"
#The list above store the indexes for combinations for 3 rows, 3 columns,
#one diagonal and one reverse diagonal (8 in total). Variable **a**
#stores the index of the first sector in the combination. **b** stores
#the index of the second and **c** stores the third.

class Sector:
    """Object for Sectors

    The screen will be divided into 9 objects, called sectors.
    Each sector will represent a block which can depict a states
    of "X", "O" or  by default "None". The sector object will be
    assigned to a state when clicked and will keep this state until
    either player has won the game or a tie has occured. After this,
    each sector will be reset to their default states for a new game
    to begin.
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
        if "X" clicked it and to "O" if "O" clicked
        it
        """
        if not self.state:
            self.state = True
            self.type = player
    def display_self(self):
        if self.type == "O":
            pygame.draw.circle(DISPLAYSURF, O_COLOR, (self.mid_x, self.mid_y), self.radius, self.width)
        if self.type == "X":
            pygame.draw.line(DISPLAYSURF, X_COLOR, (self.pos_x, self.pos_y), (self.pos_x + self.len_x, self.pos_y + self.len_y), self.width)
            pygame.draw.line(DISPLAYSURF, X_COLOR, (self.pos_x + self.len_x, self.pos_y), (self.pos_x, self.pos_y + self.len_y), self.width)

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
    "X", the new player will be "O" and vice versa.
    """
    if player == "O":
        return "X"
    if player == "X":
        return "O"

def draw_grid():
    """Draw Grid

    Draws four lines representative of the Tic Tac Toe
    Grid
    """
    pygame.draw.line(DISPLAYSURF, GRD_COLOR, (third_width, 0), (third_width, height), width//45)
    pygame.draw.line(DISPLAYSURF, GRD_COLOR, (2*third_width, 0), (2*third_width, height), width//45)
    pygame.draw.line(DISPLAYSURF, GRD_COLOR, (0, third_height), (width, third_height), height//45)
    pygame.draw.line(DISPLAYSURF, GRD_COLOR, (0, 2*third_height), (width, 2*third_height), height//45)

def draw_strike(win_sector_1_pos, win_sector_3_pos):
    FPS = 60
    fpsClock = pygame.time.Clock()
    
    strike_vect_x = int((win_sector_3_pos.mid_x - win_sector_1_pos.mid_x)/99)
    strike_vect_y = int((win_sector_3_pos.mid_y - win_sector_1_pos.mid_y)/99)
    strike_pos_x = win_sector_1_pos.mid_x - strike_vect_x * 27
    strike_pos_y = win_sector_1_pos.mid_y - strike_vect_y * 27
    a = win_sector_1_pos
    c = win_sector_3_pos
    
    while True:
        pygame.draw.circle(DISPLAYSURF, STRIKE_COLOR, (strike_pos_x, strike_pos_y), width//30)
        strike_pos_x += strike_vect_x
        strike_pos_y += strike_vect_y
        fpsClock.tick(FPS)
        pygame.display.update()
        if (strike_pos_x > width or strike_pos_x < 0):
            break
        if strike_pos_y > height or strike_pos_y < 0:
            break
    time.sleep(0.25)

def game_over(x, text):    
    if not text == "Draw!!":
        draw_strike(list_of_sectors[a[x]],list_of_sectors[c[x]])
        pygame.display.update()
    
    DISPLAYSURF.fill(END_SCREEN_BG_COLOR)
    END_GAME_SCREEN = pygame.font.Font.render(f, text, False, END_SCREEN_TEXT_COLOR)
    DISPLAYSURF.blit(END_GAME_SCREEN,(text_display_pos_x,text_display_pos_y))
    pygame.display.update()
    
    time.sleep(END_GAME_WAIT_TIME)
    DISPLAYSURF.fill(BG_COLOR)
    draw_grid()
    
    for x in range(9): #Resets sectors to default states
        list_of_sectors[x].state = False
        list_of_sectors[x].type = "None"

    return "X"

for x in range(9): #initialises sectors
    list_of_sectors.append(Sector(x))

player = "X"

draw_grid()

end_of_game = False

########################################################################################################################
########################################################################################################################

while True: #main game loops
    for x in range(9): #checks if each sector is activated
        if not list_of_sectors[x].type == "None":
            end_of_game = True
            text = "Draw!!"
            text_display_pos_x = sixth_width
            text_display_pos_y = third_height
            continue
        end_of_game = False #if one sector is empty then it breaks out of the loop
        break
    
    for x in range(8): #loops through all 8 predefined winning conditions to test if someone has won
        if list_of_sectors[a[x]].type == list_of_sectors[b[x]].type == list_of_sectors[c[x]].type and list_of_sectors[a[x]].state:
            end_of_game = True
            text = list_of_sectors[a[x]].type + " Wins!!" 
            text_display_pos_x = height // 40
            text_display_pos_y = third_height
            break
                            
    if end_of_game == True: #displays the results screen if the game has ended
        player = game_over(x, text)
            
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
