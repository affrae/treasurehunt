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
print('''\nREMEBMER: You can type:
- 'search' to search the area you are in for items.
- 'inventory' to see what items you have.
- 'quit' to quit the game.
''')

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

treasureIsland = {
    'start': 'At the crossroads',
    'chapters': {
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
You can 'swim' across or 'wait' for a boat.
You can also 'return' to the crossrowds""",
            'validCommands': {
                'swim': 'Drowned',
                'wait': 'At the dock',
                'return': 'At the crossroads'
            },
            'search':{
                'rusty sword': "In the mud by the lake you find a rusty sword.",
                'found': False
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
            },
            'search': {
                'coinsText': """Under some long-ago dried up manure...""",
                'coins': 10,
                'found': False
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
        'At the dock': {
            'chapterContent': """You pull up at the dock and arrive at the island unharmed.
There is a house with 5 doors.
One 'red', one 'yellow', one 'green', one 'purple' and one 'blue'.""",
            'prompt': "Which colour door do you choose to open?",
            'validCommands': {
                'red': 'At the red door',
                'yellow': 'At the yellow door',
                'blue': 'At the blue door',
                'purple': 'At the purple door',
                'green': 'At the green door'
            },
        },
        'Return to the dock': {
            'chapterContent': """You return back to the dock.
There is a house with 5 doors.
One 'red', one 'yellow', one 'green', one 'purple' and one 'blue'.""",
            'prompt': "Which colour door do you choose to open?",
            'validCommands': {
                'red': 'At the red door',
                'yellow': 'At the yellow door',
                'blue': 'At the blue door',
                'purple': 'At the purple door',
                'green': 'At the green door'
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
                'retreat': 'Return to the dock'
            },
        },
        'At the green door': {
            'validCommands': {},
            'autoFind': {
                'coinsText': """Inside you find a treasure chest.
You open it and find a pile of gold coins.""",
                'coins': 10,
                'found': False
            },
            'gameEndReason': """You open the green door.""",
            'didTheyWin': True
        },
        'At the purple door': {
            'chapterContent': """You walk up to the purple door,
remembering that when you are done with this door your options are
to pick another colour door ('red', 'blue', 'yellow' or 'green') or 'return' to the dock.""",
            'validCommands': {
                'return': 'Return to the dock',
                'blue': 'At the blue door',
                'yellow': 'At the yellow door',
                'red': 'At the red door',
                'green': 'At the green door'
                },
            'autoFind': {
                'shiny sword': "Inside you find a treasure chest.\nYou open it and find a shiny sword.",
                'found': False
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
You can 'open' the yellow door or 'return' to the dock.""",
            'validCommands': {
                'open': 'Open the yellow door',
                'return': 'Return to the dock'
            },
        },
        'The orc beats you!': {
            'validCommands': {},
            'gameEndReason': "You lose the fight and die.",
            'didTheyWin': False
        },
        'Open the yellow door': {
            'validCommands': {},
            'autoFind': {
                'coinsText': """Inside you find a treasure chest.
You open it and find a pile of gold coins.""",
                'coins': 1000,
                'rusty sword': 'You find a rusty sword.',
                'found': False
            },
            'gameEndReason': """You open the yellow door.""",
            'didTheyWin': True
        }
    },
    'tomeOfManyMonsters': {
        'orc': {
            'name': 'Orc',
            'challenge': 30,
            'toughness': 10
        },
    },
    'codexOfManyItems' : {
        'rusty sword': {
            'name': 'Rusty Sword',
            'damage': 10
        },
        'shiny sword': {
            'name': 'Shiny Sword',
            'damage': 20
        }
    }
}



def lowerInput(prompt):
    return input(f"\n{prompt}\n> ").lower()


def processGameOver(book, chapter, character):
    reason = book['chapters'][chapter]['gameEndReason']
    win = book['chapters'][chapter]['didTheyWin']
    print(f"\n{reason}")
    if 'autoFind' in book['chapters'][chapter] and 'found' in book['chapters'][chapter]['autoFind'] and not book['chapters'][chapter]['autoFind']['found']:
        book['chapters'][chapter]['autoFind']['found'] = True
        for item in book['chapters'][chapter]['autoFind']:
            if item == 'coinsText' or item == 'found':
                continue
            if item == 'coins':
                coin_count = book['chapters'][chapter]['autoFind']['coins']
                coin_word = "coin" if coin_count == 1 else "coins"
                if 'coinsText' in book['chapters'][chapter]['autoFind']:
                    print(f"\n{book['chapters'][chapter]['autoFind']['coinsText']}")
                print(f"\nYou find {coin_count} {coin_word}")
                character['coins'] += book['chapters'][chapter]['autoFind'][item]
            elif item not in character['inventory']:
                print(f"\n{book['chapters'][chapter]['autoFind'][item]}")
                print(f"You add this {item} to your inventory.")
                print(f"I wonder if it might have been useful earlier?")
                character['inventory'].append(item)
            else:
                print(f"\n{book['chapters'][chapter]['autoFind'][item]}")
                print("But you can only carry one of those and you already have this item.")
    elif 'autoFind' in book['chapters'][chapter] and 'found' in book['chapters'][chapter]['autoFind']:
        print("\nYou find nothing more.") 
    print("\nGame Over")
    if win == True:
        print("You Win!")
    else:
        print("You Lose!")
    print(f"\nYour character achieved level {character['level']}")
    handle_inventory(None, None, character)


import random

def levelUp(character):
    character['level'] += 1
    character['experience'] = 0
    print(f"Congratulations! Your character has leveled up to level {character['level']}")

def processFight(book, chapter, character):
    diceRolls = [random.randint(1, 100) for _ in range(character['level'])]
    highestRoll = max(diceRolls)
    challenge = book['tomeOfManyMonsters'][book['chapters'][chapter]['fight']]['challenge']
    toughness = book['tomeOfManyMonsters'][book['chapters'][chapter]['fight']]['toughness']
    print(f"\nYour character is at level {character['level']}, so you get to roll {character['level']} dice.")
    print(f"You need your (highest roll + the highest damage any of your weapons can provide) - the enemy's toughness ({toughness}) to be greater than the enemy's challenge value of {challenge}.")

    # Search the character's gear for items with a 'damage' key
    highestDamage = 0
    highestDamageItem = None
    for item_name in character['inventory']:
        if item_name in book['codexOfManyItems']:
            if 'damage' in book['codexOfManyItems'][item_name]:
                if book['codexOfManyItems'][item_name]['damage'] > highestDamage:
                    highestDamage = book['codexOfManyItems'][item_name]['damage']
                    highestDamageItem = item_name

    if highestDamage > 0:
        print(f"Your {highestDamageItem} is your best weapon and adds {highestDamage} to your roll.")

    print(f"\nYou rolled {diceRolls} and your highest roll is {highestRoll}")
    print(f"Your (highest roll ({highestRoll}) + damage ({highestDamage})) - toughness ({toughness}) is {highestRoll + highestDamage - toughness}\n")
    if highestRoll + highestDamage - toughness >= challenge:
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

def handle_search(book, chapter, character):
    if 'search' in book['chapters'][chapter] and 'found' in book['chapters'][chapter]['search'] and not book['chapters'][chapter]['search']['found']:
        book['chapters'][chapter]['search']['found'] = True
        for item in book['chapters'][chapter]['search']:
            if item == 'coinsText' or item == 'found':
                continue
            if item == 'coins':
                coin_count = book['chapters'][chapter]['search']['coins']
                coin_word = "coin" if coin_count == 1 else "coins"
                if 'coinsText' in book['chapters'][chapter]['search']:
                    print(f"\n{book['chapters'][chapter]['search']['coinsText']}")
                print(f"\nYou find {coin_count} {coin_word}")
                character['coins'] += book['chapters'][chapter]['search'][item]
            elif item not in character['inventory']:
                print(f"\n{book['chapters'][chapter]['search'][item]}")
                print(f"You add this {item} to your inventory.")
                print(f"I wonder if it might have been useful earlier?")
                character['inventory'].append(item)
            else:
                print(f"\n{book['chapters'][chapter]['search'][item]}")
                print("But you can only carry one of those and you already have this item.")
    else:
        print("\nYou find nothing.")

def handle_inventory(book, chapter, character):
    if character['inventory']:
        print("\nYou have the following items:")
        for item in character['inventory']:
            print(f"- {item}")
    else:
        print("\nYou have no items.")
    if character['coins'] > 0:
        coin_word = "coin" if character['coins'] == 1 else "coins"
        print(f"\nYou have {character['coins']} {coin_word}.")
    else:
        print("\nYou are broke!")
    
def handle_quit(book, chapter, character):
    if lowerInput("\nAre you sure you want to quit? (y/n)") == 'y':
        print("\nGoodbye!\n")
        raise QuitException

def handle_invalid_command(book, chapter, character):
    print("\nInvalid command. Please try again.")

command_handlers = {
    'search': handle_search,
    'inventory': handle_inventory,
    'quit': handle_quit,
    'invalid': handle_invalid_command,
}

def playBook(book, chapter, character):
    try:
        while True:
            # print(f"\nChapter: {chapter}: {book['chapters'][chapter]}")
            print(f"\nChapter: {chapter}")
            if 'chapterContent' in book['chapters'][chapter]:
                print(book['chapters'][chapter]['chapterContent'])
            if 'autoFind' in book['chapters'][chapter] and 'found' in book['chapters'][chapter]['autoFind'] and not book['chapters'][chapter]['autoFind']['found']:
                book['chapters'][chapter]['autoFind']['found'] = True
                for item in book['chapters'][chapter]['autoFind']:
                    if item == 'coinsText' or item == 'found':
                        continue
                    if item == 'coins':
                        coin_count = book['chapters'][chapter]['autoFind']['coins']
                        coin_word = "coin" if coin_count == 1 else "coins"
                        if 'coinsText' in book['chapters'][chapter]['autoFind']:
                            print(f"\n{book['chapters'][chapter]['autoFind']['coinsText']}")
                        print(f"\nYou find {coin_count} {coin_word}")
                        character['coins'] += book['chapters'][chapter]['autoFind'][item]
                    elif item not in character['inventory']:
                        print(f"\n{book['chapters'][chapter]['autoFind'][item]}")
                        print(f"You add this {item} to your inventory.")
                        print(f"I wonder if it might have been useful earlier?")
                        character['inventory'].append(item)
                    else:
                        print(f"\n{book['chapters'][chapter]['autoFind'][item]}")
                        print("But you can only carry one of those and you already have this item.")
            elif 'autoFind' in book['chapters'][chapter] and 'found' in book['chapters'][chapter]['autoFind']:
                print("\nYou find nothing more.")          

            prompt_for_command = True
            if 'fight' in book['chapters'][chapter]:
                result = processFight(book, chapter, character)
                if result in ['win', 'lose']:
                    chapter = book['chapters'][chapter]['validCommands'].get(result)
                    if result == 'win':
                        # print(f"\nChapter: {chapter}: {book['chapters'][chapter]}")
                        print(f"\nChapter: {chapter}")
                        if 'chapterContent' in book['chapters'][chapter]:
                            print(book['chapters'][chapter]['chapterContent'])
                    elif result == 'lose':
                        prompt_for_command = False

            if prompt_for_command:
                prompt = book['chapters'][chapter].get('prompt', "What do you want to do?")
                command = lowerInput(prompt)
                if command in book['chapters'][chapter]['validCommands']:
                    chapter = book['chapters'][chapter]['validCommands'].get(command)
                else:
                    handler = command_handlers.get(command, command_handlers['invalid'])
                    handler(book, chapter, character)

            if 'gameEndReason' in book['chapters'][chapter]:
                # print(f"\nChapter: {chapter}: {book['chapters'][chapter]}")
                print(f"\nChapter: {chapter}")
                processGameOver(book, chapter, character)
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
        'inventory': [],
        'coins': 0
    }
    
import copy

book = copy.deepcopy(treasureIsland)
startGame(book)
