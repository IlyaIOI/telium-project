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
fuel = 500          #The amount of fuel the player has in the flamethrower
locked = 0          #The module that has been locked by the player
queen = 0           #Location of the queen alien
vent_shafts = []    #Location of the ventilation shaft entrances
info_panels = []    #Location of the information panels
workers = []        #Location of the worker aliens

#Procedure declarations

#loads all modules players can move to
def load_module():
    global module, possible_moves
    possible_moves = get_modules_from(module)
    possible_moves = [i.strip('\n') for i in possible_moves]
    output_module()

#opens module's txt file
def get_modules_from(module):
    moves = []
    text_file = open("Hallownest/module" + str(module) + ".txt", "r")
    for counter in range(0,6):
        move_read = text_file.readline()
        if move_read != 0:
            moves.append(str(move_read))
    text_file.close()
    return moves

#prints current module
def output_module():
    global module
    print()
    print("-----------------------------------------------------------------")
    print()
    print(possible_moves[0])
    print(possible_moves[1])
    print()

#prints all modules player can move to
def output_moves():
    global possible_moves
    print()
    print("From here you can move to modules:")
    for move in range(2,6):
        print('| ', possible_moves[move])
    print()

#gets the players action
def get_action():
    global module, last_module, possible_moves, power
    valid_action = False
    while valid_action == False:
        print("What do you want to do next ? (MOVE, SCANNER)")
        action = input(">")
        if action.upper() == "MOVE" or action.upper() == "M":
            move = input("Enter the module to move to: ")
            print(possible_moves)
            if power <= 0:
                print("power 0")
                exit()
            elif move in possible_moves:
                power -= 1
                valid_action = True
                last_module = module
                module = move
            else:
                print("The module must be connected to the current module.")
    
#Main program starts here
    
while alive and not won:
    load_module()
    if won == False and alive == True:
        output_moves()
        get_action()

if won == True:
    print("The queen is trapped and you burn it to death with your flamethrower.")
    print("Game over. You win!")
if alive == False:
    print("The station has run out of power. Unable to sustain life support, you die.")
