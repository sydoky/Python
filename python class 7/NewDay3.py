def function(orange, apple):
    return orange + apple

print(function(3, 7))

def fun(grape, peach):
    return grape * peach

print(fun(2, 6))

def arguments(bear, wolf):
    if bear > wolf:
        return bear
    if wolf > bear:
        return wolf
print(arguments(3, 7))

def funct(list1):
    numbers = []
    for loop in list1:
        if loop % 2 == 0:
            numbers.append(loop)
    return numbers
print(funct([3, 4, 5, 6, 7, 8]))

def element(world):
    number = []
    for loop in world:
        if loop % 2 == 1 and loop > 5:
            number.append(loop)
    return number
print(element([1, 2, 3, 4, 6, 7, 8, 10, 12, 15, 17, 18]))

def newlist(list1, list2):
    number = []
    for loop in list1:
        if loop % 2 == 1:
            number.append(loop)
    for loop in list2:
        if loop % 2 == 0:
            number.append(loop)
    return number

print(newlist([1, 2, 3, 4, 5, 6, 7, 8, 9], [21, 21, 22, 23, 25, 27, 28, 30, 32]))


def anewlist(yoyo):
    number = []
    highest = None
    for loop in yoyo:
        if highest == None:
            if loop % 2 == 1:
                highest = loop

        elif loop % 2 == 1 and loop > highest:
            highest = loop
    lowest = None
    for loop in yoyo:
        if lowest == None:
            if loop % 2 == 0:
                lowest = loop
        elif loop % 2 == 0 and loop < lowest:
            lowest = loop
    number.append(highest)
    number.append(lowest)
    return number

print(anewlist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


























