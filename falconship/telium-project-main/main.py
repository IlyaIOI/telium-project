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
energy_cell = []    #Location of the energy cells
info_panels = []    #Location of the information panels
workers = []        #Location of the worker aliens

#Procedure declarations

def check_vent_shafts():
    global num_modules, module, vent_shafts, fuel
    if module in vent_shafts: #If you have selected the module with a vent shaft
        print("There is a bank of fuel cells here.") 
        print("You load one into your flamethrower.")
        gainedrandom = random.randint(0,3) #Select a random amount of fuel to give you
        if gainedrandom == 0:
            fuel_gained = 20
        elif gainedrandom == 1:
            fuel_gained = 30
        elif gainedrandom == 2:
            fuel_gained = 40
        elif gainedrandom == 3:
            fuel_gained = 50
        else:
            print ("An Error occured adding fuel")
        
        print("Fuel was",fuel,"now reading:",fuel+fuel_gained) #And output how much you have
        fuel = fuel + fuel_gained #add the fuel
        print("The doors suddenly lock shut.")
        print("What is happening to the station?")
        print("Our only escape is to climb into the ventilation shaft.")
        print("We have no idea where we are going.")
        print("We follow the passages and find ourselves sliding down.")
        last_module = module
        module = random.randint(1,num_modules)
        while module in vent_shafts:
            module = random.randint(1,num_modules)
        load_module()

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

def lock():
    global num_modules, power, locked
    new_lock = int(input("Enter module to lock:"))
    if new_lock<0 or new_lock>num_modules:
        print("Invalid module. Operation failed.")
    elif new_lock == queen:
        print("Operation failed. Unable to lock module.")
    else:
        locked = new_lock
    print("Aliens cannot get into module",locked)
    power_used = 25 + 5*random.randint(0,5)

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
    global room_description, module, queen, vent_shafts, info_panels, workers
    print()
    print("-----------------------------------------------------------------")
    print()
    print("You are in module", str(module) + "\n\n\n" + room + "\n" + room_description) #Print which module you are in, the room name and the description of the room
    if module == queen:
        print ("The queen is in this module")
    elif module in vent_shafts:
        print ("There is a vent shaft in this module")
    elif module in info_panels:
        print ("There is an info panel in this module")
    elif module in workers:
        print ("There is a worker alien in this room")
    check_vent_shafts()

def output_moves():
    global possible_moves
    print()
    print("From here you can move to modules:")
    for move in possible_moves:
        print('| ', move, end='') #For every item in the array of where you can go, output each module and a line to seperate them.
    print()

def spawn_npcs():
    global num_modules, queen, vent_shafts, info_panels, workers, energy_cell
    module_set = [] #array containing where each alien is (which module)
    for counter in range(2,num_modules): 
        module_set.append(counter) #for each module, have 14 modules in an array
    random.shuffle(module_set) #Shuffle the modules
    i = 0 
    queen = module_set[i] #The queen is in the first item in the array (0)
    for counter in range(0,3):
        i=i+1 #The vents are in the second to fourth item in the array (1,2,3)
        vent_shafts.append(module_set[i])
    for counter in range(0,2):
        i=i+1 #The info-panels are in the fifth to sixth item in the array (4,5)
        info_panels.append(module_set[i])
    for counter in range(0,3):
        i=i+1 #The worker aliens are in the seventh to ninth (6,7,8)
        workers.append(module_set[i])
    for counter in range (0,2):
        i=1+1
        energy_cell.append(module_set[i])

def lock():
    global num_modules, power, locked, possible_moves
    new_lock = input("Enter module to lock:")
    lock_split = split_next(new_lock)
    lock_split_length = len(lock_split)
    lock_split_length = lock_split_length - 1
    if lock_split[0].lower == "l":
        lock_split_length_down = int(lock_split_length-1)
        lock_split_last_number = lock_split[lock_split_length].isdigit()
        lock_split_second_last = lock_split[split_action_length_down].isdigit()
        if lock_split_last_number == True:
            if lock_split_second_last == True:
                lock_split_two_digits = lock_split[lock_split_length-1]+lock_split[lock_split_length]
            else:
                lock_split_two_digits = lock_split[lock_split_length]
            lock_module_number = int(lock_split_two_digits)
            if lock_module_number in possible_moves


    
    if new_lock.isdigit() == False:
        print ("System Malfunction: Invalid Module")
    else:
        if new_lock<0 or new_lock>num_modules:
            print("Invalid module. Operation failed.")
        elif new_lock == queen:
            print("Operation failed. Unable to lock module.")
        elif new_lock == locked:
            print("Nothing happened. This module is already locked.")
        else:
            locked = new_lock
            print("Aliens cannot get into module",locked)
            power_used = 25 + 5*random.randint(0,5)

def split_next(action):
    return [char for char in action] #Split "action" into an array, each character a different item in the array

def get_action():
    global module, last_module, possible_moves, power
    valid_action = False #Keep looping and asking the user where they want to go until they type either MOVE or SCANNER
    while valid_action == False:
        print("What do you want to do next ? (MOVE, SCANNER)")
        action = input(">")
        split_action = split_next(action)
        split_action_length = len(split_action) #Get the length of the array that contains where the person wants to move
        split_action_length = split_action_length - 1 
        #action.lower() == "move" or action.lower() == "m"
        
        if split_action[0].lower() == "m":
            split_action_length_down = int(split_action_length-1) #Length of array - 1
            split_action_last_number = split_action[split_action_length].isdigit() #If the last character is a number, change to true
            split_action_second_last = split_action[split_action_length_down].isdigit() #If the second last character is a number, change to true
            if split_action_last_number == True: #If last character is a number, continue and skip asking for which module you need to go to
                if split_action_second_last == True: #If the second last character is a number, continue and merge the two last characters
                    split_two_digits = split_action[split_action_length-1]+split_action[split_action_length] #Merge the two last digits together
                else:
                    split_two_digits = split_action[split_action_length] #Put the last digit in the variable
                move = int(split_two_digits)
                if move in possible_moves: #Check if it is between 1 and 17 (number of modules)
                    valid_action = True #Stop looping the input
                    last_module = module #Change the previous module variable
                    module = move #Change current module variable
                else:
                    print("Please retype it using the format of MOVE2")
            else:
                move = int(input("Enter the module to move to: "))
                if move in possible_moves: #Check if it is between 1 and 17 (number of modules)
                    valid_action = True #Stop looping the input
                    last_module = module #Change the previous module variable
                    module = move #Change current module variable
                    print ("Development: Power - " +str(power))
                    
                else:
                    print("The module must be connected to the current module.")
        if action.lower() == "scanner" or action.lower() == "s":
            loop_scanner = True
            while loop_scanner == True:
                command = input("Scanner is ready. The following commands are available (LOCK, MAP, POWER, BACK):")
                if command.lower() == "lock" or command.lower() == "l":
                    loop_scanner = False
                    lock()
                elif command.lower() == "power" or command.lower() == "p":
                    print ("The current power is at "+ str(power))
                elif command.lower() == "back" or command.lower() == "b":
                    loop_scanner = False
                elif command.lower() == "map" or command.lower() == "m":
                    print ("""\n\n\n\n\n                   ━━━━━━━━━      ━━━━━━━━━      ━━━━━━━━━      ━━━━━━━━━      ━━━━━━━━━      ━━━━━━━━━
                   ┃       ┃      ┃       ┃      ┃       ┃      ┃       ┃      ┃       ┃      ┃       ┃
           ────────┃   1   ┃──────┃   2   ┃──────┃   3   ┃──────┃   4   ┃──────┃   5   ┃──────┃   6   ┃────────
           │       ┃       ┃      ┃       ┃      ┃       ┃      ┃       ┃      ┃       ┃      ┃       ┃       │
           │       ━━━━━━━━━      ━━━━━━━━━      ━━━━━━━━━      ━━━━━━━━━      ━━━━━━━━━      ━━━━━━━━━       │
           │                          │              │              │              │                          │
           │               ───────────│              │              │              │───────────               │
           │               │                         ───────│────────                         │               │
       ━━━━━━━━━       ━━━━━━━━━                        ━━━━━━━━━                         ━━━━━━━━━       ━━━━━━━━━
       ┃       ┃       ┃       ┃                        ┃       ┃                         ┃       ┃       ┃       ┃
   ────┃   8   ┃───────┃   9   ┃────────────────────────┃   7   ┃─────────────────────────┃   13  ┃───────┃   14  ┃────
   │   ┃       ┃       ┃       ┃                        ┃       ┃                         ┃       ┃       ┃       ┃   │
   │   ━━━━━━━━━       ━━━━━━━━━                        ━━━━━━━━━                         ━━━━━━━━━       ━━━━━━━━━   │
   │       │                                                                                                  │       │
   │       │           ━━━━━━━━━                                                          ━━━━━━━━━           │       │
   │       │           ┃       ┃                                                          ┃       ┃           │       │
   │       ────────────┃   10  ┃                                                          ┃   15  ┃────────────       │
   │                   ┃       ┃                                                          ┃       ┃                   │
   │                   ━━━━━━━━━                                                          ━━━━━━━━━                   │
   │                       │                                                                  │                       │
   │   ━━━━━━━━━       ━━━━━━━━━                                                          ━━━━━━━━━       ━━━━━━━━━   │
   │   ┃       ┃       ┃       ┃                                                          ┃       ┃       ┃       ┃   │
   ────┃   11  ┃───────┃   12  ┃──────────────────────────────────────────────────────────┃   16  ┃───────┃   17  ┃────
       ┃       ┃       ┃       ┃                                                          ┃       ┃       ┃       ┃  
       ━━━━━━━━━       ━━━━━━━━━                                                          ━━━━━━━━━       ━━━━━━━━━\n\n\n""")
                
    
#Main program starts here

def gamemenu():
    global menu, menu_selection, selection
    while menu == 1:
        print ("\nTelium - The Game\n\n")
        print ("Please type PLAY to start the game, STORY to get the lore of the game or INSTRUCTIONS to find out how to play the game")
        menu_selection = input(str("> "))
        if menu_selection.lower() == "story" or menu_selection.lower() == "s": #If s or story is inputed, go to the function of story
            menu = 0
            selection = 2
            the_story()
        elif menu_selection.lower() == "instructions" or menu_selection.lower() == "instruction" or menu_selection.lower() == "i": #If i or instruction(s), go to the function instructions
            menu = 0
            selection = 3
            instructions()
        elif menu_selection.lower() == "play" or menu_selection.lower() == "start" or menu_selection.lower() == "game" or menu_selection.lower() == "p": #If p or game or play or start is inputed, go to the fucntion play
            menu = 0
            selection = 1
            spawn_npcs()
            game_play()
        else:
            print ("Invalid: Please type the item you want by typing the word in capitals.") #If it is none of them, ask to repeat using the correct the terms

def game_play():
    global alive, won, selection
    while alive == True and won == False and selection == 1: #Start of game - Loops the program, asking the location you want to go to
        
        print("Queen alien is located in module:",queen)
        print("Ventilation shafts are located in modules:",vent_shafts)
        print("Information panels are located in modules:",info_panels)
        print("Worker aliens are located in modules:",workers, "\n\n") #Output where the everything is
        print("There are 2 energy modules around the ship to restore 10% of the power")
        load_module() #Loads the module that globalises variables & imports the data from the module.txt files
        if won == False and alive == True: #If the game is not complete, output where you can go and get the input of what the player wants to do
            output_moves()
            get_action()
        else:
            break

def the_story():
    global selection, menu
    print ("A remote probe on the surface of Mars has detected biological signatures of dormant, single celledc primitive life. A sample of the Martian soil is returned to the space station orbiting the Earth for further analysis.\nThe sample of the orange coloured cells are examined and DNA analysis shows remarkable similarities to Dictyostelium discoideum, a species of soil-living amoeba here on Earth. Commonly referred to as slime mould, it transitions from a collection of unicellular amoebae into a multicellular organism and then into a fruiting body within its lifetime. Nicknamed, “Telium” due to its colour and cellular structure, the sample is incubated in the lab aboard the space station in conditions similar to when Mars was a warmer, wetter planet in its ancient past.\nRemarkably, independent Telium cells start to slowly move and after a period of several days have joined together to form an organism resembling a slug. In further days the slug-like creature grows additional arms and begins to look like a large starfish. Each cell working with other cells to become a single organism. Intrigued, scientists continue to examine the creature that appears to be consuming bacteria from inside the incubation chamber, growing in size daily. Telium begins to show signs of advanced movement around the chamber and grows significantly in strength. Eventually becoming strong enough to break out of its chamber, suffocating the scientist examining it, the animal scuttles through the space station to an unknown location. The organism is not seen for several days, but tension between the astronauts escalates when the space station electronics begin to behave erratically, power starts draining and communication is lost with Earth. “We are on our own. Telium needs to be found and killed. There is no protocol for this and we cannot risk further loss of life. We must stick together and work it out”, the captain orders.\n\n\n")
    selection = 0 #Print the story and go back to the menu
    menu = 1
    gamemenu ()

def instructions():
    global selection, menu
    print ("""\n\n\nThe space station has a limited amount of power which reduces on each turn. This provides a timer for the game. Telium – the queen alien, must be killed before the power runs out. The player is equipped with a flamethrower that requires fuel. This is used to kill aliens. The player also has a portable computer called ‘the scanner’, that has limited functionality to interact with the space station. On each turn, the player can use their scanner to lock the doors in a module. Locking the doors prevents aliens from moving to that module. Due to the station malfunction, only one module can be locked at a time. A player can move to an adjacent module. Each module could contain: \n• A ventilation shaft opening. In these modules the doors will lock on entry, forcing the player to move through the ventilation shaft. The dark passages lead to another random module. The player arrives in the new module and cannot return through the vent in the roof. \n• The queen alien (Telium). When the player enters the same module as Telium it attempts to escape via random adjacent modules. It can take 1-3 moves. If it arrives in a module with a ventilation shaft it will travel down the shaft arriving in a random module. If Telium is unable to move due to the only adjacent module being locked the player wins. \n• Worker aliens. Spawned asexually from the queen, the worker aliens gather bacteria for the queen to feed. They will attack the player if the player enters a module they are in. The player has the option to frighten the worker or attempt to kill it. This is done by using fuel from their flamethrower. The amount of fuel needed is not known by the player and will need to be deduced over several play attempts. The player will die if they do not frighten or kill the worker alien, losing the game. \n• An information panel. This costs power to use, but scans the space station and reveals the location of the queen. The remaining power in the station is also be shown by the panel.\n\n\n""")
    selection = 0 #Print the instructions and go back to the menu
    menu = 1
    gamemenu()

if won == True: #If the game has been won, print that the queen was killed and close the program
    print("The queen is trapped and you burn it to death with your flamethrower.")
    print("Game over. You win!")
    exit()

gamemenu() #On start, go to the game menu

#━

#┃

#                   ━━━━━━━━━      ━━━━━━━━━      ━━━━━━━━━      ━━━━━━━━━      ━━━━━━━━━      ━━━━━━━━━
#                   ┃       ┃      ┃       ┃      ┃       ┃      ┃       ┃      ┃       ┃      ┃       ┃
#           ────────┃   1   ┃──────┃   2   ┃──────┃   3   ┃──────┃   4   ┃──────┃   5   ┃──────┃   6   ┃────────
#           │       ┃       ┃      ┃       ┃      ┃       ┃      ┃       ┃      ┃       ┃      ┃       ┃       │
#           │       ━━━━━━━━━      ━━━━━━━━━      ━━━━━━━━━      ━━━━━━━━━      ━━━━━━━━━      ━━━━━━━━━       │
#           │                          │              │              │              │                          │
#           │               ───────────│              │              │              │───────────               │
#           │               │                         ───────│────────                         │               │
#       ━━━━━━━━━       ━━━━━━━━━                        ━━━━━━━━━                         ━━━━━━━━━       ━━━━━━━━━
#       ┃       ┃       ┃       ┃                        ┃       ┃                         ┃       ┃       ┃       ┃
#   ────┃   8   ┃───────┃   9   ┃────────────────────────┃   7   ┃─────────────────────────┃   13  ┃───────┃   14  ┃────
#   │   ┃       ┃       ┃       ┃                        ┃       ┃                         ┃       ┃       ┃       ┃   │
#   │   ━━━━━━━━━       ━━━━━━━━━                        ━━━━━━━━━                         ━━━━━━━━━       ━━━━━━━━━   │
#   │       │                                                                                                  │       │
#   │       │           ━━━━━━━━━                                                          ━━━━━━━━━           │       │
#   │       │           ┃       ┃                                                          ┃       ┃           │       │
#   │       ────────────┃   10  ┃                                                          ┃   15  ┃────────────       │
#   │                   ┃       ┃                                                          ┃       ┃                   │
#   │                   ━━━━━━━━━                                                          ━━━━━━━━━                   │
#   │                       │                                                                  │                       │
#   │   ━━━━━━━━━       ━━━━━━━━━                                                          ━━━━━━━━━       ━━━━━━━━━   │
#   │   ┃       ┃       ┃       ┃                                                          ┃       ┃       ┃       ┃   │
#   ────┃   11  ┃───────┃   12  ┃──────────────────────────────────────────────────────────┃   16  ┃───────┃   17  ┃────
#       ┃       ┃       ┃       ┃                                                          ┃       ┃       ┃       ┃  
#       ━━━━━━━━━       ━━━━━━━━━                                                          ━━━━━━━━━       ━━━━━━━━━

       
#
#
#
#
#
#
