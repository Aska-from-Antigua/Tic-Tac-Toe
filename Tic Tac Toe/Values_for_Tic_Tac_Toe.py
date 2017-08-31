####################################
##
##Jerry Aska
##
##Values for Tic-Tac-Toe
##
####################################
# colours        R    G    B

WHITE          = (255, 255, 255)
BLACK          = (  0,   0,   0)
RED            = (255,   0,   0)
ORANGE         = (255, 125,   0)
GREEN          = (  0, 255,   0)
BLUE           = (  0,   0, 255)
YELLOW         = (255, 255,   0)
GOLD           = (255, 200,   0)
LIGHT_BLUE     = ( 75,  75, 255)
LIGHT_YELLOW   = (255, 255,  75)
GREY           = (125, 125, 125)
PURPLE         = (255,   0, 255)
DARK_GREEN     = (  0, 125,   0)
DARK_PURPLE    = (125,   0, 125)
LIGHT_PURPLE   = (255, 125, 255)
LILAC          = (255, 200, 255)

color_names = ["White", "Black", "Red", "Green", "Blue", "Yellow", "Gold", "Light Blue", "Light Yellow", "Grey", "Purple", "Dark Green", "Dark Purple", "Light Purple"]
color_value = [WHITE, BLACK, RED, GREEN, BLUE, YELLOW, GOLD, LIGHT_BLUE, LIGHT_YELLOW, GREY, PURPLE, DARK_GREEN, DARK_PURPLE, LIGHT_PURPLE]

THEME_NAMES = ["Shades", "Seafoam", "Present", "Light Elf", "Dark Elf", "Golden", "Indigo", "Default", "Rainbow"]
theme_value = [[BLACK, WHITE, YELLOW, GREY], [LIGHT_BLUE, LIGHT_YELLOW, GREEN, BLACK], [RED, YELLOW, BLUE, BLACK], [GREEN, WHITE, BLACK, GREY], [DARK_GREEN, DARK_PURPLE, BLACK, GREY], [GOLD, GREY, WHITE, BLACK], [PURPLE, DARK_PURPLE, LIGHT_PURPLE, LILAC], [BLACK, WHITE, YELLOW, BLACK], ["Rainbow", BLACK, BLACK, BLACK]]


rainbow_colors = [RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE]
rainbow = False

END_SCREEN_FONT = "comicsansmc"
SCR_HEIGHT = 500
SCR_WIDTH = 500
END_GAME_WAIT_TIME = 2

def set_color(color):
    if color in color_names:
        return color_value[color_names.index(color)]
    else:
        return None
    
def custom_theme():
    invalid_input = True
    while invalid_input:
        c = input("Enter Base Color: ")
        c1 = set_color(c)
        if not c1 == None:
            invalid_input = False
        if c1 == None:
            print("Color ",c," not identified", sep = "'")
    invalid_input = True
    while invalid_input:                
        c = input("Enter Secondary Color: ")
        c2 = set_color(c) 
        if not c2 == None:
            invalid_input = False
        if c2 == None:
            print("Color ",c," not identified", sep = "'")
    invalid_input = True
    while invalid_input:
        c = input("Enter Tertiary Color: ")
        c3 = set_color(c)
        if not c3 == None:
            invalid_input = False
        if c3 == None:
            print("Color ",c," not identified", sep = "'")
    return c1, c2, c2, c2, c1, c2, c3  

def update_theme(theme):
    if not THEME_NAMES[theme] == "Rainbow":
        c1, c2, c3, c4 = theme_value[theme]
        return c1, c2, c2, c2, c1, c2, c3, c4
    else:
        return theme_value[theme]


####################################### Default
BG_COLOR, GRD_COLOR, X_COLOR, O_COLOR, END_SCREEN_BG_COLOR, END_SCREEN_TEXT_COLOR, STRIKE_COLOR, FILL_COLOR = update_theme(0)
#######################################
