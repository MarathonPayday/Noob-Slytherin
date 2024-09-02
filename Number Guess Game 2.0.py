import random 

def get_positive_integer(prompt): #function definition 
    while True: #while true is infinate loop stops when we get valid input
        user_input = input(prompt) #prompt for user input 
        if user_input.isdigit() and int(user_input) > 0: #validate input, if userinput is a digit and if that digit is greatter than 0
            return int(user_input) # breaks the loop and exits the function. the value is sent back to get_pos_int2
        else: 
            print ('please enter a valid positive integer') #ask again if input invalid 

#get the upper limit from the user 
get_limit = get_positive_integer ('Enter a positive integer as the upper limit: ')

random_number  = random.randint(0, get_limit) #generate a number between 0 and limit 
guess = 0

while True: 
    guess += 1
    user_guess = get_positive_integer ('make a guess: ')
   
    if user_guess == random_number:
        print ('you win')
        break  
    
    elif user_guess > random_number:
        print('your guess is too high')

    else: 
        print('your guesss was too low')


print('you got it in', str(guess), 'guesses')
