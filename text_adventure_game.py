name = input("Hey type your name: ")
print("Hello " + name +" Welcome to my game!")

should_we_play = input("Do you want to play? ").lower()

if should_we_play == "y" or should_we_play == "yes":
    print("We are gonna play!")

    direction = input("Do you want to go left or right ?")
    if direction == "left":
        print("Okey we went left")
    elif direction == "right":
        choice = input("Okey, you now see a bridge, do you want to swim under it or cross it?")
        if choice == "swim":
            print("You got eaten by an alligator, you die, the end!")
        else:
            print("You found the gold and won!")
    else:
        print("Okay we went left")

else:
    print("We are NOT playing....")
