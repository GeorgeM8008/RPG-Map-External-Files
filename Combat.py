import Map

combat_stats = {
    "Player" : {
        "Attack" : 3,
        "Health" : 20 },
    "Enemy1" : {
        "Attack" : 2,
        "Health" : 9 },
    "Enemy2" : {
        "Attack" : 4,
        "Health" : 6 },
    "Enemy3" : {
        "Attack" : 2,
        "Health" : 9 },
    "Enemy4" : {
        "Attack" : 4,
        "Health" : 6 }
}
def combat():
    if Map.row == 0 and Map.col == 0:
        while combat_stats['Player']['Health'] > 0 and combat_stats['Enemy1']['Health'] > 0:
            print("Current health: " + str(combat_stats['Player']['Health']))
            print("Combat Options: Attack\n")
            choicec = input("Action: ")
            if choicec == "Attack":
                    print("\nYou deal 3 damage")
                    combat_stats['Enemy1']['Health'] -= combat_stats['Player']['Attack']
                    if combat_stats['Enemy1']['Health'] == 0:
                        print("You defeated the enemy\n")
                        break
                        Map.Move()
            else:
                print("I didn't understand that")
                combat()
            print("The alien swings and deals 4 damage to you\n")
            combat_stats['Player']['Health'] -= combat_stats['Enemy1']['Attack']
            if combat_stats['Player']['Health'] == 0:
                print("You have died\nYou lose")
                break
                Map.Loop = False
    elif Map.row == 1 and Map.col == 2:
        while combat_stats['Player']['Health'] > 0 and combat_stats['Enemy2']['Health'] > 0:
            print("Current health: " + str(combat_stats['Player']['Health']))
            print("Combat Options: Attack\n")
            choicec = input("Action: ")
            if choicec == "Attack":
                    print("\nYou deal 3 damage")
                    combat_stats['Enemy2']['Health'] -= combat_stats['Player']['Attack']
                    if combat_stats['Enemy4']['Health'] == 0:
                        print("You defeated the enemy\n")
                        break
                        Map.Move()
            else:
                print("I didn't understand that")
                combat()
            print("The alien swings and deals 4 damage to you\n")
            combat_stats['Player']['Health'] -= combat_stats['Enemy2']['Attack']
            if combat_stats['Player']['Health'] == 0:
                print("You have died\nYou lose")
                break
                Map.Loop = False
    elif Map.row == 2 and Map.col == 3:
        while combat_stats['Player']['Health'] > 0 and combat_stats['Enemy3']['Health'] > 0:
            print("Current health: " + str(combat_stats['Player']['Health']))
            print("Combat Options: Attack\n")
            choicec = input("Action: ")
            if choicec == "Attack":
                    print("\nYou deal 3 damage")
                    combat_stats['Enemy3']['Health'] -= combat_stats['Player']['Attack']
                    if combat_stats['Enemy3']['Health'] == 0:
                        print("You defeated the enemy\n")
                        break
                        Map.Move()
            else:
                print("I didn't understand that")
                combat()
            print("The alien swings and deals 2 damage to you\n")
            combat_stats['Player']['Health'] -= combat_stats['Enemy3']['Attack']
            if combat_stats['Player']['Health'] == 0:
                print("You have died\nYou lose")
                break
                Map.Loop = False
    elif Map.row == 3 and Map.col == 2:
        while combat_stats['Player']['Health'] > 0 and combat_stats['Enemy4']['Health'] > 0:
            print("Current health: " + str(combat_stats['Player']['Health']))
            print("Combat Options: Attack\n")
            choicec = input("Action: ")
            if choicec == "Attack":
                    print("\nYou deal 3 damage")
                    combat_stats['Enemy4']['Health'] -= combat_stats['Player']['Attack']
                    if combat_stats['Enemy4']['Health'] == 0:
                        print("You defeated the enemy\n")
                        break
                        Map.Move()
            else:
                print("I didn't understand that")
                combat()
            print("The alien swings and deals 4 damage to you\n")
            combat_stats['Player']['Health'] -= combat_stats['Enemy4']['Attack']
            if combat_stats['Player']['Health'] == 0:
                print("You have died\nYou lose")
                break
                Map.Loop = False