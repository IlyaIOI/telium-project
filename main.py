#Telium – The game
import random
#Global variables
num_modules = 17    #The number of modules in the space station
module = 1          #The module of the space station we are in
last_module = 0     #The last module we were in
possible_moves = [] #List of the possible moves we can make
alive = True        #Whether the player is alive or dead
won = False         #Whether the player has won
power = 5 #100         #The amount of power the space station has
fuel = 500          #The amount of fuel the player has in the
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
    moves = [] #Array containing spaces you can go to from current position
    text_file = open("Charles_Darwin/module" + str(module) + ".txt", "r") #Open the module you are currently in to find out which modules you can go to from the current position
    for counter in range(0,4): 
        move_read = text_file.readline() #For every line, read it and append it to the array
        if move_read != 0:
            moves.append(int(move_read))
    text_file.close()
    return moves

def output_module():
    global module
    print()
    print("-----------------------------------------------------------------")
    print()
    print("You are in module",module)
    print()

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
            print(possible_moves)
            if move in possible_moves: #Check if it is between 1 and 17 (number of modules)
                valid_action = True #Stop looping the input
                last_module = module #Change the previous module variable
                module = move #Change current module variable
                print (str(power))
                    
            else:
                print("The module must be connected to the current module.")
    
#Main program starts here
    
while alive == True and won == False: #Start of game - Loops the program, asking the location you want to go to
    load_module() #Loads the module that globalises variables & imports the data from the module.txt files
    if won == False and alive == True: #If the game is not complete, output where you can go and get the input of what the player wants to do
        output_moves()
        get_action()
    else:
        break

if won == True:
    print("The queen is trapped and you burn it to death with your flamethrower.")
    print("Game over. You win!")



