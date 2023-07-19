
#Author : Chit Ko Ko




print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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






l="left"
s='swim'
w='wait'
r_ed='red'
b_lue='blue'
y_ellow='yellow'


direction=(input("left or right?"))
if direction == 'right':
  print("Fall into a hole. Game over.")
elif direction == l:

  
    transportation=(input("swim or wait?"))
    if transportation == s:
        print("Attacked by trout. Game Over.")
    elif transportation == w:


        doorcolor=(input("Which door?"))

        if doorcolor == r_ed:
            print("Burned by fire. Game Over.")
        elif doorcolor == b_lue:
            print("Eaten by beasts. Game Over.")
        elif doorcolor == y_ellow:
            print("You win!")
        else:
            print("Game Over.")
    else:
        print("Invalid transportation input. Game Over.")
else:
    print("Invalid direction input. Game Over.")
