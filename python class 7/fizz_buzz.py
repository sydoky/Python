def fizz_buzz(number:int)->str:
    if number%3==0:
        return 'fizz'
    elif number%5==0:
        return 'buzz'
    elif number%15==0:
        return 'fizz buzz'
    else:
        return str(number)

input("Please start the game by pressing Enter")

next_number = 0

while next_number<100:
    next_number+=1 # this becomes 1
    print(fizz_buzz(next_number))  # we are calling our function and providing the next number is as an argument
    next_number+=1 #this becomes 2
    correct_answer = fizz_buzz(next_number)
    player_answer = input("Your turn: ")
    if correct_answer != player_answer:
        print("Sorry, you lost the game. The correct answer was {}".format(correct_answer))
        break
else:
    print("You completed the whole game. Congrats!")

