#Telium – The game
import random
#Global variables
story = 'Hallownest'
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

#menu lets player see instructions and choose story
def display_menu():
    global story
    while True:
        print("WELCOME TO TELIUM")
        print("c - change story\ni - instructions\ns - start")
        action = input('')
        if action.upper() == "S":
            break
        elif action.upper() == "I":
            print("go through modules and kill the queen")
        elif action.upper() == "C":
            print("1) Hallownest\n2) The Darwin")
            choice = input('')
            if choice == '1':
                story = 'Hallownest'
            elif choice == '2':
                story = 'Charles_Darwin'
        

#loads all modules players can move to
def load_module():
    global module, possible_moves
    possible_moves = get_modules_from(module)
    possible_moves = [i.strip('\n') for i in possible_moves]
    output_module()

#opens module's txt file
def get_modules_from(module):
    moves = []
    text_file = open(story + "/module" + str(module) + ".txt", "r")
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
    if int(module) == queen:
        print("There's a Queen in here")
        print()
    if int(module) in vent_shafts:
        print("There's a stag station in here")
        print()
    if int(module) in info_panels:
        print("There's an info panel in here")
        print()
    if int(module) in workers:
        print("There's a infected bug in here")
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
        try:
            if action[0].upper() == "M":
                move = ''
                if action[len(action)-2].isdigit():
                    move = action[len(action)-2]
                if action[len(action)-1].isdigit():
                    move += action[len(action)-1]
                else:
                    move = input("Enter the module to move to: ")
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
            if action[0].upper() == "S":
                command = input("Scanner ready. Enter command (LOCK):")
                if command.upper() == "LIFEFORMS":
                    print("You sense " +str(len(workers) + 1) + " infected insects.")
                elif command[0].upper() == "L":
                    move = 0
                    if command[len(command)-2].isdigit():
                        command = int(command[len(command)-2])
                    if command[len(command)-1].isdigit():
                        move += int(command[len(command)-1])
                    lock(move)
        except:
            continue

#spawns the NPCs of the game
def spawn_npcs():
    global num_modules, queen, vent_shafts, info_panels, workers
    module_set = []
    for counter in range(2,num_modules):
        module_set.append(counter)
    random.shuffle(module_set)#makes a list of shuffled rooms
    i = 0
    queen = module_set[i]
    for counter in range(0,3): #sets three random rooms for vents
        i=i+1
        vent_shafts.append(module_set[i])
    for counter in range(0,2): #sets two random rooms for info pannels
        i=i+1
        info_panels.append(module_set[i])
    for counter in range(0,3): #sets three random room for workers
        i=i+1
        workers.append(module_set[i])

def check_vent_shafts():
    global num_modules, module, vent_shafts, fuel
    if int(module) in vent_shafts:
        print("There is a SOUL statue in here.")
        print("You absorb it into your body.")
        fuel_gained = 50
        print("Soul was",fuel,"now reading:",fuel+fuel_gained)
        fuel = fuel + fuel_gained
        print("The ground suddenly starts shaking.")
        print("The floor collapses beneath you and you fall.")
        print("We follow the passages and find ourselves sliding down.")
        last_module = module
        module = random.choice([i for i in range(1,num_modules) if i not in vent_shafts or i != module])

#allows user to lock modules
def lock(new_lock):
    global num_modules, power, locked
    try:
        if new_lock <= 0:
            new_lock = int(input("Enter module to lock:"))
        if new_lock<0 or new_lock>num_modules: #validates chosen module
            print("Invalid module. Operation failed.")
        elif new_lock == queen:
            print("Operation failed. Unable to lock module.")
        elif new_lock == locked:
            print("Module already locked")
        else:
            locked = new_lock
            print("Aliens cannot get into module",locked)
    except:
        print("Invalid input.")
    power -= 25 + 5*random.randint(0,5) #uses power

def move_queen():
    global num_modules, module, last_module, locked, queen, won, vent_shafts
    #If we are in the same module as the queen...
    if int(module) == queen:
        print("There it is! The queen alien is in this module...")
        #Decide how many moves the queen should take
        moves_to_make = random.randint(1,3)
        can_move_to_last_module = False
        while moves_to_make > 0:
            #Get the escapes the queen can make
            escapes = get_modules_from(queen)
            #Remove the current module as an escape
            if module in escapes:
                escapes.remove(module)
            #Allow queen to double back behind us from another module
            if last_module in escapes and can_move_to_last_module == False:
                escapes.remove(last_module)
            #Remove a module that is locked as an escape
            if locked in escapes:
                escapes.remove(locked)
            #If there is no escape then player has won...
            if len(escapes) == 0:
                won = True
                moves_to_make = 0
                print("...and the door is locked. It's trapped.")
            #Otherwise move the queen to an adjacent module
            else:
                if moves_to_make == 1:
                    print("...and has escaped.")
                queen = random.choice(escapes)
                moves_to_make = moves_to_make - 1
                can_move_to_last_module = True
                #Handle the queen being in a module with a ventilation shaft
                while queen in vent_shafts:
                    if moves_to_make > 1:
                        print("...and has escaped.")
                    print("We can hear scuttling in the ventilation shafts.")
                    valid_move = False
                    #Queen cannot land in a module with another ventilation shaft
                    while valid_move == False:
                        valid_move = True
                        queen = random.randint(1,num_modules)
                        if queen in vent_shafts:
                            valid_move = False
                    #Queen always stops moving after travelling through shaft
                    #moves_to_make = 0

#checks fuel and tells player if low
def fuel_check():
    global fuel
    if fuel < 100:
        print("You have low SOUL")
    
#Main program starts here
display_menu()

#spawns in all npcs and then output's their locations
spawn_npcs()
print("Queen alien is located in module:",queen)
print("Ventilation shafts are located in modules:",vent_shafts)
print("Information panels are located in modules:",info_panels)
print("Worker aliens are located in modules:",workers)
    
while alive and not won:
    check_vent_shafts()
    move_queen()
    load_module()
    if won == False and alive == True:
        fuel_check()
        output_moves()
        get_action()


if won == True:
    print("The queen is trapped and you burn it to death with your flamethrower.")
    print("Game over. You win!")
if alive == False:
    print("The station has run out of power. Unable to sustain life support, you die.")
