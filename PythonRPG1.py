from multiprocessing.connection import wait
from time import time
from time import sleep
from timeit import repeat
from tkinter import W


classList = ["Paladin","Ranger","Mage","Summoner"]



player_name = input("What is your name?")
print(player_name.capitalize(), ", what a great name!")
sleep(2)
print("Okay ",player_name, ", what class would you like to be?",classList)
 
def classSelect():
    global playerClass
    playerClass = input("Class:")
    playerClass = playerClass
    if playerClass in classList:
        print(player_name.capitalize(),", you are the ",playerClass," we need you!")
    else: print("Pick a valid class from the list.",classList),classSelect()
classSelect()


inventoryPlayer = []
def gameStart():
    if playerClass == "Mage":
        mageStarter = ["Basic Wooden Wand","Basic Magical Robes","Basic Mage Boots","Iron Dagger"]
        inventoryPlayer.extend(mageStarter)
    elif playerClass == "Paladin":
        paladinStarter = ["Basic Wooden Tower Shield","Basic Iron Sword","Basic Iron Armor","Basic Holy Circlet"]
        inventoryPlayer.extend(paladinStarter)
    elif playerClass == "Summoner":
        summonerStarter = ["Basic Familiar Staff","Basic Magical Robes","Basic Mage Boots","Iron Dagger"]
        inventoryPlayer.extend(summonerStarter)
    elif playerClass == "Rogue":
        rogueStarter = ["Leather Armor","Leather Boots","Iron Dagger","Wooden Bow","Wooden Arrows"]
        inventoryPlayer.extend(rogueStarter)
gameStart()

print(inventoryPlayer)

exit()

def inventorySystem():
    if not inventoryPlayer:
        print("Your inventory is empty. Go get some items!")
    else: print(inventoryPlayer)






def youDied():
    print("Game over.")
    exit()



def startAdventure():
    Door1 = input("You see two doors. The right door is decaying and wet. The door on the left is demonic in nature. Which do you choose?")
    if Door1 == "left":
        choice1 = input("You see a demonic looking beast. It lunges at you. What do you do? [Run] [Fight]")
        if choice1 == "run":
            print("You got away.")
        elif choice1 == "fight":
            print("You tried to fight a demon. Yea, nice one. You were devoured."), youDied()
        else: print("Not sure what that was, but the beast didn't wait. You died."), youDied()
    elif Door1 == "right":
        print("Wah")
    else: print("Please choose left or right"), startAdventure()
startAdventure()

