print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = " "
lake = " "
door = " "
direction = input('You are at a crossroads. '
                  'Which way do you want to go? Type \'right\' or \'left\'\n').lower()
if direction == "left":
    lake = input('You arrive at a lake. There is an island in the middle of the lake. '
                 'Type "swim" to swim or "wait" to wait for a boat.\n').lower()
    if lake == "wait":
        print("A small boat arrives and you can row savely over to an island.")
        door = input('On the island is a house with 3 doors. '
                     'Which door do you want to enter? Choose: red, yellow or blue:\n ').lower()
        if door == "yellow":
            print("You arrive savely at treasure island. Enjoy your loot.")
        elif door == "red":
            print("You walked into a trap of spears. You are bleeding out. Game over!")
        elif door == "blue":
            print("You are being haunted by ghosts. Game over!")
        else:
            print("Can't choose? I guess you die. Game over!")
    else:
        print("You have been eaten by the famous lake shark. Game over!")
else:
    print("You fell into a hole in the ground. Game over!")
