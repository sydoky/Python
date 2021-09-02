# my_sentence = ("I love movie theater") # tuple
# my_sentence1 = set(my_sentence) #
# print(my_sentence1)
# my_vowels = ('aeiou')
# my_vowels1 = set(my_vowels)
#
# my_sentence1.difference_update(my_vowels1)
# print(my_sentence1)
# apple = sorted(my_sentence1, key=str.casefold) #sorted the upper and lower cases together otherwise if I don't use it the the upper case will always go first
# print(apple)

# print("------------")
#
# #first 3 lines is the same as 2 lines below
# # my_sentence = ("I love movie theater") # tuple
# # my_sentence1 = set(my_sentence) #
# # print(my_sentence1)
# my_sentence1 = set('I love movie theater') #this set will make them in unordered set
# print(my_sentence1)
#
# # my_vowels = ('aeiou')
# # my_vowels1 = set(my_vowels) line below is the same as these two lines
# my_vowels = set('aeiou')
#
# print(my_sentence1.difference(my_vowels)) #difference function will remove common values

# my_new_set = set([1, 2, 3, 4, 5, 'I love apples'])
# my_other_set = set([2, 3, 5, 7, 8, "I am away from the keyboard"])
# my_intersection = my_new_set.intersection(my_other_set) # intersection will look for common values
#
# apple = my_new_set & my_other_set
# print(my_intersection)
# print(apple)

# for i in my_new_set: #when I see iteration, it means I have to use a loop
#     print(i)

# my_new_set = set([1, 2, 3, 4, 5, 'I love apples'])
# my_other_set = set([2, 3, 5, 7, 8, "I am away from the keyboard"])
# my_print = my_new_set.union(my_other_set) #it will exclude any duplicates
# print(my_print)
#
# my_new_set = set([1, 2, 3, 4, 5, 'I love apples'])
# my_other_set = set([2, 3, 5, 7, 8, "I am away from the keyboard"])
# banana = my_new_set.difference(my_other_set) # it will show in display only unique values # the order matters here but not in symmetric
# print(banana)
#
# my_other_set = set([2, 3, 5, 7, 8, "I am away from the keyboard"])
# my_new_set = set([1, 2, 3, 4, 5, 'I love apples'])
# banana2 = my_other_set.difference(my_new_set) # it will show in display only unique values
# print(banana)
#
# my_new_set = set([1, 2, 3, 4, 5, 'I love apples'])
# my_other_set = set([2, 3, 5, 7, 8, "I am away from the keyboard"])
# rasberry = my_new_set.symmetric_difference(my_other_set) # it will always return identical difference and the order does not matter but it matters in difference
# print(rasberry)


# set1 = {1, 2, 5, 7, 10, 12}
# set2 = {2, 3, 5, 7}
# set3 = {10, 12, 14, 15, 17}
# set4 = {1, 2, 5}
#
# if set2.issubset(set1):
#     print("True")
# else:
#     print("False")
#
# if set4.issubset(set1):
#     print("True")
# else:
#     print("False")
#
# #Write a Python program to create a shallow copy of sets
#
# my_set = set3.copy()
# print(my_set)


# Write a Python program to remove all elements from a given set
#Write a Python program to use of frozensets


# my_set = {2, 5, 8, 9, 12, 13, 15}
# my_set.clear()
# print(my_set)
#
#
# orange = frozenset(range(1, 40, 2)) #frozenset is immutable
# print(orange)




# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number

# i is 100, 101, 102, 103 and so on

for i in range(100, 401):
    number = str(i)
    if (int(number[0]) % 2 != 0) and (int(number[1]) % 2 != 0) and (int(number[2]) % 2 != 0): #!=0 only will work with odd numbers
    # if (int(number[0]) % 2 == 1) and (int(number[1]) % 2 == 1) and (int(number[2]) % 2 == 1):
        print(i)





