# import random
#
# answer = random.randint(1, 20)
#
# your_guess = 0
#
# while your_guess != answer:
#     your_guess = int(input('Please, make your guess: '))
#     if your_guess == answer:
#         print("Congrats! You are the winner!")
#         break
#     else:
#         if your_guess > answer:
#             print("You need to lower your guesses")
#         else:
#             print("You need to higher your guesses")

#
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





# answer = 10
# guess = int(input("Please, make your guess: "))
#
# if answer == guess:
#     print("Congrats! Your are correct!")
# else:
#     if guess != answer:
#         guess = int(input("Please, make another guess: "))
#         if guess == answer:
#             print("You are correct at second time")
#         else:
#             print("You are lost again")



#
# name = input('Please, enter your name: ')
# age = int(input("Also enter your age: "))
#
# if age >= 31 or age <= 18:
#     print("You are not allowed to the party")
# else:
#     print("Welcome to the party, " + name + "!")

#
# if age>=18 and age<=50: # When we use 'and,' all conditions have to be True
#     print("Bravo")
# else:
#     print("Good day")
#
# if age>=18 or age<=50: # When we use 'or,' only one condition has to be true
#     print("Bravo")
# else:
#     print("Good day")


# word = "American Computer"
#
# letter = input("Please, enter your character: ")
#
# if letter in word:
#     print("{} is in {}".format(letter, word))
# else:
#     print("Sorry, that character is not in the word")


# activity = input("What would you like to do today? ")
# if 'cinema' not in activity.casefold():  # casefold will convert all upper letters into lower cases
#     print('but I would like to go for the cinema')
# else:
#     print('Enjoy')
#
# activity = input("What would you like to do today? ")
# if 'cinema' not in activity.lower():  # casefold will convert all upper letters into lower cases
#     print('but I would like to go for the cinema')
# else:
#     print('Enjoy')
#
# activity = input("What would you like to do today? ")
# if 'cinema' not in activity.upper():  # casefold will convert all upper letters into lower cases
#     print('but I would like to go for the cinema')
# else:
#     print('Enjoy')


# for i in range(1, 11):
#     print('I love milk {}'.format(i))
#
#
# word = "Computer science"
# for i in word:
#     print(i)
#
# for i in range(len(word)):
#     print('The index number of {} is {}'.format(word[i], i))
#

# keyword continue . We use continue to skip any interation

# shopping_list = ["beef", "rice", "apple", "robot", "beans"]
# print(shopping_list)
#
# for items in shopping_list:
#     print(items)
#
# for items in shopping_list:
#     if items == "robot":
#         continue
#     print(items)

#
# directions = ['up', 'down', 'left', 'right']
#
# the_right_direction = ''  # if u don't make it empty, my while condition will be false & I can't enter the while loop.
# # the_right_direction will keep looping until I type anything from 'directions'
# while the_right_direction.lower() not in directions:  # the_right_direction is true
#     the_right_direction = input('Please, choose a direction where you wanna go: ')
#     if the_right_direction.lower() == 'quit':
#         print('The game is over')
#         break
# else:
#     print('I am glad I get out of here')




# you have to find those numbers, which are dividable by 7 and mulitple of 5 between the range 1500 4000

#for "and operation", and if

# for n in range(1500, 4000):
#     if n % 7 == 0 and n % 5 == 0:
#         print(n)

# you have to count the number of even and odd numbers from a list of numbers

# list = [5, 7, 10, 12, 15, 25, 37, 45, 49, 53, 67, 77, 99, 101]
# counter1 = 0
# counter2 = 0
# for n in list:
#     if n % 2 == 0:
#         counter1 += 1
#     else:
#         counter2 += 1
# print('The number of even numbers is {} and the number of odd number is {}'.format(counter1, counter2))

# you have to print all the numbers from a range 5-30 except 13, 17, 21

# for n in range(5, 31):
#     if n == 13 or n == 17 or n == 21:
#         continue
#     print(n)


# I need to print from a range the number and cube value of that number

# for y in range(2, 20):
#     print("The number is {} and the cube is {}".format(y, y*y*y))

# from a range 1 to 11 to find out the summation of the range

# counter = 0
# for x in range(1, 11):
#     counter += x
# print(counter)
#
# #calculate a sum of odd number up to 200
#
# counter = 0
# for x in range(1, 5): # 1 and 3 are the odd numbers in this range. 5 is not included. sni
#     if x % 2 != 0:
#         counter += x
# print(counter)
#
# #the sum of even numbers up to 95
#
# counter = 0
# for y in range(1, 5): # 2 and 4 are my even numbers
#     if y % 2 == 0:
#         counter += y
# print(counter)

# word = "Titanic" #tanic
# print(word[2:])
# print(word[6:1:-1])  # in order to print backwards I need to add -1 at the end
#
# print(word[0:7:3])  # last digit is my stepping value
# print(word[0::3])  # if I remove the middle part, than I don't have to count my index.

#you have to write a program using for loop, then you provide a word and the program will print the reversed word

# word = "apple"
# for w in range(4, -1, -1):
#     print(word[w])


# word = ((input("Please, enter your word: ")))
#
# for i in range(len(word)-1, -1, -1):
#     print(word[i])

#Given a list, iterate it, and display numbers divisible by five, and if you find a number greater than 150, stop the loop iteration.


# list= [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
#
# for i in list:
#     if i > 150:
#         break
#     if i % 5 == 0:
#         print("Number of {} is divisible by 5".format(i))

# list_of_fruits = ["banana", "apples", "grapes"]
# list_of_numbers = [1, 2, 3, 4, 5]
#
# print(list_of_numbers, list_of_fruits)
#
# for i in list_of_fruits:
#     print(i)
#
# print(list_of_fruits[0][2:])
#
# for i in list_of_fruits:
#     if i == "apples":
#         continue
#     print(i)


# number_list1 = [1, 2, 3, 4, 5, 6]
# number_list2 = [10, 7, 9, 11, 8]
#
# number_list1.extend(number_list2)
# print(number_list1)
#
# number_list1.sort()
# print(number_list1)
#
# number_list1.sort(reverse=True)
# print(number_list1)

#Removing High values and Low values

data=[4,5,6,104,110,120,135,145,155,165,175,185,195,350,380]

min_valid=100
max_valid=200

#Processing with lower values
stop=0
for index,value in enumerate(data): # enumerate iterating 2 things at the same
    if value>=min_valid:
        stop=index  # updating stop variable with the index value , which 3
        break
print(stop) # here it's printing 3 then we do slicing next line
del data[:stop] # we are deleting before stop point, which are 4, 5, and 6
print(data)

#Processing with Higher values

start=0 # len is how many items in my list
for index in range(len(data)-1,-1,-1):  # 1. len(data)-1 is my starting point, 2. ending point, 3. a stepping value
    if data[index]<=max_valid:  # we are going backwards from the last value which is 380 and we are going to 200 (line271)
        start=index+1 # because we want to keep 195 value, if I remove +1, 195 will be missing
        break
print(start)
del data[start:] # the start is 350, which does not count
print(data)































