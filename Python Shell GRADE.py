#please download wordslist.txt from our folder

def generate_random_word():
    #from https://www.hangmanwords.com/words
    import random
    lines = open("wordslist.txt").readlines()
    line = lines[0]
    listofwords = line.split()
    word = random.choice(listofwords)
    return word

def print_word(word, guessed_letter, guessed_letters):
    listed_letters = list(word)
    displayed_word = ""
    for letter in listed_letters:
        if letter in guessed_letters:
            displayed_word = displayed_word + " " + letter
        else:
            displayed_word = displayed_word + " __"
    print(displayed_word)
    return displayed_word

def win(word, guessed_letters):
    listed_letters = list(word)
    displayed_word = ""
    for letter in listed_letters:
        if letter in guessed_letters:
            displayed_word = displayed_word + " " + letter
        else:
            displayed_word = displayed_word + " __"
    if " __" not in displayed_word:
        winner = "yes"
    else:
        winner = "no"
    return winner

def lose_print_word(word, guessed_letters):
    listed_letters = list(word)
    displayed_word = ""
    for letter in listed_letters:
        if letter in guessed_letters:
            displayed_word = displayed_word + " " + letter
        else:
            displayed_word = displayed_word + " _" + letter + "_ "
    print(displayed_word)
    return word

def play_hangman():
    winner = "no"
    want_to_play = True
    while (want_to_play):
        guessed_letters = []
        guesses_left = 6
        word = str(generate_random_word())
        print("__ "*len(word))
        letter = input("Guess letter:")
        done = False
        while not done:
            if letter in guessed_letters:
                guesses_left = guesses_left - 1
                print("You already guessed", letter)
            elif letter not in word:
                guessed_letters.append(letter)
                guesses_left = guesses_left - 1
                winner = win(word, guessed_letters)
                print(letter, "is not in the word.")
            else:
                guessed_letters.append(letter)
                winner = win(word, guessed_letters)
                print(letter, "is in the word.")
            if winner == "yes":
                done = True
                print("CONGRATULATIONS! You won the game.")
                print_word(word, letter, guessed_letters)
            elif guesses_left == 0:
                done = True
                print("Sorry! You ran out of guesses. You lose.")
                lose_print_word(word, guessed_letters)
            else:
                print_word(word, letter, guessed_letters)
                letter = input("Guess letter:")
        want_to_play = input("Play another round of hangman? Y/N")
        if want_to_play == "Y":
            want_to_play = True
        else:
            want_to_play = False

play_hangman()
