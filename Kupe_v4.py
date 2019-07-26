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

#Story for the discovery of Aoteroa
def story(chapter):
    if chapter == 1:
        print("""Although Maui fished up the North and South Islands, it was the great Polynesian navigator Kupe who discovered them. Kupe lived in Hawaiiki, mythical ancestral homeland of the Māori. In Hawaiiki lived a canoe maker by the name of Toto. 

Toto fabricated two huge ocean going canoes from a large tree. One canoe he named Aotea and the other he named Matahorua. Toto gave his canoe named Aotea to one of his daughters, Rongorongo, and the other canoe named Matahorua to his other daughter, Kura. It happened that Kupe desired Kura very much. However, Kura was already the wife of Kupe's cousin Hoturapa. """)
        print()
    elif chapter == 2:
        print("""When Hoturapa and Kupe were out fishing one day, Kupe ordered Hoturapa to dive down and free Kupe's fishing line, which had become tangled. When Hoturapa dived into the sea to free the tangled line, Kupe sliced through the anchor rope of the canoe, and began to row furiously back to shore. Hoturapa drowned, but his family were suspicious of the circumstances surrounding his death. It was, in fact, a plan on Kupe's part to take Hoturapa's wife Kura. """)
        print()
    elif chapter == 3:
        print("""In order to avoid vengeance from Hoturapa's family, Kupe and his own family left Hawaiiki in Kura's canoe Matahorua. After some time of navigating, Kupe's wife Hine Te Aparangi sighted the islands of New Zealand, which appeared as land lying beneath a cloud. Because of this, they named the islands Aotearoa, Land of the Long White Cloud. """)
        print()
    #At this chapter I would add the octopus into the game
    elif chapter == 4:
        print("""As Kupe and his crew were sailing along the coast of this new land, they disturbed a giant octopus, who was hiding in a coastal cave. Terrified at the sight of a strange canoe filled with human beings, the huge octopus swam rapidly in front of the Matahorua and took flight, passing through the strait between the North and South Islands. Kupe followed the octopus, and discovered modern Cook Strait. 

Kupe and the Matahorua eventually caught up with the giant octopus. In defence, the octopus whipped its enormous tentacles around the canoe, intent on devouring the whole canoe.""")
        print()
    elif chapter == 5:
        print("""During the furious battle which followed with the sea monster, it became obvious that the Matahorua was in great danger of breaking up. 

However, Kupe suddenly had an idea, and threw a large water gourd overboard. The octopus, thinking that a man had fallen over, released it's tentacles from the Matahorua and turned to attack the gourd. Kupe seized this opportunity, and waited until the octopus was entwined around the gourd. Kupe then attacked the head of the octopus with his adze, and the octopus died. """)
        print()
    else:
        print("""With his adze, Kupe then cut several islands away from the South Island, and several islands away from the North Island, including the island of Kapiti. He remained for a short while in modern Wellington, before continuing northwards up the coast of the North Island, naming various islands, rivers and harbours on the way. Kupe then returned to Hawaiiki, telling everybody of this distant cloud capped and high rising land which he had discovered. 

sHe gave instructions on how to return to this new land, but said that he himself would not be returning. """)
        
#Randomising the location of the story tile
def randomise_tile(x_list):
    #randomise the x axis
    number1 = random.randint(0, 4)
    #randomise the y axis
    number2 = random.randint(0, 4)
    #Add a value to a certain tile, and when landed on this tile, it will give the story and delete the key
    x_list[number1][number2].append("S")
    print(x_list)
    print(number1)
    print(number2)
    return number1, number2
    
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

def hint(x_story, y_story):
    chance = random.randint(1, 2)
    if chance == 1:
        print("The next part of the story is hidden somewhere on X = {}".format(x_story + 1))
    else:
        print("The next part of the story is hidden somewhere on row {}".format(y_story + 1))

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
def move_board(direction, current_position, x_list, x_pos, y_pos, turns, x_story, y_story):
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
        #Checking if user lands on significant tile
        if "S" in x_list[x_pos][y_pos]:
            print("Yes this significant")
            chapter += 1
            del x_list[x_pos][y_pos][2]
            story(chapter)
            x_story, y_story = randomise_tile(x_list)
        else:
            print("No not here")
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
Every time you fish on a tile, the chance to catch a bonus fish will decrease, so keep moving



Good luck!

<---------------------------------------->
""")


#Menu system for the input
def main():
    instructions()
    original_turn = 0
    chapter = 1
    story(chapter)
    #Printing the board to the user
    x_list = []
    board(x_list)
    x_story, y_story = randomise_tile(x_list)
    #Position as a fixed starting place
    position = "x_list[4][4]"
    x_pos, y_pos = start_pos(x_list)
    #Fish Inventory - start with 3 as of the project plan
    fish = 3
    #Starting turns
    turns = 55
    #Making a variable for the chance, but later I will put this chance within a dictionary for each tile
    options = ['w', 'a', 's', 'd', 'f', 'i']
    
    #Need to make a way that when turns reach 0 the game will end
    print("Starting Fish: {}".format(fish))
    print("Turns: {}".format(turns))
    if turns%5 == 0:
        hint(x_story, y_story)
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
            print("=========")
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
            x_pos, y_pos, position, turns = move_board(direction, position, x_list, x_pos, y_pos, turns, x_story, y_story)
        elif option == "a":
            direction = "left"
            x_pos, y_pos, position, turns = move_board(direction, position, x_list, x_pos, y_pos, turns, x_story, y_story)
        elif option == "s":
            direction = "down"
            x_pos, y_pos, position, turns = move_board(direction, position, x_list, x_pos, y_pos, turns, x_story, y_story)
        elif option == "d":
            direction = "right"
            x_pos, y_pos, position, turns = move_board(direction, position, x_list, x_pos, y_pos, turns, x_story, y_story)
        elif option == "f":
            fish = add_fish(fish, x_list, x_pos, y_pos)#Later will also give the dictionary for tiles, so you can decrease fish chance
        elif option == "i":
            inventory(turns, fish)
            
        
    
main()    

