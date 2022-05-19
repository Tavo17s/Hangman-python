# Write your code here
import random
wins = 0
losses = 0


def game_status():

    global wins, losses
    mode = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ').lower()
    print("")
    if mode == "play":
        play()
    elif mode == "results":
        print(f"You won: {wins} times")
        print(f"You lost: {losses} times\n")
        game_status()
    elif mode == "exit":
        exit()
    else:
        print("Please enter a valid option.")
        game_status()


def play():
    global losses, wins

    attempts = 8
    words = ["python", "java", "swift", "javascript"]
    aux_random_word = random.choice(words)

    result = list("-" * len(aux_random_word))  # we get the word with ----
    letters_set = set()  # it'll help us to valid the user's input, asking if the input was already entered

    while True:
        # for writing the selected word with --- and the user's guessed words
        for x in result:
            print(x, end="")

        print("")
        guess = input("Input a letter: ")
        # a list to store the indices where the user's guess matches the selected word
        indices = [i for i, x in enumerate(aux_random_word) if x == guess]

        if len(guess) != 1 or guess is None:
            print("Please, input a single letter.\n")
            continue
        elif not guess.isalpha() or guess.isupper():
            print("Please, enter a lowercase letter from the English alphabet.\n")
            continue

        if guess in letters_set:
            attempts -= 1
            print(f"You've already guessed this letter.\n")
            if attempts == 0:
                print("You lost!")
                losses += 1
                game_status()
            else:
                continue
        
        letters_set.add(guess)
        
        if len(indices) != 0:
            for idx in indices:
                result[idx] = guess
            print("")
            
        else:
            attempts -= 1
            print(f"That letter doesn't appear in the word.  #{attempts} attempts\n")

        word_joined = ''.join(result)

        if word_joined == aux_random_word:
            print(f"\nYou guessed the word {aux_random_word}!")
            print("You survived!")
            wins += 1
            game_status()
        elif attempts == 0:
            print("You lost!")
            losses += 1
            game_status()


if __name__ == "__main__":
    print("H A N G M A N  # 8 attempts\n")
    game_status()
