#This is a board game based on the adventure of the great Polynesian Navigator Kupe

#When creating 'landmarks', I will need to create each tile a dictionary
#But display the "X"
#When you have 'discovered' a landmark i will rerandomise, the next landmark
#Octopus (%) will have it's own movement and will cause the user to lose fish if you move onto the same tile.
import random

WATER = "X"
WAKA = "O"

#Board Set up
def board(x_list):    
    for i in range(5):
        y_list = []
        x_list.append(y_list)
        for j in range(5):
            #Squares are represented by the "X"
            y_list.append(WATER)
    #I want to make the users space with an "O"
    #The user will originally start in the bottom corner
    x_list[4].pop(4)
    x_list[4].insert(4, WAKA)
    
def start_pos(x_pos, y_pos, x_list):
    #We need to find the users position so that we can move the character
    total = -1
    for row in x_list:
        total += 1
        if WAKA in row:
            if row.index(WAKA) == 0:
                y_pos = 0
                x_pos = 1
            elif row.index(WAKA) == 1:
                y_pos = 1
                x_pos = total
            elif row.index(WAKA) == 2:
                y_pos = 2
                x_pos = total
            elif row.index(WAKA) == 3:
                y_pos = 3
                x_pos = total
            elif row.index(WAKA) == 4:
                y_pos = 4
                x_pos = total
    return x_pos, y_pos

#Changing/removing the current the position
def change_position(x_pos, y_pos, board_item, x_list):
        x_list[x_pos].pop(y_pos)
        x_list[x_pos].insert(y_pos, board_item)    
        
#Fishing for new fish
def add_fish(fish):
    BONUS = 1
    NO_BONUS = 0
    
    #So far I will set the chance to 1, chance will later be stored in the dictionary
    chance = 1
    #Chance that the user gains a bonus fish
    amount = random.randint(1,10)
    #If the user has chances above 0.8 then they will gain 2 + 1 bonus
    if chance > 0.7:
        # Comparing their chances and using the roll to see if they get more fish
        if chance == 1:
            new_amount = BONUS
        elif chance == 0.9:
            if amount < 10:
                new_amount = BONUS
            else:
                new_amount = NO_BONUS
        elif chance == 0.8:
            if amount < 9:
                new_amount = BONUS
            else:
                new_amount = NO_BONUS
        fish += (2 + new_amount)
    #If they are above 0.5 then they will gain 1 + 1 bonus
    elif chance > 0.4:
        if chance == 0.7:
            if amount < 8:
                new_amount = BONUS
            else:
                new_amount = NO_BONUS
        elif chance == 0.6:
            if amount < 7:
                new_amount = BONUS
            else:
                new_amount = NO_BONUS
        elif chance == 0.5:
            if amount < 6:
                new_amount = BONUS
            else:
                new_amount = NO_BONUS
        fish += (1 + new_amount)
    chance -= 0.1
    print(fish)
    return fish, chance

  
#Moving the character on the board
def move_board(direction, current_position, x_list, x_pos, y_pos):
    invalid_l = (direction == "left") and (current_position in ["x_list[0][0]", "x_list[0][1]", "x_list[0][2]", "x_list[0][3]", "x_list[0][4]"])
    invalid_u = (direction == "up") and (current_position in ["x_list[0][0]", "x_list[1][0]", "x_list[2][0]", "x_list[3][0]", "x_list[4][0]"])
    invalid_d = (direction == "down") and (current_position in ["x_list[0][4]", "x_list[1][4]", "x_list[2][4]", "x_list[3][4]", "x_list[4][4]"])
    invalid_r = (direction == "right") and (current_position in ["x_list[4][0]", "x_list[4][1]", "x_list[4][2]", "x_list[4][3]", "x_list[4][4]"])
    
    if invalid_l or invalid_u or invalid_d or invalid_r:
        print("Sorry but you aren't allowed to go {}".format(direction))
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
        print(new_position)
    return x_pos, y_pos, new_position

#Menu system for the input
def main():
    #Printing the board to the user
    x_list = []
    board(x_list)
    #Position as a fixed starting place
    position = "x_list[4][4]"
    x_pos = 0
    y_pos = 0
    x_pos, y_pos = start_pos(x_pos, y_pos, x_list)
    print(x_pos)
    print(y_pos)
    #Fish Inventory - start with 3 as of the project plan
    fish = 3
    #Making a variable for the chance, but later I will put this chance within a dictionary for each tile
    chance = 1
    options = ['w', 'a', 's', 'd', 'f']
    again = True
    while again:
        repeat = True
        print("=========")
        while repeat:
            for i in range(len(x_list)):
                for j in range(len(x_list[i])):
                    print(x_list[j][i], end = " ")
                print()
            print("=========")
            print(position)
            option = input("""What would you like to do?
W) UP
A) LEFT
S) DOWN
D) RIGHT
F) Fish
""").lower().strip()
            #Checking if the user chose a valid option
            if option not in options:
                print("Please choose one of the options")
            elif option in options:
                repeat = False
        #Changing the direction depending on the input
        if option == "w":
            direction = "up"
            x_pos, y_pos, position = move_board(direction, position, x_list, x_pos, y_pos)
        elif option == "a":
            direction = "left"
            x_pos, y_pos, position = move_board(direction, position, x_list, x_pos, y_pos)
        elif option == "s":
            direction = "down"
            x_pos, y_pos, position = move_board(direction, position, x_list, x_pos, y_pos)
        elif option == "d":
            direction = "right"
            x_pos, y_pos, position = move_board(direction, position, x_list, x_pos, y_pos)
        elif option == "f":
            fish, chance = add_fish(fish)#Later will also give the dictionary for tiles, so you can decrease fish chance
            
            
        
    
main()    

