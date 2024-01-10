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
You can go 'left' or 'right'""",
        'validCommands': {
            'left': 'At the lake',
            'right': 'At the chasm'
        }
    },
    'At the lake': {
        'chapterContent': """You come to a lake.
There is an island in the middle of the lake.
You can 'swim' across or 'wait' for a boat.""",
        'validCommands': {
            'swim': 'Drowned',
            'wait': 'At the island'
        }
    },
    'At the chasm': {
        'chapterContent': """You see a huge chasm in the ground, stretching to your left and right for as far as you can see.
The path seems to continue on the other side.
Maybe the bridge fell in?
You can 'leap' across or 'return' to the crossroad.""",
        'validCommands': {
            'leap': 'Fell into chasm',
            'return': 'At the crossroads'
        }
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
One 'red', one 'yellow' and one 'blue'.""",
        'prompt': "Which colour door do you choose to open?",
        'validCommands': {
            'red': 'At the red door',
            'yellow': 'At the yellow door',
            'blue': 'At the blue door'
        },
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

tomeOfManyMonsters = {
    'orc': {
        'name': 'Orc',
        'challenge': 30,
        'toughness': 10
    },
}



def lowerInput(prompt):
    return input(f"\n{prompt}\n> ").lower()


def processGameOver(book, reason, win, character):
    print(f"\n{reason}")
    print("Game Over")
    if win == True:
        print("You Win!")
    else:
        print("You Lose!")
    print(f"\nYour character ended at level {character['level']}")
    if character['gear']:
        print(f"With gear: {character['gear']}.")
    else:
        print("You did not have any gear!")
    if character['coins'] == 0:
        print("You were broke!")
    else:
        coin_word = "coin" if character['coins'] == 1 else "coins"
        print(f"You had {character['coins']} {coin_word}.")

import random

def levelUp(character):
    character['level'] += 1
    character['experience'] = 0
    print(f"Congratulations! Your character has leveled up to level {character['level']}")

def processFight(book, chapter, character):
    diceRolls = [random.randint(1, 100) for _ in range(character['level'])]
    highestRoll = max(diceRolls)
    challenge = tomeOfManyMonsters[book[chapter]['fight']]['challenge']
    toughness = tomeOfManyMonsters[book[chapter]['fight']]['toughness']
    print(f"\nYour character is at level {character['level']}, so you get to roll {character['level']} dice.")
    print(f"You need your highest roll - the enemy's toughness ({toughness}) to be greater than the enemy's challnge value of {challenge}.")
    print(f"\nYou rolled {diceRolls} and your highest roll is {highestRoll}")
    print(f"Your highest roll - toughness is {highestRoll - toughness}\n")
    if highestRoll - toughness >= challenge:
        print("You win the fight!")
        character['experience'] += 1
        if character['experience'] >= character['level'] * 3:
            levelUp(character)
        else:
            neededExperience = character['level'] * 3 - character['experience']
            point_word = "point" if neededExperience == 1 else "points"
            print(f"You need {neededExperience} more experience {point_word} to level up.")
        return 'win'
    else:
        return 'lose'

class QuitException(Exception):
    pass

def playBook(book, chapter, character):
    try:
        while True:
            print(f"\nChapter: {chapter}")
            if 'chapterContent' in book[chapter]:
                print(book[chapter]['chapterContent'])
            
            prompt_for_command = True
            if 'fight' in book[chapter]:
                result = processFight(book, chapter, character)
                if result in ['win', 'lose']:
                    chapter = book[chapter]['validCommands'].get(result)
                prompt_for_command = False

            if prompt_for_command:
                prompt = book[chapter].get('prompt', "What do you want to do?")
                command = lowerInput(prompt)
                if command == 'quit':
                    if lowerInput("Are you sure you want to quit? (y/n)") == 'y':
                        print("\nGoodbye!\n")
                        raise QuitException
                    else:
                        continue
                if command in book[chapter]['validCommands']:
                    chapter = book[chapter]['validCommands'].get(command)
                else:
                    print("Invalid command. Please try again.")
                    continue

            if 'gameEndReason' in book[chapter]:
                reason = book[chapter]['gameEndReason']
                win = book[chapter]['didTheyWin']
                processGameOver(book, reason, win, character)
                if lowerInput("Do you want to play again? (y/n)") != 'y':
                    print("\nGoodbye!\n")
                    break
                else:
                    chapter = book['start']  # Reset to the starting chapter
                    character = createCharacter()  # Create a new character
    except QuitException:
        pass

def startGame(book):
    character = createCharacter()
    startingChapter = book['start']
    playBook(book, startingChapter, character)

def createCharacter():
    return {
        'level': 1,
        'experience': 0,
        'gear': [],
        'coins': 0
    }
    
book = treasureIsland

startGame(book)
