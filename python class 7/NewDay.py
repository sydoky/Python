my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def function(num1):
    maxsofar = num1[0]
    for count in num1:
        if count > maxsofar:
            maxsofar = count
    print("This maximum is ", maxsofar)

function(my_list)


def minimum(num2):
    lesssofar = num2[0]
    for count in num2:
        if count < lesssofar:
            lesssofar = count
    print("The minimum is ", lesssofar)

minimum(my_list)


def count(num3, testnumber):
    greaterthan = 0
    for count in num3:
        if count > testnumber:
            greaterthan += 1
    print("There are ", greaterthan, " elements greater than ", testnumber)

count(my_list, 3)

def count5(num3):
    greaterthan5 = 0
    for count5 in num3:
        if count5 > 5:
            greaterthan5 += 1
    print("There are ", greaterthan5, " elements greater than 5")

count5(my_list)


def sum(numbers):
    sumsofar = 0
    for number in numbers:
        sumsofar += number
    print("The sum is ", sumsofar)

sum(my_list)


def average(numbers):
    thesumsofar = 0
    for number in numbers:
        thesumsofar += number
    theaverage = thesumsofar / len(numbers)
    print("The average number is", theaverage)

average(my_list)

