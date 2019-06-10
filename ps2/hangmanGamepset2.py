#Hangman
# Check user's input if user input is inappropriate returns a warning
# import file and randomize the secret word
# The full game
import hangmanFunc


def hangman(secret_word):
    '''
    The full game^^
    '''
    
    secret_word_list = hangmanFunc.split_char(secret_word)
    letter_guessed = []
    num_guesses = 6
    num_warnings = 3
    correct_guesses = 0
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long".format(len(secret_word)))
    #The body of the game (Loop)
    while num_guesses > 0:
        #Interface
        print(hangmanFunc.get_guessed_word(secret_word,letter_guessed))
        print(15*"_ ")
        print("You have {} guesses left".format(num_guesses))
        print("You have {} warnings left".format(num_warnings))
        print("Available letters:"+ str(hangmanFunc.get_available_letters(letter_guessed)))
        player_guess = str(input("Please guess a letter... ")).lower()
        #Hint call
        if player_guess == '*':
            print("Possible word matches are: {}".format(hangmanFunc.show_possible_matches(hangmanFunc.get_guessed_word(secret_word,letter_guessed))))
            continue
        #Check user's input and subtract warnings
        if num_warnings < 1:
            print("You are out of warnings, penalty is now applied")
            num_guesses -= 1
            if num_guesses > 0:
                continue
        elif not hangmanFunc.input_check(player_guess,letter_guessed):
            num_warnings-= 1
            continue
    
        letter_guessed.append(player_guess)

        #Check whether user guessed correctly
        if player_guess in secret_word_list:
            print("Good guess^^:")
            correct_guesses+=1

        elif player_guess in ["a", "e", "i", "o"] and not player_guess in secret_word_list:
            print("Oops! That letter is not in my word. You lose 2 guesses because it's a vowel :)))):")
            num_guesses-=2

        else:
            print("Oops! That letter is not in my word :):")
            num_guesses -=1                    
#TEST PASSED IT'S still working till now^^

        #Win condition
        if hangmanFunc.is_word_guessed(secret_word, letter_guessed):
            print("Congrats, you won!!!^^")
            print("The word was {}".format(secret_word))
            print("Your score is: {}".format(hangmanFunc.total_score(num_guesses, correct_guesses)))
            break
        if num_guesses <= 0:
            print("You lost, too bad the word was {} :)".format(secret_word))
    play_game = str(input("Input 1 to play again or anyother button otherwise..."))
    return play_game 
#TEST PASSED still working fine i guess   

def hangman_Call(a):
    if a == "1":
        ans = hangman(hangmanFunc.random_secret_word(hangmanFunc.use_file()))
        return hangman_Call(ans)
    else: print("End Game")

hangman_Call("1")    