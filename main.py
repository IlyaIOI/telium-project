import random

# ---- global variables ----

num_modules = 17
module = 1
last_module = 0
possible_moves = []
alive = True
won = False
power = 100
fuel = 500

# ---- flamethrower ----

locked = 0
queen = 0
vent_shafts = []
info_panels = []
workers = []

def load_module():
    global module, possible_moves
    possible_moves = get_modules_from(module)
    output_module()

def get_modules_from(module):
    moves = []
    text_file = open("Charles_Darwin\module" + str(module) + ".txt", "r")
    for counter in range(0,4):
        move_read = text_file.readline()
        move_read = int(move_read.strip())
        if move_read != 0:
            moves.append(move_read)
            
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
    print("From here you can move to modules: | ",end='')
    for move in possible_moves:
        print(move,'| ',end='')
        print()

def get_action():
    global module, last_module, possible_moves
    valid_action = False
    while valid_action == False:
        print("What do you want to do next ? (MOVE, SCANNER)")
        action = input(">")
        if action == "MOVE":
            move = int(input("Enter the module to move to: "))
            if move in possible_moves:
                valid_action = True
                last_module = module
                module = move
            else:
                print("The module must be connected to the current module.")

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
