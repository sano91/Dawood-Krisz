from playsound import playsound
import os
fileDir = os.path.dirname(os.path.abspath(__file__))

# Colors          ##############################################################x

bold = '\033[1m'
whitebgblack = '\033[7m'
default = '\033[0m'
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
white = '\033[37m'

bgblack = '\033[40m'
bgred = '\033[41m'
bggreen = '\033[42m'
bgyellow = '\033[43m'
bgblue = '\033[44m'
bgpurple = '\033[45m'
bgcyan = '\033[46m'
bgwhite = '\033[47m'
nderline = '\033[2m'
######################################################################x
   
        
def menu():
    
    introname = "BATTLESHIP\n"
    CENTERINTRONAME = introname.center(80)
    print(CENTERINTRONAME)                                    # Main menu
    initial = int(input('''

    1. New Game
    2. Load Game
    3. Guide
    4. Game Setup
    5. Credits
    6. Exit 
    :'''))
    #back_to_menu = ""
    return initial
def submenu(initial):
    exit = None                           # Sub Menu
    if initial == 1:
        game_status = "new game"
    elif initial == 2:
        game_status = "load game"
    elif initial == 3:
        guide = int(input('''
        Torpedo
        The game start with adding the players name, and rightafter, the game start.
        The gamefield is 4x4 big, and a ship is already randomly set.
        You can guess by type the row, and after the column.
        The game is so simple but fun to play with it with bet with your friend.
        press 88 to Menu: ''' ))
    elif initial == 4:                              # Setups Menu
        game_setup = int(input('''
        1. Music 
        2. Color Theme
        3. Single Player Mode
        4. Difficulity
        
        : '''))
    elif initial == 5:
        credits = int(input('''
        Torpedo
        Written by Ghammud Dawood and Krisztián Szőllösy
        Co work Sano
        All right reserved
        Press 1 to Menu
        : '''))
    elif initial == 6:
        exit = "fuck"
        print("No way man!")
    return game_setup
        
def game_settings_main(game_setup):
                          # Main game Settings/Setup!!
    if game_setup == 1:
        music_setup = int(input('''
        1. Lounge music
        2. Caffe music
        3. Chill out                                         
        4. Jazz music
        
        : '''))
        return music_setup
    elif game_setup == 2:
        color_setup = int(input('''
        1. Solid
        2. Matt theme
        3. Default
        4. Back to menu
        : '''))
        return color_setup
    elif game_setup == 3:
        player_mode = int(input('''
        1. Single Player Mode
        2. Two Players mode
        
        : '''))
        return player_mode
    elif game_setup == 4:
        difficulity_setup = int(input('''
        1. Easy
        2. Medium
        3. Hard
        
        : '''))
        return difficulity_setup
    elif game_setup == 5:
        back_to_menu = "menu"
    
def game_settings_music(game_setup):

    back_to_menu = False
    music_setup = int(input('''
    1 Lounge music
    2 Caffe music
    3 Chill music
    4 Jazz music
    : '''))                           # Choose music
    
    return music_setup
def set_color(color_setup):
    coloring = int(input('''
    1 Solid
    2 Matt theme
    3 Default
    : '''))
    return coloring
def set_playerMode(player_mode):
    back_to_menu = False                  # single or two player setup
    game_mode = int(input('''
    1 Single player
    2 Two player
    : '''))
    return game_mode
def set_difficulity(difficulity_setup):
    level = int(input('''
    1 easy
    2 medium
    3 hard
    : '''))
    return level
def main(back_to_menu=None):
    if back_to_menu == "menu":
        
        initial = menu()
        secini = submenu(initial)
        if secini == 4:
            trecini = game_settings_main(4)
            
            if trecini == 1:
                quatrocini = game_settings_music(trecini)
                if quatrocini == 1:
                    print("Lounge.mp3")
                elif quatrocini == 2:
                    print("Caffe.mp3")
                elif quatrocini == 3:
                    print("chill.mp3")    
                elif quatrocini == 4:
                    print("Jazz.mp3")
            elif trecini == 2:
                seicini = set_color(trecini)
                if secini == 1:
                    print("Solid")
                elif secini == 2:
                    print("Matt theme")
                elif secini == 3:
                    print("default")
            elif trecini == 3:
                settecini = set_playerMode(trecini)
                if settecini == 1:
                    print("Single player")
                elif settecini == 2:
                    print("Two players")
            elif trecini == 4:
                ottocini = set_difficulity(trecini)
                if ottocini == 1:
                    print("easy")
                elif ottocini == 2:
                    print("medium")
                elif ottocini == 3:
                    print("hard")



        elif initial == 5:
            submenu(initial)
        elif initial == 6:
            submenu(initial)

main(back_to_menu="menu")        



            
        




