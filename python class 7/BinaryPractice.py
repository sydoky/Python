low = 1
high = 1000

print('Please choose a number between {} and {} '.format(low, high))

guesses = 1

while True:
    guess = low+(high-low)//2  # a+b=c

    high_low = input('My guess is {}. Please enter h, l or c: '.format(guess)).casefold() # Pass the statement

    if high_low == 'h':
        low = guess + 1
    elif high_low == 'l':
        high = guess - 1
    elif high_low == 'c':
        print("You got the correct answer in {} guesses".format(guesses))  # Pass the statement
        break
    else:
        print('Please enter h, l or c') # Pass the statement
    guesses += 1  # or you can type "guesses = guesses + 1". It's called Augmented function