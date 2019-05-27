#Check if word is guessed returns True or False
def split_char(string): #time complexity: O(len(L)) + space complexity len(L)
    '''
    Split strings into list of characters
    '''
    L = []
    for char in string:
        L.append(char)
    return L

def is_word_guessed(secret_word, letter_guessed):
#O(len(splitted)*len(letter_guessed + len(splitted))) = O(n*n)   
    '''
    Returns True if word is guessed, False if not
    '''
    splitted= split_char(secret_word)
    if all(x in letter_guessed for x in splitted):
        return True
    return False
#TEST PASSED
#word = "hello"
#guessed = ['e','i','h','o','g','']
#print(is_word_guessed(word,guessed)) 
   
def get_guessed_word(secret_word, letter_guessed):#O(n*n)
    '''Returns a string with underscore for letters that are not guessed
    '''
    splitted = split_char(secret_word)
    guess_result = []
    for i in splitted:
        if i in letter_guessed:
            guess_result.append(i)
        else: guess_result.append("_")
    str_result = " ".join(guess_result)
    return str_result
#TEST PASSED 
#print(get_guessed_word(word, guessed))

def get_available_letters(letter_guessed):
    '''
    Returns a string comprised of letters that is not in letter guessed
    '''
    import string
    all_lowercase = string.ascii_lowercase
    split_lower = split_char(all_lowercase)
    for char in letter_guessed:
        if char in split_lower:
            split_lower.remove(char)
    lowercase_left = "".join(split_lower)
    return lowercase_left
#TEST PASSED
#print(get_available_letters(guessed))

#input check function
def input_check(player_guess, letter_guessed):
    '''
    Check user's input, returns a boolean
    '''
    import string
    if len(str(player_guess)) != 1:
        print("Guess 1 character at a time pls .-.")
        return False
    elif not str(player_guess).isalpha():
        print("Your input should be {} only".format(string.ascii_letters)) 
        return False
    elif player_guess in letter_guessed:
        print("You've already guessed this letter")
        return False
    else:
        return True

def total_score(guesses_remaining,unique_letters):
    '''
    Calculate score if you win by multipling 2 parameters
    '''
    return guesses_remaining*unique_letters

def use_file():
    '''
    Use the file words.txt to generate hangman secret word'''
    print("Loading wordlist from file ... ")
    
    word_file = open("words.txt" ,"r")
    words = word_file.readline() #word is string
    word_list = words.split()
    print("{} words loaded".format(len(word_list)))
    return word_list

def random_secret_word(word_list):
    '''
    Choose a random word in word_list
    '''
    import random
    return random.choice(word_list)