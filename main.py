#George Mi, CS30, March 
#This is a simple map for an RPG game

import Inventory
import Map

#These are variables of the different rooms in the lists below

Loop = True
Keys = False
#This function detects if you are in a room with an item and gives the choice to pick it up
def Get_Item():
    global Keys
    if Map.row == 0 and Map.col == 1:
        choice3 = input("Choice: ")
        if choice3 == "Yes":
            Inventory.inventory.append("Medkit")
            print("\nYou picked up the Medkit\n")
            Map.Move()
        elif choice3 == "No":
            print("\nYou did not pick up the Medkit\n")
            Map.Move()
        else:
            print("\nI didn't understand that")
            Get_Item()
    elif Map.row == 2 and Map.col == 2:
        choice4 = input("Choice: ")
        if choice4 == "Yes":
            Inventory.inventory.append("Keys")
            print("\nYou picked up the keys\n")
            Keys = True
            Map.Move()
        elif choice4 == "No":
            print("\nYou did not pick up the keys\n")
            Map.Move()
layout = [['Enemy Room', 'Supply Room', 'Safe Room', 'Escape Pod'],
          ['Safe Room',  'Safe Room',  'Enemy Room', 'Safe Room'],
          ['Safe Room',  'Safe Room',  'Janitor Closet',  'Enemy Room'],
          ['Starting Room', 'Safe Room', 'Enemy Room', 'Safe Room'],]
#Nested dictionaries describing the rooms and their effects
Tile_Descriptions = {
    "Safe Room" : {
        "Description" : "You enter an empty room",
        "Effect" : "You ponder your next actions" },
    "Starting Room" : {
        "Description" : "You find yourself on an enemy ship and must escape"},
    "Enemy Room" : {
        "Description" : "You enter room with an enemy inside",
        "Effect" : "You lose 2 health" },
    "Escape Pod" : {
        "Description" : "You find a lone escape pod at the end of the ship",
        "Effect" : "You win" },
    "Supply Room" : {
        "Description" : "You find a small storage room with a Medkit hanging on the wall",
        "Effect" : "Do you choose to pick it up?" },
    "Janitor Closet" : {
        "Description" : "You find a small janitor's closet with a pair of keys dangling off a key hook",
        "Effect" : "Do you choose to pick it up?",
    }
}
#This function detects if you are on the end tile with the keys, thus winning the game
def Win():
    global Loop, Keys
    if Map.row == 0 and Map.col == 3 and Keys == True:
        Loop = False
    elif Map.row == 0 and Map.col == 3 and Keys == False:
        print("You find an empty escape pod but there's no key for the ignition")
        Map.Move()

#Introduction to situation
print(f"{Map.Tile_Descriptions[Map.layout[Map.row][Map.col]]['Description']}\n")
#This will loop the code until they win the game or quit
while Loop == True:
   Get_Item()
   Map.Move()
   Win()