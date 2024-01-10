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

treasureIsland = {
    'start': 'At the crossroads',
    'At the crossroads': {
        'chapterContent': """You are at a crossroad.
Where do you want to go? Type 'left' or 'right'""",
        'validCommands': {
            'left': 'At the lake',
            'right': 'At the chasm'
        },
        'gameEndReason': "You didn't choose a direction.",
        'didTheyWin': False
    },
    'At the lake': {
        'chapterContent': """You come to a lake.
There is an island in the middle of the lake.
You can 'swim' across or 'wait' for a boat.""",
        'validCommands': {
            'swim': 'Drowned',
            'wait': 'At the island'
        },
        'gameEndReason': "You didn't choose to swim or wait.",
        'didTheyWin': False
    },
    'At the chasm': {
        'chapterContent': """You see a huge chasm in the ground, stretching to your left and right for as far as you can see.
The path seems to continue on the other side.
Maybe the bridge fell in?
You can 'leap' across or 'return' to the crossroad.""",
        'validCommands': {
            'leap': 'Fell into chasm',
            'return': 'At the crossroads'
        },
        'gameEndReason': "You didn't choose to leap or return.",
        'didTheyWin': False
    },
    'Fell into chasm': {
        'validCommands': {},
        'gameEndReason': "You fall down into what you now know to be a bottomless chasm.",
        'didTheyWin': False
    },
    'Drowned': {
        'validCommands': {},
        'gameEndReason': "You Drown.",
        'didTheyWin': False
    },
    'At the island': {
        'chapterContent': """You arrive at the island unharmed.
There is a house with 3 doors.
One red, one yellow and one blue.
Which colour do you choose?""",
        'validCommands': {
            'red': 'At the red door',
            'yellow': 'At the yellow door',
            'blue': 'At the blue door'
        },
        'gameEndReason': "You didn't choose a door.",
        'didTheyWin': False
    },
    'At the red door': {
        'validCommands': {},
        'gameEndReason': "You open the red door.\nYou burn to death.",
        'didTheyWin': False
    },
    'At the yellow door': {
        'chapterContent': """You walk up to the yellow door.
All over a sudden an Orc rushes out from a nearby bush and tries to attack you!
You can 'fight' or 'retreat'.""",        
        'validCommands': {
            'fight': 'Fight the orc',
            'retreat': 'At the island'
        },
        'gameEndReason': "You did not choose to fight or retreat.",
        'didTheyWin': False
    },
    'At the blue door': {
        'validCommands': {},
        'gameEndReason': "You open the blue door.\nYou freeze to death.",
        'didTheyWin': False
    },
    'Fight the orc': {
        'chapterContent': """You decide to fight the orc.
Have at it!!!""",
        'fight': 'orc',
        'validCommands': {
            'win': 'You beat the orc!',
            'lose': 'The orc beats you!'
        },
    },
    'You beat the orc!': {
        'chapterContent': """You beat the orc and they run away.
You can 'open' the yellow door or 'return' to the island.""",
        'validCommands': {
            'open': 'Open the yellow door',
            'return': 'At the island'
        },
        'gameEndReason': "You didn't choose to open or return.",
        'didTheyWin': False
    },
    'The orc beats you!': {
        'validCommands': {},
        'gameEndReason': "You lose the fight and die.",
        'didTheyWin': False
    },
    'Open the yellow door': {
        'validCommands': {},
        'gameEndReason': """You open the yellow door.
Inside you find a treasure chest.
You open it and find a pile of gold!""",
        'didTheyWin': True
    }
}

monsters = {
    'orc': {
        'name': 'Orc',
        'baseChance': 70,
        'toughness': 10
    },
}



def lowerInput(prompt):
    return input(f"\n{prompt}\n> ").lower()


def processGameOver(book, reason, win, character):
    print(f"\n{reason}\n")
    if win == True:
        print("You Win!")
    else:
        print("You Lose!")
    print(f"Your character ended at level {character['level']} with gear: {character['gear']}")
    print("Game Over")

import random

def levelUp(character):
    character['level'] += 1
    character['experience'] = 0
    print(f"Congratulations! Your character has leveled up to level {character['level']}")

def processFight(book, chapter, character):
    diceRolls = [random.randint(1, 100) for _ in range(character['level'])]
    lowestRoll = min(diceRolls)
    baseChance = monsters[book[chapter]['fight']]['baseChance']
    toughness = monsters[book[chapter]['fight']]['toughness']
    print(f"Your character is at level {character['level']}, so you get to roll {character['level']} dice.")
    print(f"You need your lowest roll + the enemy's toughness ({toughness}) to be less than {baseChance} percent.")
    print(f"You rolled {diceRolls} and your lowest roll is {lowestRoll}")
    print(f"Your lowest roll + toughness is {lowestRoll + toughness}")
    if lowestRoll + toughness <= baseChance:
        character['experience'] += 1
        if character['experience'] >= character['level'] * 3:
            levelUp(character)
        else:
            neededExperience = character['level'] * 3 - character['experience']
            print(f"You need {neededExperience} more experience points to level up.")
        return 'win'
    else:
        return 'lose'

def playBook(book, chapter, character):
    while True:
        while True:
            if 'fight' in book[chapter]:
                chapterContent = book[chapter].get('chapterContent')
                if chapterContent:
                    print(f"\n{chapterContent}\n")
                result = processFight(book, chapter, character)
                if result == 'win':
                    chapter = book[chapter]['validCommands'].get('win')
                elif result == 'lose':
                    chapter = book[chapter]['validCommands'].get('lose')
                continue
            elif 'chapterContent' in book[chapter]:
                command = lowerInput(book[chapter]['chapterContent'])
                nextChapter = book[chapter]['validCommands'].get(command)
                if nextChapter:
                    chapter = nextChapter
                    continue
            reason = "For some generic reason..."
            win = False
            if 'gameEndReason' in book[chapter]:
                reason = book[chapter]['gameEndReason']
            if 'didTheyWin' in book[chapter]:
                win = book[chapter]['didTheyWin']
            processGameOver(book, reason, win, character)
            break
        if lowerInput("Do you want to play again? (y/n)") != 'y':
            print("\nGoodbye!\n")
            break
        else:
            chapter = 'At the crossroads'  # Reset to the starting chapter
            character = createCharacter()  # Create a new character

def startGame(book):
    character = createCharacter()
    startingChapter = book['start']
    playBook(book, startingChapter, character)

def createCharacter():
    return {
        'level': 1,
        'experience': 0,
        'gear': []
    }
    
book = treasureIsland

startGame(book)
