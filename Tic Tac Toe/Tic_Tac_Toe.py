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
height = SCR_WIDTH#height of screen                    
width = SCR_HEIGHT #width of screen
diff_x = 0
diff_y = 0
third_height = height//3
third_width = width//3
sixth_height = height//6
sixth_width = width//6
eighteenth_height = height//18
eighteenth_width = width//18
############################## 

############################## #Initialises Game Screen
pygame.init()
pygame.display.set_caption('Tic Tac Toe')
tool_bar_height = 25
settings_pos = 9 * width // 10
tool_bar_color = WHITE
DISPLAYSURF = pygame.display.set_mode((width, height + tool_bar_height),pygame.RESIZABLE)
DISPLAYSURF.fill(BG_COLOR)
##############################    

f=pygame.font.SysFont(END_SCREEN_FONT, min(third_width,third_height))
f2=pygame.font.SysFont(END_SCREEN_FONT, min(eighteenth_width,eighteenth_height))
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
        self.pos_x = third_width * ((sector_pos) % 3) + diff_x // 2
        self.pos_y = third_height * ((sector_pos) // 3) + tool_bar_height + diff_y // 2
        self.len_x = third_width
        self.len_y = third_height
        self.mid_x = self.pos_x + sixth_width
        self.mid_y = self.pos_y + sixth_height
        self.radius = min(self.len_x,self.len_y) // 2
        self.width = min(width, height)//100
        self.state = False
        self.type = "None"
    def resize_self(self,sector_pos):        
        self.pos_x = third_width * ((sector_pos) % 3) + diff_x // 2
        self.pos_y = third_height * ((sector_pos) // 3) + tool_bar_height + diff_y // 2
        self.len_x = third_width
        self.len_y = third_height
        self.mid_x = self.pos_x + sixth_width
        self.mid_y = self.pos_y + sixth_height
        self.radius = min(self.len_x,self.len_y) // 2
        self.width = min(width, height)//100
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
##            pygame.draw.line(DISPLAYSURF, X_COLOR, (self.pos_x, self.pos_y), (self.pos_x + self.len_x, self.pos_y + self.len_y), self.width)
##            pygame.draw.line(DISPLAYSURF, X_COLOR, (self.pos_x + self.len_x, self.pos_y), (self.pos_x, self.pos_y + self.len_y), self.width)
            pygame.draw.line(DISPLAYSURF, X_COLOR, (self.mid_x - self.radius, self.pos_y), (self.mid_x + self.radius, self.pos_y + self.len_y), self.width)
            pygame.draw.line(DISPLAYSURF, X_COLOR, (self.mid_x + self.radius, self.pos_y), (self.mid_x - self.radius, self.pos_y + self.len_y), self.width)

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
    if (mouse_pos_y < tool_bar_height + diff_y // 2) and (mouse_pos_y < height + diff_y // 2):
        if (mouse_pos_x > settings_pos + diff_x // 2) and (mouse_pos_x < width + diff_x // 2):
            return -1
        else:
            return -2
    if mouse_pos_x < diff_x // 2 or mouse_pos_x > width + diff_x // 2:
        return -2
    if mouse_pos_y < diff_y // 2 or mouse_pos_y > width + diff_y // 2:
        return -2
    if (mouse_pos_x < third_width +  diff_x // 2) and (mouse_pos_x > diff_x // 2):
        sector_x = 0
    elif (mouse_pos_x < 2*third_width + diff_x // 2):
        sector_x = 1
    elif (mouse_pos_x < width + diff_x // 2):
        sector_x = 2
    else:
        return -2
        
    if (mouse_pos_y < third_height + tool_bar_height + diff_y // 2) and (mouse_pos_y > tool_bar_height + diff_y // 2):
        sector_y = 0
    elif (mouse_pos_y < 2*third_height + tool_bar_height + diff_y // 2):
        sector_y = 3
    elif (mouse_pos_y < height + tool_bar_height + diff_y // 2):
        sector_y = 6
    else:
        return -2
    
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

def draw_toolbar():    
    pygame.draw.rect(DISPLAYSURF, tool_bar_color, (diff_x // 2, diff_y // 2, width , tool_bar_height))
    pygame.draw.line(DISPLAYSURF, BLACK, (diff_x // 2, diff_y // 2), (width + diff_x // 2, diff_y // 2))
    pygame.draw.line(DISPLAYSURF, BLACK, (settings_pos + diff_x // 2, diff_y // 2) , (settings_pos + diff_x // 2, tool_bar_height + diff_y // 2))

highlight = []
def draw_settings_menu():
    for y in range(len(THEME_NAMES)):
        if not y in highlight:
            pygame.draw.rect(DISPLAYSURF, WHITE,(5 * sixth_width + diff_x // 2, tool_bar_height + eighteenth_height * y + diff_y // 2, sixth_width, eighteenth_height))
            SETTINGS_SCREEN = pygame.font.Font.render(f2, THEME_NAMES[y], False, RED)
        if y in highlight:
            pygame.draw.rect(DISPLAYSURF, BLUE,(5 * sixth_width + diff_x // 2, tool_bar_height + eighteenth_height * y + diff_y // 2, sixth_width, eighteenth_height)) 
            SETTINGS_SCREEN = pygame.font.Font.render(f2, THEME_NAMES[y], False, YELLOW)
        DISPLAYSURF.blit(SETTINGS_SCREEN,(5 * sixth_width + diff_x // 2, tool_bar_height + eighteenth_height * y + 5 + diff_y // 2))   
            
    
def draw_grid():
    """Draw Grid

    Draws four lines representative of the Tic Tac Toe
    Grid
    """
    draw_toolbar()
    pygame.draw.line(DISPLAYSURF, GRD_COLOR, (third_width + diff_x // 2, tool_bar_height + diff_y // 2), (third_width + diff_x // 2, height + tool_bar_height + diff_y // 2), width//45)
    pygame.draw.line(DISPLAYSURF, GRD_COLOR, (2*third_width + diff_x // 2, tool_bar_height + diff_y // 2), (2*third_width + diff_x // 2, height + tool_bar_height + diff_y // 2), width//45)
    pygame.draw.line(DISPLAYSURF, GRD_COLOR, (diff_x // 2, third_height + tool_bar_height + diff_y // 2), (width + diff_x // 2, third_height + tool_bar_height + diff_y // 2), height//45)
    pygame.draw.line(DISPLAYSURF, GRD_COLOR, (diff_x // 2, 2*third_height + tool_bar_height + diff_y // 2), (width + diff_x // 2, 2*third_height + tool_bar_height + diff_y // 2), height//45)

def draw_strike(win_sector_1_pos, win_sector_3_pos):
    FPS = 60
    fpsClock = pygame.time.Clock()
    sleep_time = .25
    strike_vect_x = int((win_sector_3_pos.mid_x - win_sector_1_pos.mid_x)/99)
    strike_vect_y = int((win_sector_3_pos.mid_y - win_sector_1_pos.mid_y)/99)
    strike_pos_x = win_sector_1_pos.mid_x - strike_vect_x * 27
    strike_pos_y = win_sector_1_pos.mid_y - strike_vect_y * 27
    a = win_sector_1_pos
    c = win_sector_3_pos
    
    while True:
        for event in pygame.event.get():
            if (event.type == MOUSEBUTTONDOWN) or (event.type == KEYDOWN):
                FPS = 500
                sleep_time = 0 
##            if event.type == VIDEORESIZE:
##                DISPLAYSURF, height, width, diff_x, diff_y = resize_screen(event)
        pygame.draw.circle(DISPLAYSURF, STRIKE_COLOR, (strike_pos_x, strike_pos_y), width//30)
        draw_toolbar()
        strike_pos_x += strike_vect_x
        strike_pos_y += strike_vect_y
        fpsClock.tick(FPS)
        pygame.display.update()
        if (strike_pos_x > width + diff_x // 2 or strike_pos_x < diff_x // 2):
            break
        if strike_pos_y > height + tool_bar_height + diff_y // 2 or strike_pos_y < diff_y // 2:
            break
    time.sleep(sleep_time)

def reset_board():
    for x in range(9): #Resets sectors to default states
        list_of_sectors[x].state = False
        list_of_sectors[x].type = "None"

    return "X"
    
def game_over(x, text): 
    if not text == "Draw!!":
        draw_strike(list_of_sectors[a[x]],list_of_sectors[c[x]])
        
    DISPLAYSURF.fill(FILL_COLOR)
    if not rainbow:
        DISPLAYSURF.fill(BG_COLOR, (diff_x // 2, diff_y // 2, width, height + tool_bar_height))
    if rainbow:
        y = len(rainbow_colors)
        for x in range(y):
            DISPLAYSURF.fill(rainbow_colors[x], (diff_x // 2 + width // y * x, diff_y // 2, width // y, height + tool_bar_height))
    draw_toolbar()
    END_GAME_SCREEN = pygame.font.Font.render(f, text, False, END_SCREEN_TEXT_COLOR)
    DISPLAYSURF.blit(END_GAME_SCREEN,(text_display_pos_x + diff_x // 2,text_display_pos_y + diff_y // 2))
    pygame.display.update()
    start = pygame.time.get_ticks()
    time_is_up = False
    while not time_is_up:
        for event in pygame.event.get():
            if (event.type == MOUSEBUTTONDOWN) or (event.type == KEYDOWN):
                time_is_up = True            
##            if event.type == VIDEORESIZE:
##                DISPLAYSURF, height, width, diff_x, diff_y = resize_screen(event)
        if pygame.time.get_ticks() - start >  END_GAME_WAIT_TIME*1000:
            time_is_up = True
    
    return reset_board()

def resize_screen(event):
    DISPLAYSURF = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
    height = min(event.h - tool_bar_height, event.w)
    width = min(event.h - tool_bar_height, event.w)
    diff_x = event.w - width
    diff_y = event.h - height - tool_bar_height
    return DISPLAYSURF, height, width, diff_x, diff_y 

def draw_screen():
    DISPLAYSURF.fill(FILL_COLOR)
    if not rainbow:
        DISPLAYSURF.fill(BG_COLOR, (diff_x // 2, diff_y // 2, width, height + tool_bar_height))
    if rainbow:
        y = len(rainbow_colors)
        for x in range(y):
            DISPLAYSURF.fill(rainbow_colors[x], (diff_x // 2 + width // y * x, diff_y // 2, width // y, height + tool_bar_height))
    for sector_i in list_of_sectors:        
        if sector_i.state == True:
            sector_i.display_self()
    draw_grid()
    draw_toolbar()
    if settings_menu == True:
        draw_settings_menu()
    pygame.display.update()
   

    
for x in range(9): #initialises sectors
    list_of_sectors.append(Sector(x))

player = "X"

draw_grid()

end_of_game = False
settings_menu = False
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
            text_display_pos_y = third_height + tool_bar_height
            break
                            
    if end_of_game == True: #displays the results screen if the game has ended
        player = game_over(x, text)        
        
    for event in pygame.event.get():
        if not settings_menu:
            if event.type == KEYDOWN:
                if event.key == 109:
                    BG_COLOR, GRD_COLOR, X_COLOR, O_COLOR, END_SCREEN_BG_COLOR, END_SCREEN_TEXT_COLOR, STRIKE_COLOR, FILL_COLOR = custom_theme()
                    draw_screen()
                if event.key >= 257 and event.key <= 265:
                    if event.key < 260:
                        sector_i = (event.key - 257) + 6
                    elif event.key > 262:
                        sector_i = (event.key - 257) - 6
                    else:
                        sector_i = (event.key - 257)
                    if not list_of_sectors[sector_i].state:
                        player = update_player(player)
                    list_of_sectors[sector_i].set_state(player)                        
        if event.type == MOUSEBUTTONDOWN:            
            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
            sector_i = check_sector(mouse_pos_x, mouse_pos_y)
            if sector_i == -1:
                settings_menu = not settings_menu
            if not settings_menu:
                if sector_i >= 0:
                    draw_screen()
                    if not list_of_sectors[sector_i].state:
                        player = update_player(player)
                    list_of_sectors[sector_i].set_state(player)
                    
        if settings_menu:            
            if event.type == MOUSEMOTION:
                highlight.clear()
                mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
                if mouse_pos_x > 5 * sixth_width + diff_x // 2 and mouse_pos_x < width + diff_x // 2:
                    for y in range(len(THEME_NAMES)):
                        if (mouse_pos_y > tool_bar_height + eighteenth_height * y + diff_y // 2) and (mouse_pos_y < tool_bar_height + eighteenth_height * (y + 1) + diff_y // 2):
                            highlight.append(y)
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
                if mouse_pos_x > 5 * sixth_width + diff_x // 2 and mouse_pos_x < width + diff_x // 2:
                    if mouse_pos_y > tool_bar_height + eighteenth_height * 6:
                        settings_menu = not settings_menu
                    for y in range(len(THEME_NAMES)):
                        if (mouse_pos_y > tool_bar_height + eighteenth_height * y + diff_y // 2) and (mouse_pos_y < tool_bar_height + eighteenth_height * (y + 1) + diff_y // 2):
                            try:
                                BG_COLOR, GRD_COLOR, X_COLOR, O_COLOR, END_SCREEN_BG_COLOR, END_SCREEN_TEXT_COLOR, STRIKE_COLOR, FILL_COLOR = update_theme(y)
                                rainbow = False
                            except ValueError:
                                rainbow = True
                                GRD_COLOR, X_COLOR, O_COLOR, END_SCREEN_TEXT_COLOR, STRIKE_COLOR = WHITE, BLACK, BLACK, BLACK, WHITE
                            settings_menu = False
                            break
                else:
                    settings_menu = not settings_menu                    
        
        if event.type == VIDEORESIZE:
            DISPLAYSURF, height, width, diff_x, diff_y = resize_screen(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    third_height = height//3
    third_width = width//3
    sixth_height = height//6
    sixth_width = width//6
    eighteenth_height = height//18
    eighteenth_width = width//18
    settings_pos = 9 * width // 10
    f=pygame.font.SysFont(END_SCREEN_FONT, min(third_width,third_height))
    f2=pygame.font.SysFont(END_SCREEN_FONT, min(eighteenth_width,eighteenth_height))
    for x in range(9):
        list_of_sectors[x].resize_self(x)
        
    draw_screen()        
