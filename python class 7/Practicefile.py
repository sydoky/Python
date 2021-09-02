import numpy as np

'''n = int(input("Enter your a and b numbers: "))
x = int(input("Enter number X: "))
counter = 0
#loop from 0 to z
for numbers in range(1, n + 1):
    if numbers % x == 0:
        counter += 1
print(counter)'''



# input a and b and find odd numbers between a and b.
# input a, b, c and see even numbers between a and b, and odd numbers b and c.
'''
a = int(input("Enter your first number: "))
b = int(input("Enter your second number and it has to be higher than your previous number: "))
c = int(input("Enter your 3rd number: "))
counter = 0
counter2 = 0
for numbers in range(a, b + 1):  # in range always the second thing has to be with + cause range look only at 1 one

    if numbers % 2 == 0:
        counter += 1
for o in range(b, c + 1):
    if o % 2 == 1: #  % 2 == 1 for odd numbers
        counter2 += 1
if counter > counter2:
    print("More even numbers between a & b than between b & c")
else:
    print("More odd numbers between c & b than between a & b")
'''

numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def odd_numbers(num):
    odd_list = []
    for n in num:
        if n % 2 == 1:
            odd_list.append(n)
    return odd_list


print(odd_numbers(numbers))

def dividable_by_three(num2):
    list_three = []
    for nums in num2:
        if nums % 3 == 0:
            list_three.append(nums)
    return list_three

print(dividable_by_three(numbers))

#dividable by 5 and not by 3

def dividable_by_5(num3):
    list_five = []
    for nu in num3:
        if nu % 5 == 0:
            if nu % 3 != 0:
                list_five.append(nu)
    return list_five
print(dividable_by_5(numbers))


def dividable_by_5(num3):
    list_five = []
    for nu in num3:
        if nu % 5 == 0:
            if not nu % 3 == 0:
                list_five.append(nu)
    return list_five
print(dividable_by_5(numbers))


string = "I ran 2.1 miles for 30 minutes at 9:45am"

def counting_numbers(strings):
    counting = 0
    for c in strings:
        if c.isnumeric():
            print(c)


print(counting_numbers(string))

#for hw find the minimum and the maximum numbers.

def maximum_num(string):
    maxx = 0
    for mn in string:
        if mn.isnumeric():
            if int(mn) > maxx:
                maxx = int(mn)
    return maxx
print(maximum_num(string))

def minumum_num(string):
    minn = 0
    for mn in string:
        if mn.isnumeric():
            if int(mn) < minn:
                minn = int(mn)
    return minn
print(minumum_num(string))

my_newlist = [1, 2, 3, 4, 5, 6, 7, 8, 9.9, "a"]
my_array = np.array(my_newlist)
print(my_newlist)
print(my_array)
print(type(my_newlist))
print(type(my_array))
a = my_array[0]
b = my_newlist[0]
print(type(a), type(b))


