#This is a board game based on the adventure of the great Polynesian Navigator Kupe


#Board Set up
def board(x_list):    
    for i in range(5):
        y_list = []
        x_list.append(y_list)
        for j in range(5):
            #Squares are represented by the "X"
            y_list.append("X")
    #I want to make the users space with an "O"
    #The user will originally start in the bottom corner
    x_list[4].pop(4)
    x_list[4].insert(4, "O")
    
def start_pos(x_pos, y_pos, x_list):
    #We need to find the users position so that we can move the character
    total = -1
    for row in x_list:
        total += 1
        if "O" in row:
            if row.index("O") == 0:
                y_pos = 0
                x_pos = 1
            elif row.index("O") == 1:
                y_pos = 1
                x_pos = total
            elif row.index("O") == 2:
                y_pos = 2
                x_pos = total
            elif row.index("O") == 3:
                y_pos = 3
                x_pos = total
            elif row.index("O") == 4:
                y_pos = 4
                x_pos = total
    return x_pos, y_pos
#Moving the character on the board
def move_board(direction, position, x_list, x_pos, y_pos):
    invalid_l = ["x_list[0][0]", "x_list[0][1]", "x_list[0][2]", "x_list[0][3]", "x_list[0][4]"]
    invalid_u = ["x_list[0][0]", "x_list[1][0]", "x_list[2][0]", "x_list[3][0]", "x_list[4][0]"]
    invalid_d = ["x_list[0][4]", "x_list[1][4]", "x_list[2][4]", "x_list[3][4]", "x_list[4][4]"]
    invalid_r = ["x_list[4][0]", "x_list[4][1]", "x_list[4][2]", "x_list[4][3]", "x_list[4][4]"]
    if direction == "left":
        if position in invalid_l:
            print("Sorry but you can't move there")
        else:
            print("Moving left...")
            #Making the new position:

            #Removing the original position
            x_list[x_pos].pop(y_pos)
            x_list[x_pos].insert(y_pos, "X")
            x_pos -= 1
            #Updating the new Position
            x_list[x_pos].pop(y_pos)
            x_list[x_pos].insert(y_pos, "O")
            #string value for the position
            position = "x_list" + "[" + str(x_pos) + "]" + "[" + str(y_pos) + "]"
            print(position)
            return x_pos, y_pos
    elif direction == "right":
        if position in invalid_r:
            print("Sorry but you can't move there")
        else:
            print("Moving right...")
            x_list[x_pos].pop(y_pos)
            x_list[x_pos].insert(y_pos, "X")
            x_pos += 1
            #Updating the new Position
            x_list[x_pos].pop(y_pos)
            x_list[x_pos].insert(y_pos, "O")
            #string value for the position
            position = "x_list" + "[" + str(x_pos) + "]" + "[" + str(y_pos) + "]"
            return x_pos, y_pos
    elif direction == "up":
        if position in invalid_u:
            print("Sorry but you can't move there")
        else:
            print("Moving up...")
            x_list[x_pos].pop(y_pos)
            x_list[x_pos].insert(y_pos, "X")
            y_pos -= 1
            #Updating the new Position
            x_list[x_pos].pop(y_pos)
            x_list[x_pos].insert(y_pos, "O")
            #string value for the position
            position = "x_list" + "[" + str(x_pos) + "]" + "[" + str(y_pos) + "]"
            return x_pos, y_pos
    elif direction == "down":
        if position in invalid_d:
            print("Sorry but you can't move there")
        else:
            print("Moving down...")
            x_list[x_pos].pop(y_pos)
            x_list[x_pos].insert(y_pos, "X")
            y_pos += 1
            #Updating the new Position
            x_list[x_pos].pop(y_pos)
            x_list[x_pos].insert(y_pos, "O")
            #string value for the position
            position = "x_list" + "[" + str(x_pos) + "]" + "[" + str(y_pos) + "]"
            return x_pos, y_pos
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
    options = ['w', 'a', 's', 'd']
    again = True
    while again:
        repeat = True
        while repeat:
            for i in range(len(x_list)):
                for j in range(len(x_list[i])):
                    print(x_list[j][i], end = " ")
                print()
            print("=========")
            option = input("""What would you like to do?
W) UP
A) LEFT
S) DOWN
D) RIGHT
F) Fish
""").lower()
            #Checking if the user chose a valid option
            if option not in options:
                print("Please choose one of the options")
            elif option in options:
                repeat = False
        #Changing the direction depending on the input
        if option == "w":
            direction = "up"
            x_pos, y_pos = move_board(direction, position, x_list, x_pos, y_pos)
        elif option == "a":
            direction = "left"
            x_pos, y_pos = move_board(direction, position, x_list, x_pos, y_pos)
        elif option == "s":
            direction = "down"
            x_pos, y_pos = move_board(direction, position, x_list, x_pos, y_pos)
        elif option == "d":
            direction = "right"
            x_pos, y_pos = move_board(direction, position, x_list, x_pos, y_pos)
        
    

main()    

