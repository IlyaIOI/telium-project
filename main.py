#Telium – The game
import random

#Global variables
num_modules = 17    #The number of modules in the space station
module = 1          #The module of the space station we are in
last_module = 0     #The last module we were in
possible_moves = [] #List of the possible moves we can make
alive = True        #Whether the player is alive or dead
won = False         #Whether the player has won
power = 100         #The amount of power the space station has
fuel = 500          #The amount of fuel the player has in the
selection = 0
menu = 1
menu_selection = ""

#flamethrower
locked = 0          #The module that has been locked by the player
queen = 0           #Location of the queen alien
vent_shafts = []    #Location of the ventilation shaft entrances
info_panels = []    #Location of the information panels
workers = []        #Location of the worker aliens

#Procedure declarations

def load_module():    
    global module, possible_moves, power #Make the array with the possible places you can go & the position the player is in be accessable to all functions 
    power = power - 1
    if power == -1:
        alive = False
        print("The station has run out of power. Unable to sustain life support, you die.")
        exit()
    else:
        possible_moves = get_modules_from(module) #Get the output of the file containing the where you can go
        output_module() #Output which module you are in

def get_modules_from(module):
    global room, room_description
    moves = [] #Array containing spaces you can go to from current position
    text_file = open("Charles_Darwin/module" + str(module) + ".txt", "r") #Open the module you are currently in to find out which modules you can go to from the current position
    room = text_file.readline()
    room_description = text_file.readline()
    for counter in range(0,4): 
        move_read = text_file.readline() #For every line, read it and append it to the array
        if move_read != 0:
            moves.append(int(move_read))
    text_file.close()
    return moves

def output_module():
    global room_description, module
    print()
    print("-----------------------------------------------------------------")
    print()
    print("You are in module", str(module) + "\n\n\n" + room + "\n" + room_description)

def output_moves():
    global possible_moves
    print()
    print("From here you can move to modules:")
    for move in possible_moves:
        print('| ', move, end='') #For every item in the array of where you can go, output each module and a line to seperate them.
    print()

def get_action():
    global module, last_module, possible_moves, power
    valid_action = False #Keep looping and asking the user where they want to go until they type either MOVE or SCANNER
    while valid_action == False:
        print("What do you want to do next ? (MOVE, SCANNER)")
        action = input(">")
        if action.lower() == "move" or action.lower() == "m":
            move = int(input("Enter the module to move to: "))
            if move in possible_moves: #Check if it is between 1 and 17 (number of modules)
                valid_action = True #Stop looping the input
                last_module = module #Change the previous module variable
                module = move #Change current module variable
                print ("Development: Power - " +str(power))
                    
            else:
                print("The module must be connected to the current module.")
    
#Main program starts here

def gamemenu():
    global menu, menu_selection, selection
    while menu == 1:
        print ("Telium - The Game")
        print ("Please type PLAY to start the game, STORY to get the lore of the game or INSTRUCTIONS to find out how to play the game")
        menu_selection = input(str("> "))
        if menu_selection.lower() == "story" or menu_selection.lower() == "s":
            menu = 0
            selection = 2
            the_story()
        elif menu_selection.lower() == "instructions" or menu_selection.lower() == "instruction" or menu_selection.lower() == "i":
            menu = 0
            selection = 3
            instructions()
        elif menu_selection.lower() == "play" or menu_selection.lower() == "start" or menu_selection.lower() == "game" or menu_selection.lower() == "p":
            menu = 0
            selection = 1
            print("Development: Pre-game")
            game_play()
        else:
            print ("Invalid: Please type the item you want by typing the word in capitals.")

def game_play():
    global alive, won, selection
    while alive == True and won == False and selection == 1: #Start of game - Loops the program, asking the location you want to go to
        print ("Development:Game")
        load_module() #Loads the module that globalises variables & imports the data from the module.txt files
        if won == False and alive == True: #If the game is not complete, output where you can go and get the input of what the player wants to do
            output_moves()
            get_action()
        else:
            break

def the_story():
    global selection, menu
    print ("A remote probe on the surface of Mars has detected biological signatures of dormant, single celledc primitive life. A sample of the Martian soil is returned to the space station orbiting the Earth for further analysis.\nThe sample of the orange coloured cells are examined and DNA analysis shows remarkable similarities to Dictyostelium discoideum, a species of soil-living amoeba here on Earth. Commonly referred to as slime mould, it transitions from a collection of unicellular amoebae into a multicellular organism and then into a fruiting body within its lifetime. Nicknamed, “Telium” due to its colour and cellular structure, the sample is incubated in the lab aboard the space station in conditions similar to when Mars was a warmer, wetter planet in its ancient past.\nRemarkably, independent Telium cells start to slowly move and after a period of several days have joined together to form an organism resembling a slug. In further days the slug-like creature grows additional arms and begins to look like a large starfish. Each cell working with other cells to become a single organism. Intrigued, scientists continue to examine the creature that appears to be consuming bacteria from inside the incubation chamber, growing in size daily. Telium begins to show signs of advanced movement around the chamber and grows significantly in strength. Eventually becoming strong enough to break out of its chamber, suffocating the scientist examining it, the animal scuttles through the space station to an unknown location. The organism is not seen for several days, but tension between the astronauts escalates when the space station electronics begin to behave erratically, power starts draining and communication is lost with Earth. “We are on our own. Telium needs to be found and killed. There is no protocol for this and we cannot risk further loss of life. We must stick together and work it out”, the captain orders.\n\n\n")
    selection = 0
    menu = 1
    gamemenu ()

def instructions():
    global selection, menu
    print ("""\n\n\nThe space station has a limited amount of power which reduces on each turn. This provides a timer for the game. Telium – the queen alien, must be killed before the power runs out. The player is equipped with a flamethrower that requires fuel. This is used to kill aliens. The player also has a portable computer called ‘the scanner’, that has limited functionality to interact with the space station. On each turn, the player can use their scanner to lock the doors in a module. Locking the doors prevents aliens from moving to that module. Due to the station malfunction, only one module can be locked at a time. A player can move to an adjacent module. Each module could contain: \n• A ventilation shaft opening. In these modules the doors will lock on entry, forcing the player to move through the ventilation shaft. The dark passages lead to another random module. The player arrives in the new module and cannot return through the vent in the roof. \n• The queen alien (Telium). When the player enters the same module as Telium it attempts to escape via random adjacent modules. It can take 1-3 moves. If it arrives in a module with a ventilation shaft it will travel down the shaft arriving in a random module. If Telium is unable to move due to the only adjacent module being locked the player wins. \n• Worker aliens. Spawned asexually from the queen, the worker aliens gather bacteria for the queen to feed. They will attack the player if the player enters a module they are in. The player has the option to frighten the worker or attempt to kill it. This is done by using fuel from their flamethrower. The amount of fuel needed is not known by the player and will need to be deduced over several play attempts. The player will die if they do not frighten or kill the worker alien, losing the game. \n• An information panel. This costs power to use, but scans the space station and reveals the location of the queen. The remaining power in the station is also be shown by the panel.\n\n\n""")
    selection = 0
    menu = 1
    gamemenu()

if won == True:
    print("The queen is trapped and you burn it to death with your flamethrower.")
    print("Game over. You win!")

gamemenu()

