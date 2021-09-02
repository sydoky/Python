low = 1
high = 1000

def guess_binary(answer, low, high):
    guesses = 1 # that means initially our guesses is one. we start with a one.

    while True:
        guess=low+(high-low)//2 #a binary search formula to find out the mid point or guess

        if guess<answer:
            low=guess+1
        elif guess>answer:
            high=guess-1
        elif guess==answer:
            return guesses

        guesses+=1 #this line is going to count how many guesses computer needs to make the correct prediction for each number
for n in range(low, high+1): # we use high+1 because the last digit is always excluded, for example 1000 would be 999
    number_of_guesses=guess_binary(n, low, high)
    print("{} guessed in {}".format(n, number_of_guesses))


