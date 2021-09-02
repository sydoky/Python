# data=[1,23,46,36,3,4,576,4667,456,783774,63663,8884747,663,7387763,536,893898734,2626,92,300,500,700,200,250,300,150]
#
# low = 200
# high = 2000
#
# for index in range(len(data)-1, -1, -1):
#     if data[index] < low or data[index] > high:
#         print(index, data[index])
#         del data[index]
# print(data)
#
# data=[104,101,4,105,308,103,5,107,100,306,106,210]
#
# min_value = 100
# max_value = 200
#
# top_index = len(data)-1 # we use actually to get a real index value
#
# for index,value in enumerate(reversed(data)):
#     if value < min_value or value > max_value:
#         print(top_index-index,value)
#         del data[top_index-index]
# print(data)


# #Nested list
# countries = [["Bangladesh", "Russia", "USA"],
#             ["Italy", "Germany", "Spain"],
#              ["China", "Japan", "Vietnam"]]
#
# for i in countries:
#     for e in i:
#         print(e)
#
# for a in range(len(countries)-1, -1, -1):
#     for h in countries:
#         for g in h:
#             print(g)
#
# for k in countries:
#     for q in range(len(k)-1, -1, -1):
#         if k[q] == "Spain":
#             del k[q]
#     print(k)

# countries = ["Bangladesh", "Russia", "USA", "Italy", "Germany", "Spain", "China", "Japan", "Vietnam"]
#
# print(countries)
#
# separated = ", "
#
# my_cool_countries = separated.join(countries)
#
# print(my_cool_countries)
#
# print(my_cool_countries[12:18])

# albums=[("Welcome to my Nightmare","Alice Cooper",1975),
#         ("Bad Company","Bad Comp",1974),
#         ("Ride the Lighting","Metalica",1984)
# ]
#
# for i in albums:
#     print("Album: {}, Artist: {}, Year: {}".format(i[0], i[1], i[2]))

# albums=[
#     ("WELCOME TO MY NIGHTMARE","Alice cooper",1975,
#      [
#          (1,"Welcome to my Nightmare"),
#          (2,"Devils Food"),
#          (3,"The Black widow")
#
#      ]
#      ),
#     ("Bad Company","Bad",1974,
#      [
#          (1,"Can't get enough"),
#          (2,"Rock Steady"),
#          (3,"Ready for Love")
#      ])]
#
# tupl=albums[0]
# print(tupl)
# artist = tupl[1]
# print(artist)
# song_name = tupl
# print(song_name)
# print("__________________")
# song_name = tupl[3]
# print(song_name)
# print('--------------')
#
# song = song_name[2]
# print(song)
# print(song[1])

# introduction to function

# function is going to help up to reduce lines of codes in our project
# we create a function that we can use it every time whatever we need


# def multi(num1, num2): #those are parameters
#     return num1 + num2, num1 - num2, num1 * num2, num1 / num2
# num1 = 10
# num2 = 15
#
# c = multi(num1, num2) # those two are arguments
# print(c)
# #we have two ways up and down
#
# print(multi(5, 12)) # those two are arguments
# You can use numeric string or any types of variables as your argument

# Program flow when calling a function from the bottom to up
#
#
# def Palindrome(w):
#     backward = w[::-1]
#     return backward.casefold() == w.casefold()

# word = input("Please enter your word: ")
# if Palindrome(word):
#     print("{} is a palindrome".format(word))
# else:
#     print("{} is not a palindrome".format(word))
#
#     print("--------")
#
# def Palindrome_two(w):
#     string = ""
#     for i in w: # 'w' is a sentence provided by us, 'i' will interate each character of the sentence
#         if i.isalnum(): # Y line 131 first letter will be checked. If it's true, it will be stored in next line in string variable
#             string += i #all my characters will be stored in this variable.
#     print(string)
#     return string[::-1].casefold() == string.casefold()
#
# sentence = input("Please enter your sentence: ")
# if Palindrome_two(sentence):
#     print("{} is a palindrome sentence".format(sentence))
# else:
#     print("{} is not a palindrome sentence".format(sentence))
#
# print("---------------")

# def Palindrome_two(w):
#     string = ""
#     for i in w: # 'w' is a sentence provided by us, 'i' will interate each character of the sentence
#         if i.isalnum(): # Y line 131 first letter will be checked. If it's true, it will be stored in next line in string variable
#             string += i #all my characters will be stored in this variable.
#     print(string)
#     return Palindrome(string)
#
# sentence = input("Please enter your sentence: ")
# if Palindrome_two(sentence):
#     print("{} is a palindrome sentence".format(sentence))
# else:
#     print("{} is not a palindrome sentence".format(sentence))

# Returning Values
# import random
#
# def get_integer(prompt):
#     while True:
#         temp=input(prompt)
#         if temp.isnumeric():
#             return int(temp)
#
# answer=random.randint(1,100)
# guess=0
#
# while guess!=answer:
#
#     print("Please enter a number")
#
#     guess=get_integer("Enter The guess: ")
#
#     if guess==answer:
#         print("Congratz")
#         break
#     else:
#         if guess<answer:
#             print("Increase")
#         else:
#             print("Lower")


# Fibonacci Numbers

def Fibonacci_Misha(n):  # n=4 is the index of 3

    if 0 <= n <= 1:  # only 0 and 1 will not be looped
        return n  # 4 is false here

    n_minus1, n_minus2 = 1, 0
    result = None

    for f in range(n - 1):  # n-1 (4-1=3 this means my loop can interate 3 times)
        result = n_minus2 + n_minus1  # 1 step loop: 0 +1 = 1 , the result is 1; 2 step loop: n_minus_2 = 1 + n_minus_1 = 1, the result = 2. 3. step loop: n_minus2 is 1 + n_minus1 is 2 = the result is 3
        n_minus2 = n_minus1  # 1. step loop: n-2, which is 0, = 1 now we are updating to the value of n_minus2 with value of n_minus1 which is 1; 2 step loop: n_minus1 = 1 ; 3 step loop n-minus1 is 2
        n_minus1 = result  # 1. step loop: n_minus1 which is 1 = result 1 this whole loop will be interated 3 times. 2. step loop: now we are updating n_minus1 with the value of result which is 2 . 3 step loop n-minus1 becomes 3

        # left side is variable = right side is value. The left side will be always updated based on the right side activities

    # as long as my condition in the loop is true, it will be iterated

    return result  # the result is 3


#
# for i in range(0,12):
#     print(i,Fibonacci_Misha(i))

for i in range(0, 12):
    print(i, Fibonacci_Misha(i))
