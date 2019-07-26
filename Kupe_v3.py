#This is a board game based on the adventure of the great Polynesian Navigator Kupe

#When creating 'landmarks', I will need to create each tile a dictionary
#But display the "X"
#When you have 'discovered' a landmark i will rerandomise, the next landmark
#Octopus (%) will have it's own movement and will cause the user to lose fish if you move onto the same tile.
import random

#CONSTANTS
WATER = "X"
WAKA = "O"
#Default chance

CHANCE = 1

X_RANGE = 5
Y_RANGE = 5

#Board Set up
def board(x_list):    
    for i in range(X_RANGE):
        y_list = []
        x_list.append(y_list)
        for j in range(Y_RANGE):
            #Squares are represented by the "X"
            y_list.append([WATER, CHANCE])
    #I want to make the users space with an "O"
    #The user will originally start in the bottom corner
    x_list[4].pop(4)
    x_list[4].insert(4, [WAKA, CHANCE])
    
def start_pos(x_list):
    #We need to find the users position so that we can move the character
    for x_pos in range(len(x_list)):
        for y_pos in range(len(x_list[x_pos])):
            if x_list[x_pos][y_pos][0] == WAKA:
                return x_pos, y_pos

#Changing/removing the current the position
def change_position(x_pos, y_pos, board_item, x_list):
        #Retaining the chance that the tile had before
        fish_chance = x_list[x_pos][y_pos][1]
        x_list[x_pos].pop(y_pos)
        x_list[x_pos].insert(y_pos, [board_item, fish_chance])
        
#Fishing for new fish
def add_fish(fish, x_list, x_pos, y_pos):
    BONUS = 1
    NO_BONUS = 0
    new_amount = 0
    #So far I will set the chance to 1, chance will later be stored in the dictionary
    #Chance that the user gains a bonus fish
    amount = random.randint(1,10)
    #Chance of bonus fish on this certain tile
    chance = x_list[x_pos][y_pos][1]
    #If the user has chances above 0.8 then they will gain 2 + 1 bonus
    if round(chance, 1) > 0.7:
        # Comparing their chances and using the roll to see if they get more fish
        if chance == 1:
            new_amount = BONUS
        elif round(chance, 1) == 0.9:
            if amount < 10:
                new_amount = BONUS
            else:
                new_amount = NO_BONUS
        elif round(chance, 1) == 0.8:
            if amount < 9:
                new_amount = BONUS
            else:
                new_amount = NO_BONUS
        fish += (2 + new_amount)
    #If they are above 0.5 then they will gain 1 + 1 bonus
    elif round(chance, 1) > 0.4:
        if round(chance, 1) == 0.7:
            if amount < 8:
                new_amount = BONUS
            else:
                new_amount = NO_BONUS
        elif round(chance, 1) == 0.6:
            if amount < 7:
                new_amount = BONUS
            else:
                new_amount = NO_BONUS
        elif round(chance, 1) == 0.5:
            if amount < 6:
                new_amount = BONUS
            else:
                new_amount = NO_BONUS
        fish += (1 + new_amount)
    elif round(chance, 1) < 0.5:
        if round(chance, 1) == 0.4:
            if amount < 5:
                new_amount = BONUS
            else:
                new_amount = NO_BONUS
        elif round(chance, 1) == 0.3:
            if amount < 4:
                new_amount = BONUS
            else:
                new_amount = NO_BONUS
        elif round(chance, 1) == 0.2:
            if amount < 3:
                new_amount = BONUS
            else:
                new_amount = NO_BONUS
        elif round(chance, 1) == 0.1:
            if amount < 2:
                new_amount = BONUS
            else:
                new_amount = NO_BONUS
        else:
            new_amount = NO_BONUS
            print("You have already gotten all the fish available on this tile")

        fish += new_amount

    #Golden/rotten fish

    golden = random.randint(1, 100)

    if golden == 1:
        print("You got a GOLDEN FISH!!!")
        print("+ 10 fish")
        fish += 10
    elif golden == 2:
        print("Oh No! you fished a rotten fish")
        print("- 2 fish")
        fish -= 2
    x_list[x_pos][y_pos][1] -= 0.1
    chance = x_list[x_pos][y_pos][1]
    print("Fish: ", fish)
    print("Tiles Chance: ", chance)
    return fish

  
#Moving the character on the board
def move_board(direction, current_position, x_list, x_pos, y_pos, turns):
    invalid_l = (direction == "left") and (current_position in ["x_list[0][0]", "x_list[0][1]", "x_list[0][2]", "x_list[0][3]", "x_list[0][4]"])
    invalid_u = (direction == "up") and (current_position in ["x_list[0][0]", "x_list[1][0]", "x_list[2][0]", "x_list[3][0]", "x_list[4][0]"])
    invalid_d = (direction == "down") and (current_position in ["x_list[0][4]", "x_list[1][4]", "x_list[2][4]", "x_list[3][4]", "x_list[4][4]"])
    invalid_r = (direction == "right") and (current_position in ["x_list[4][0]", "x_list[4][1]", "x_list[4][2]", "x_list[4][3]", "x_list[4][4]"])
    if invalid_l or invalid_u or invalid_d or invalid_r:
        print("Sorry but you aren't allowed to go {}".format(direction))
        turns += 1
        new_position = current_position
    else:
        change_position(x_pos, y_pos, WATER, x_list)
        if direction == "left":
            print("Moving left...")
            #Removing the original position
            x_pos -= 1
        elif direction == "right":
            print("Moving right...")
            x_pos += 1
        elif direction == "up":
            print("Moving up")
            y_pos -= 1
        else:
            print("Moving down")
            y_pos += 1
        change_position(x_pos, y_pos, WAKA, x_list)
        
        #string value for the position
        new_position = "x_list" + "[" + str(x_pos) + "]" + "[" + str(y_pos) + "]"
    return x_pos, y_pos, new_position, turns

def inventory(turns, fish):
    print("This is your inventory")
    option = ""
    while option != "x":
        print()
        option = input("""Do you want to...
(F) Check your fish inventory
(T) Check how many turns are left
(X) Exit """).lower().strip()
        if option == "f":
            print()
            print("You have {} fish".format(fish))
            if turns % 2 == 0:
                print("In two turns time, you will lose one fish")
            else:
                print("In one turn, you will lose one fish")
        elif option == "t":
            print()
            print("You are on turn: {}".format(30-turns))
            print("There are {} turns remaining".format(turns+1))


def lose_fish(turns, fish, original_turn):
    if turns == 30:
        original_turn = turns
        return True, fish, original_turn
    elif turns % 2 == 0 and turns!= original_turn:
        fish -= 1
        if fish < 0:
            print("Game Over!!!")
            original_turn = turns
            return False, fish, original_turn
        else:
            original_turn = turns
            return True, fish, original_turn
    else:
        original_turn = turns
        return True, fish, original_turn

def instructions():
    print("""
Welcome to Kupe's Discovery of Aoteroa

In this game you will travel across a board to discover the story of Kupe

While traversing the ocean, you will need to catch fish
but watchout, the more you fish on the same tile, the less fish there are to catch
One more thing, every two turns you will lose a fish


Good luck!
""")


#Menu system for the input
def main():
    instructions()
    original_turn = 0
    #Printing the board to the user
    x_list = []
    board(x_list)
    #Position as a fixed starting place
    position = "x_list[4][4]"
    x_pos, y_pos = start_pos(x_list)
    #Fish Inventory - start with 3 as of the project plan
    fish = 3
    #Starting turns
    turns = 30
    #Making a variable for the chance, but later I will put this chance within a dictionary for each tile
    options = ['w', 'a', 's', 'd', 'f', 'i']

    #Need to make a way that when turns reach 0 the game will end
    print("Starting Fish: {}".format(fish))
    print("Turns: 30".format(turns))
    
    again = True
    while again:
        if turns == 0:
            print("Game OVER")
            break
        play, fish, original_turn = lose_fish(turns, fish, original_turn)
        if play == False:
            break
        repeat = True
        while repeat:
            print("=========")
            for x in range(len(x_list)):
                ##print (range(len(x_list[x])))
                for y in range(len(x_list[x])):
                    print(x_list[y][x][0], end = " ")
                print()
            turns -= 1
            option = input("""What would you like to do?
W) UP
A) LEFT
S) DOWN
D) RIGHT
F) Fish
I) Check Inventory
""").lower().strip()
            #Checking if the user chose a valid option
            if option not in options:
                print("Please choose one of the options")
                turns += 1
            elif option in options:
                repeat = False
        #Changing the direction depending on the input
        if option == "w":
            direction = "up"
            x_pos, y_pos, position, turns = move_board(direction, position, x_list, x_pos, y_pos, turns)
        elif option == "a":
            direction = "left"
            x_pos, y_pos, position, turns = move_board(direction, position, x_list, x_pos, y_pos, turns)
        elif option == "s":
            direction = "down"
            x_pos, y_pos, position, turns = move_board(direction, position, x_list, x_pos, y_pos, turns)
        elif option == "d":
            direction = "right"
            x_pos, y_pos, position, turns = move_board(direction, position, x_list, x_pos, y_pos, turns)
        elif option == "f":
            fish = add_fish(fish, x_list, x_pos, y_pos)#Later will also give the dictionary for tiles, so you can decrease fish chance
        elif option == "i":
            inventory(turns, fish)
            
        
    
main()    

