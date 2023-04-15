#George Mi, CS30, March 
#This is a simple map for an RPG game

#Imports for all the different files used
import Inventory
import Map
import Combat

#This function detects if you are on the end tile with the keys, thus winning the game
def Win():
    if Map.row == 0 and Map.col == 3 and Inventory.Keys == True:
        Map.Loop = False
    elif Map.row == 0 and Map.col == 3 and Inventory.Keys == False:
        print("You find an empty escape pod but there's no key for the ignition")
        Map.Move()

#Introduction to situation
print(f"{Map.Tile_Descriptions[Map.layout[Map.row][Map.col]]['Description']}\n")
#This will loop the code until they win the game or quit
while Map.Loop == True:
   Inventory.Get_Item()
   Combat.combat()
   Map.Move()
   Win()