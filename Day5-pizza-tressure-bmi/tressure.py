print(f"welcome to the tressure")
ways=str(input("where you want to go,Type 'left' or 'right' ")).lower()
if(ways=='left'):
    print("you are reached the island,there was a lake")
    choice=str(input("did u want to 'swim' or 'wait'"))
    if(choice=='wait'):
        print(f"you are now safe")
        color=str(input("enter a color"))
        if(color=='yellow'):
            print("win")
        else:
            print("game over")
    else:
        print(f"game over")
    
else:
    print("game over")
