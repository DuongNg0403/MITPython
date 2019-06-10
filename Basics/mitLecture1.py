cube = 0.5
epsilon = 0.01
num_guesses = 0
if cube >1 :
    low = 0
    high = cube
elif cube <= 1 and cube >=0:
    high = 1
    low = cube
guess = (high+low)/2
while abs(guess**3-cube) >= epsilon:
    if guess**3 > cube:
        high=guess
    else: low = guess
    guess = (high+low)/2
    num_guesses+=1
print(guess, " is close to the cube root of ", cube)
print("Number of guess: ", num_guesses)


