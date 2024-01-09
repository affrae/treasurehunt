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
    'chapter':
    "You are at a crossroad.\nWhere do you want to go? Type 'left' or 'right'",
    'validCommands': {
        'left': 1,
        'right': 2
    },
    'gameEndReason': "You didn't choose a direction.",
    "-2": False
}, {
    'chapter':
    "You come to a lake.\nThere is an island in the middle of the lake.\nYou can 'swim' across or 'wait' for a boat.",
    'validCommands': {
        'swim': 4,
        'wait': 5
    },
    'gameEndReason': "You didn't choose to swim or wait.",
    'didTheyWin': False
}, {
    'chapter': "You see a huge chasm in the ground, stretching to your left and right for as far as you can see.\nThe path seems to continue on the other side.\nMaybe the bridge fell in?\nYou can 'leap' across or 'return' to the crossroad.",
    'validCommands': {
        'leap': 3,
        'return': 0
    },
    'gameEndReason': "You didn't choose to leap or return.",
    'didTheyWin': False
}, {
    'validCommands': {},
    'gameEndReason': "You fall down into what you now know to be a bottomless chasm.",
    'didTheyWin': False
},{
    'validCommands': {},
    'gameEndReason': "You Drown.",
    'didTheyWin': False
}, {
    'chapter':
    "You arrive at the island unharmed.\nThere is a house with 3 doors.\nOne red, one yellow and one blue.\nWhich colour do you choose?",
    'validCommands': {
        'red': 6,
        'yellow': 7,
        'blue': 8
    },
    'gameEndReason': "You didn't choose a door.",
    'didTheyWin': False
}, {
    'validCommands': {},
    'gameEndReason': "You open the red door.\nYou burn to death.",
    'didTheyWin': False
}, {
    'validCommands': {},
    'gameEndReason': "You open the yellow door.\nYou find the treasure!",
    'didTheyWin': True
}, {
    'validCommands': {},
    'gameEndReason': "You open the blue door.\nYou freeze to death.",
    'didTheyWin': False
}]


def processGameOver(reason, win):
    print(reason)
    if win == True:
        print("You Win!")
    else:
        print("You Lose!")
    print("Game Over")


def processGameStage(gameArray, index):
    command = 'none'
    if 'chapter' in gameArray[index]:
        command = lowerInput(gameArray[index]['chapter'])
        if command in gameArray[index]['validCommands']:
            processGameStage(gameArray, gameArray[index]['validCommands'][command])
    reason = "For some generic reason..."
    win = False
    if 'gameEndReason' in gameArray[index]:
        reason = gameArray[index]['gameEndReason']
    if 'didTheyWin' in gameArray[index]:
        win = gameArray[index]['didTheyWin']
    processGameOver(reason, win)
    exit()


def start():
    processGameStage(gameArray, 0)


start()
