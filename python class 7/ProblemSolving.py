#Write a Python function to find the Max of three numbers.

#I can provide as a list of numbers or I can provide individual numbers

# def max_numbers(num):
#     return max(num)
#
# list_of_numbers = [3, 5, 7]
#
# answer=max_numbers(list_of_numbers)
#
# print(answer)
#
#
# print('-------------')

#individual numbers

#
# def max_numbers(*args):
#     return max(args)
#
# answer=max_numbers(7, 9, 12)
#
# print(answer)
#
#
# print('------------')
#Write a Python function to sum all the numbers in a list.

# def sum1(nums):
#     summation = 0
#     for i in nums:
#         summation += i
#     return summation
#
#
# list_of_numb = [8, 2, 3, 0, 7]
# answer1 = sum1(list_of_numb)
#
# print(answer1)
#
# print('-------------')
#Write a Python function to multiply all the numbers in a list.
# def sum1(nums):
#     summation = 1
#     for i in nums:
#         summation *= i
#     return summation
#
#
# list_of_numb = [8, 2, 3, -1, 7]
# answer1 = sum1(list_of_numb)
#
# print(answer1)

# Write a Python program to reverse a string.  "1234abcd"

# def reverse_way(words):
#     return words[::-1]


# word = '1234abcd'
# answer2 = reverse_way(word)
# print(answer2)
# #dcba4321
# print('---------')
# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

# def factorial_number(num):
#     if num == 1:
#         return num
#     else:
#         return num * factorial_number(num-1)
#
# fact_num = factorial_number(5)
# print(fact_num)
#
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("Input a number to compute the factiorial : "))
# print(factorial(n))

print('-------------')

#Write a Python function to check whether a number falls in a given range.
#
# def my_range(num):
#     if num in range(1, 6):
#         print("You got the number")
#     else:
#         print("What a heck!")
# my_range(7)

# def test_range(n):
#     if n in range(3,9):
#         print( " %s is in the range"%str(n))
#     else :
#         print("The number is outside the given range.")
# test_range(5)

# print('-----------')

#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

# def character(sentence):
#     counter1 = 0
#     counter2 = 0
#     for i in sentence:
#         if i.isupper(): #isupper will check the character is upper case or not
#             counter1 += 1
#         elif i.islower():
#             counter2 += 1
#     print("The number of upper case characters are {} and the number of lower case characters are {}".format(counter1, counter2))
#
# character("The quick Brow Fox")

# Write a Python function that takes a list and returns a new list with unique elements of the first list. Go to the editor
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

# def filter(list):
#     return set(list)
# my_answer = filter([1,2,3,3,3,3,4,5])
# print(my_answer)
# new_answer = list(my_answer)
# print(new_answer)

# def unique_list(l):
#   x = []
#   for a in l:
#     if a not in x:
#       x.append(a)
#   return x
#
# print(unique_list([1,2,3,3,3,3,4,5]))


#Write a Python function that takes a number as a parameter and check the number is prime or not. Go to the editor
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
#Prime number is divisable by 1 and itself such as 2, 3, 5, 7, 11, 13, 17, etc

#this function is not working properly
# def prime_number(prime):
#     if prime==1:
#         print("{} is not a prime number".format(prime))
#     elif prime==2:
#         print("{} is a prime number".format(prime))
#     else:
#         for i in range(2, prime//2): #we provide 2 to check if a number is divisable
#             if prime%i==0:
#                 print("{} is not a prime number".format(prime))
#         print("{} is a prime number".format(prime))
#
# prime_number(9)

# def prime_number(num):
#     if num>1:
#         for i in range(2, num): #2 means we start from 2 for checking because we don't need to check with 1
#             if num%i==0: #suppose the num is 9
#                 # 9 / 2 = not true, then 9 / 3 = becomes true
#                 # 5 / 2 = not true, loop again 5 / 3 = not true, 5 / 4 = not true, then it will directly go to else
#                 print("{} is not a prime number".format(num))
#                 break
#         else:
#             print("{} is a prime number".format(num))
#     else:
#         print("{} is not a prime number".format(num))
#
# prime_number(9)

# Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

# def even_nums(num):
#     numbers = []
#     for i in num:
#         if i%2==0:
#             numbers.append(i)
#     print(numbers)
#
# even_nums([1, 2, 3, 4, 5, 6, 7, 8, 9])

#Perfect Numbers
#6 is a perfect number
#1,2,3  are divisors of 6
#if 1+2+3=6  ,6 is a perfect number
#The number is 28
#1,2,4,7,,14
#the summation of divisors,1+2+4+7+14= 28
#28 is a perfect number

# def perfect(num):
#     divisors=[]
#     for i in range(1,num):
#         if num%i==0: #To find out the divisor #5 is my number. 1. num is 5 % 1 == 0     2) 5 % 2 == 0. This cannot enter into if statement. 3) 5 % 3 == 0       4) 5 % 4 == 0.  Our last digit is always excluded
#             divisors.append(i) # one will be added to the list.  step 2 cannot come here. step 3 cannot come here too. step 4 cannot come come here
#     sum1=sum(divisors)
#
#     if sum1==num:
#         print("{} is a perfect number".format(num))
#     else:
#         print("{} is not a perfect number.".format(num))
#
# perfect(5)
#Write a Python function that checks whether a passed string is palindrome or not. Go to the editor
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

# def palindrome(w):
# #     backwards = w[::-1]
# #     return w.casefold() == backwards.casefold()
# #
# #
# # word = input('Please, enter your word to check if its a palindrome: ')
# #
# # if palindrome(word):
# #     print("{} is a palindrome".format(word))
# # else:
# #     print('{} is not a palindrome'.format(word))


#
# Write a Python function to check whether a string is a pangram or not. Go to the editor
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"


# def cheking_pangram(s):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for c in alphabet:
#         if c not in s.casefold():
#             return False
#     else:
#         return True
#
# # sentence = "The quick brown fox jumps over the lazy dog"
# sentence = "I want to sleep now"
#
# if cheking_pangram(sentence)==True:
#     print("This is a pangram sentence")
# else:
#     print("This is not a pangram sentence")


# def pangram(s):
#     alphabet="abcdefghijklmnopqrstuvwxyz"
#     for c in alphabet:
#         if c not in s.casefold():
#             return False
#     return True
#
#
#
# sent="The quick brown fox jumps over the lazy dog"
# # sent="My name Pavel"
#
# if pangram(sent)==True:
#     print("This is a Pangram")
# else:
#     print("This is not a pangram")


# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

# input="green-red-yellow-black-white"
# list = input.split("-")
# print(list)
# list.sort()
# print(list)
# output = "-".join(list)  #'-' is called hypen . In the U.S. they call it dash
# print(output)


# items=[n for n in input().split('-')]
# items.sort()
# print('-'.join(items))
#
# Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).

#
# def square(num):
#     list = []
#     list2 = []
#     for i in range(1, num):
#         list.append(i)
#     print(list)
#     for j in list:
#         list2.append(j**2) #you can write (j*j) instead of (j**2)
#     print(list2)
# square(31)
#
#
# def printValues():
#     l = list()
#     for i in range(1, 21):
#         l.append(i ** 2)
#     print(l)
#
# printValues()

# Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python.

# mycode = 'print("hello world")'
# code = """
# def mutiply(x,y):
#     return x*y
#
# print('Multiply of 2 and 3 is: ',mutiply(2,3))
# """
# exec(mycode)
# exec(code)
#
# my_new_code = 'print("Hello Misha and Pavel")'
# code2 = '''
# def sum(x, y):
#     return x+y
# print('Summation of 5 and 7 is ', sum(5, 7))
# '''
# exec(my_new_code)
# exec(code2)


# Write a Python program to access a function inside a function

# def my_function(f):
#     def my_function2(m):
#         return m * f
#     return my_function2
#
# fruit=my_function(3)
# fruit2 = fruit(5)
# print(fruit2)

# Write a Python program to detect the number of local variables declared in a function
#global variables = you can use them everywhere, local variables = they are declared inside the function
# Sample Output:
# 3

def my_variables():
    fruits = "apple"
    vegetable = "tomato"
    weight = 7
print(my_variables.__code__.co_nlocals)

# Write a Python program that invoke a given function after specific milliseconds.
# Sample Output:
# Square root after specific miliseconds:
# 4.0
# 10.0
# 158.42979517754858

from time import sleep
import math
def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
print("Square root after specific miliseconds:")
print(delay(lambda x: math.sqrt(x), 100, 16))
print(delay(lambda x: math.sqrt(x), 1000, 100))
print(delay(lambda x: math.sqrt(x), 2000, 25100))





