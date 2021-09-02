low=1
high=1000

def guess_binary(answer,low,high):


     guesses=1

     while True:
         guess=low+(high-low)//2

         if guess<answer:
             low=guess+1
         elif guess>answer:
             high=guess-1
         elif guess==answer:

             return guesses

         guesses+=1

#Counting Correct guesses
correct_count=0
max_guesses=0

for number in range(low,high+1):
    number_of_guesses=guess_binary(number,low,high)
    print("{} guessed in {}".format(number,number_of_guesses))

    if number_of_guesses>max_guesses: # max_guesses is initially zero
        max_guesses,correct_count=number_of_guesses,1 # 1 is to update the correct_count variable
    elif number_of_guesses==max_guesses:
        correct_count+=1

print("I guesses without being told {} times.Max {}  guesses.".format(correct_count,max_guesses))
