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

underline = '\033[2m'
#######################################################################x

    



                
def menu():                                     # Main menu
    initial = int(input('''Battleship

    1. New Game
    2. Load Game
    3. Guide
    4. Game Setup
    5. Credits
    6. Exit 
    :'''))
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
        5. Back to menu
        : '''))
    elif initial == 5:
        credits = int(input('''
        Torpedo
        Written by Ghammud Dawood and Krisztián Szőllösy
        Co work and design, Sano
        All right reserved
        Press 1 to Menu
        : '''))
    elif initial == 6:
        exit = "fuck"
        print("No way man!")
        
    return game_status, game_setup, guide, exit
def game_settings_main(gamesetup):
    back_to_menu = "menu"                        # Main game Settings/Setup!!
    if gamesetup == 1:
        music_setup = int(input('''
        1. Lounge music
        2. Caffe music
        3. Chill out                                         
        4. Jazz music
        9. Bact to Menu
        : '''))
    elif gamesetup == 2:
        color_setup = int(input('''
        1. Default
        2. Blue Power
        3. Light
        4. Back to menu
        : '''))
    elif gamesetup == 3:
        player_mode = int(input('''
        1. Single Player Mode
        2. Two Players mode
        3. Back to Menu
        : '''))
    elif gamesetup == 4:
        difficulity_setup = int(input('''
        1. Easy
        2. Medium
        3. Hard
        4. Back to Menu
        : '''))
    elif gamesetup == 5:
        back_to_menu = "menu"
    return music_setup, color_setup, player_mode, difficulity_setup, back_to_menu
def game_settings_music(music_setup):
    back_to_menu = False                           # Choose music
    if music_setup == 1:
        playsound(fileDir + "/Lounge.mp3")
    elif music_setup == 2:
        playsound(fileDir + "/caffee.mp3")
    elif music_setup == 3:
        playsound(fileDir + "/chill.mp3")
    elif music_setup == 4:
        playsound(fileDir + "/jazz.mp3")
    #elif music_setup == 5:
    #    playsound(fileDir + "/Imagination.mp3")
    #elif music_setup == 6:
    #    playsound(fileDir + "/Reverse_Skydiving.mp3")
    #elif music_setup == 7:
    #    playsound(fileDir + "/Night_Call.mp3")
    #elif music_setup == 8:
    #    playsound(fileDir + "/Sordid_affair.mp3")
    elif music_setup == 9:
        back_to_menu = "menu"
    return music_setup, back_to_menu
def set_color(color_setup):
    back_to_menu = False                      ### Choose Colors
    if color_setup == 1:
        coloring = default
    elif color_setup == 2:
        coloring  = red, bgblue
    elif color_setup == 3:
        coloring = black, bgwhite
    elif color_setup == 4:
        back_to_menu = True
    return coloring, back_to_menu
def set_playerMode(player_mode):
    back_to_menu = False                  # single or two player setup
    if player_mode == 1:
        game_mode = "single"
    elif player_mode == 2:
        game_mode = "multi"
    elif game_mode == 3:
        back_to_menu = True
    return game_mode, back_to_menu
def set_difficulity(difficulity_setup):
    back_to_menu = False
    if difficulity_setup == 1:
        level = 'easy'
    elif difficulity_setup == 2:
        level = 'medium'
    elif difficulity_setup == 3:
        level = 'hard'
    elif difficulity_setup == 4:
        back_to_menu = "menu"
    return level, back_to_menu

def main(back_to_menu=None):
    guide = 1
    if back_to_menu == "menu" or guide == 88:
        menu()
        submenu(initial)
        if initial == 4:
            game_settings_main(game_setup)
            if game_setup == 1:
                game_settings_music(music_setup)
            elif game_setup == 2:
                set_color(color_setup)
            elif game_setup == 3:
                set_playerMode(player_mode)
            elif game_setup == 4:
                set_difficulity(difficulity_setup)
main()





            
        




