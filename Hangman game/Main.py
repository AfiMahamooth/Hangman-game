import random
from Class_Hangman import play
from Class_files.PlayerCopy import playerCopy as pl


# This program runs a command console game of hangman.It will take a list of words from a text document given.
# store those words in an array,
# It will then randomly pick an element from that array and that would be the word the player will get.
# The player will loop the game until the player decides to quit.
# when the player quits it will return back to the console players name, wins & losses.


def get_list():
    """ gets words from text file into the list"""
    with open("20 Words.txt") as txt_file:  # opens the text file that has words
        wl = [line.rstrip() for line in txt_file]  # this stores each line into a list
    return wl


def get_word(wl):
    """gets random word from list"""
    word = random.choice(wl)
    return word.upper()


def win_loss(wins, loss):
    """returns percentages"""
    percent = float(wins / loss)
    return ("****Thanks for playing****")


def main():
    """plays the game"""
    wl = get_list()
    wins = 0  # wins variable
    loss = 0  # loss Variable
    game_count = 1
    name = str(input("What is your name? "))  # gets name of user and sets it to the variable
    playerCopy = pl.Player(name)  # sets player class
    print(playerCopy.display())  # displays player class before running the game
    while input("play hangman? (y/n)").upper() == "Y":  # Loop of the game
        word = get_word(wl)
        guessed = play(word)
        # these decision statements will add to either wins or losses depending on how the game goes.
        if guessed:
            wins += 1
            print("Great you guessed the word", word, ".\n")
            playerCopy.update_wins(wins)
        else:
            loss += 1
            print("Sorry the word was", word, ".\n")
            playerCopy.update_loss(loss)
        game_count += 1

    print(playerCopy.display(), win_loss(wins, game_count))  # displays win and losses


if __name__ == "__main__":
    main()
