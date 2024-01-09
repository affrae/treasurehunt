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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇


def lowerInput(question):
    return input(f"{question} ").lower()


gameArray = [{
    '0':
    "You are at a crossroad.\nWhere do you want to go? Type 'left' or 'right'",
    'left': 1,
    'right': 2,
    '-1': "You didn't choose a direction.",
    "-2": False
}, {
    '0':
    "You come to a lake.\nThere is an island in the middle of the lake.\nYou can 'swim' across or 'wait' for a boat.",
    'swim': 3,
    'wait': 4,
    '-1': "You didn't choose to swim or wait.",
    '-2': False
}, {
    '-1': "You fall down a hole.",
    '-2': False
}, {
    '-1': "You Drown.",
    '-2': False
}, {
    '0':
    "You arrive at the island unharmed.\nThere is a house with 3 doors.\nOne red, one yellow and one blue.\nWhich colour do you choose?",
    'red': 5,
    'yellow': 6,
    'blue': 7,
    '-1': "You didn't choose a door.",
    '-2': False
}, {
    '-1': "You open the red door.\nYou burn to death.",
    '-2': False
}, {
    '-1': "You open the yellow door.\nYou find the treasure!",
    '-2': True
}, {
    '-1': "You open the blue door.\nYou freeze to death.",
    '-2': False
}]


def gameOver(reason, win):
    print(reason)
    if win == True:
        print("You Win!")
    else:
        print("You Lose!")
    print("Game Over")


def processGame(gameArray, index):
    choice = 'none'
    if '0' in gameArray[index]:
        choice = lowerInput(gameArray[index]['0'])
    if choice in gameArray[index]:
        processGame(gameArray, gameArray[index][choice])
    reason = "For some generic reason..."
    win = False
    if '-1' in gameArray[index]:
        reason = gameArray[index]['-1']
    if '-2' in gameArray[index]:
        win = gameArray[index]['-2']
    gameOver(reason, win)
    exit()


def start():
    processGame(gameArray, 0)


start()
