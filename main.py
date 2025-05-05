# File: main.py
#Name : Rishard Mohamed
#Student Number : 2495235

from game import Game

def main():
    game = Game()
    game.play()

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y" or play_again.lower() == "yes":
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()
