# how to use '',\ and "" in print statement,lower()
print("Welcome to Treasure land, Your mission is to find the treasure")
selection_1 = input("make a choice of left or right: ").lower()
if selection_1 == "right":
    print("Fall into the hole,Game over!")
else:
    selection_2 = input("choose one- swim or wait:").lower()
if selection_2 == "swim":
    print("Attacked by trout,Game over!")
elif selection_2 == "wait":
    #here \ is used to escape the single quote and it shows correctly in output
    #selection_3= input(print('you'\re moved in a boat and reached Island, choose the door, Red,Blue or Yellow:')).lower()
    selection_3 = input(
        'you\'re moved in a boat and reached Island, choose the door, Red,Blue or Yellow:').lower()
if selection_3 == "red":
    print("Flames are there,Gameover")
elif selection_3 == "blue":
    print("beasts are there,Game over")
elif selection_3 == "yellow":
    print("You found the treasure,You win!")
else:
    print("You chose a door that doesn't exist,Game over")
