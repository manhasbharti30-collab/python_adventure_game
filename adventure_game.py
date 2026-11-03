# Python Adventure Game
# A text-based game where players explore
# different locations to find a hidden treasure.

print("Welcome to the Adventure Game!")
def forest_path(achievements):
    print("\nYou are walking through a dark forest.")
    print("You hear the sound of flowing water nearby.")

    print("\nWhat would you like to do?")
    print("1. Follow the river")
    print("2. Climb a tree")

    choice = input("\nEnter your choice: ")

    while choice not in ["1", "2"]:
        print("Invalid choice! Please enter 1 or 2.")
        choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\nYou follow the river and discover a hidden bridge!")
        print("You cross it and find the legendary treasure!")
        achievements.append("Found the treasure in the forest")
        print("\nCongratulations! YOU WIN!")

    elif choice == "2":
        print("\nYou climb the tree but lose your balance!")
        print("You fall and cannot continue your adventure.")
        print("\nGAME OVER!")

    else:
        print("\nInvalid choice!")
def cave_path(achievements):
    print("\nYou enter a mysterious cave.")
    print("It is extremely dark and you can hear strange noises.")

    print("\nWhat would you like to do?")
    print("1. Light a torch")
    print("2. Proceed in the dark")

    choice = input("\nEnter your choice: ")

    while choice not in ["1", "2"]:
        print("Invalid choice! Please enter 1 or 2.")
        choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\nYou light your torch and explore the cave.")
        print("You discover a secret passage!")
        print("Inside, you find the legendary treasure!")
        achievements.append("Found the treasure in the cave")
        print("\nCongratulations! YOU WIN!")

    elif choice == "2":
        print("\nYou walk blindly into the darkness.")
        print("You fall into a hidden pit!")
        print("\nGAME OVER!")

    else:
        print("\nInvalid choice!")
def start_game():
    achievements = []
    print("\n================================")
    print("       THE LOST TREASURE")
    print("================================")

    print("\nWelcome, brave explorer!")
    print("Your mission is to find a legendary treasure.")

    player_name = input("\nEnter your name: ")

    print("\nHello", player_name + "!")
    print("Your adventure begins now.")

    print("\nChoose your path:")
    print("1. Explore the dark forest")
    print("2. Enter the mysterious cave")

    choice = input("\nEnter 1 or 2: ")
    while choice not in ["1", "2"]:
        print("Invalid choice! Please choose 1 or 2.")
        choice = input("\nEnter 1 or 2: ")


    if choice == "1":
        forest_path(achievements)

    elif choice == "2":
        cave_path(achievements)

    else:
        print("\nInvalid choice! Please choose 1 or 2.")
    print("\n========== YOUR ACHIEVEMENTS ==========")

    if achievements:
        for achievement in achievements:
            print("🏆", achievement)
    else:
        print("No achievements unlocked this time!")

    print("=======================================")
play_again = "yes"

while play_again == "yes":
    start_game()

    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

    while play_again not in ["yes", "no"]:
        print("Please enter yes or no.")
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

print("\nThank you for playing The Lost Treasure!")
print("See you next time!")