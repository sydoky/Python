colors = ["green", "blue", "red", "black", "white"]

all_colors = ""
for c in colors:
    all_colors += c + ", "
print(all_colors)

print("----------")


# we have 5 books. you take 2 and me take 2 and 1 one left that is what is module %
# line 16 we check if the number is odd
numbers = [700, 2, 3, 4, 5, 10, 20, 21, 23, 15, 111, 222, 333, 500, 650]

mxxnumber = None #none means I don't know which one is the highest yet
for n in numbers:
    if mxxnumber is None:
        if n % 2 == 1:  # we use %(module) of 2 to check if # is odd (if it's dividable by 2), ==1 means remainder of division by 2
            mxxnumber = n #line 14 means 1st book, and line 15 we say it's the largest book
    else: #means it's not the first book
        if n % 2 == 1:
            if n > mxxnumber:  # this line means that the current book has more pages than the current max pages / cycle 2
                mxxnumber = n  # because of the previous line we change the max number of pages to match the # of pages the current book
            # line 17 & 18 we loop through everything else except first book
print(mxxnumber)

print("---------")

mxxnumber = None #none means I don't know which one is the highest yet
for n in numbers:
    if mxxnumber is None:
        if n % 2 == 0:
            mxxnumber = n #line 14 means 1st book, and line 15 we say it's the largest book
    else: #means it's not the first book
        if n % 2 == 0:
            if n > mxxnumber:  # this line means that the current book has more pages than the current max pages / cycle 2
                mxxnumber = n  # because of the previous line we change the max number of pages to match the # of pages the current book
            # line 17 & 18 we loop through everything else except first book

print("-------")

mxxnumber = None #none means I don't know which one is the highest yet
for n in numbers:
    if mxxnumber is None:
        mxxnumber = n #line 14 means 1st book, and line 15 we say it's the largest book
    else: #means it's not the first book
        if n > mxxnumber:  # this line means that the current book has more pages than the current max pages / cycle 2
            mxxnumber = n  # because of the previous line we change the max number of pages to match the # of pages the current book
            # line 17 & 18 we loop through everything else except first book
print(mxxnumber)

print("---------")



numbers = max(1, 2, 3, 4, 5, 10, 20, 21, 23, 15, 111, 222, 333, 500, 650)
print(numbers)


numbers = min(1, 2, 3, 4, 5, 10, 20, 21, 23, 15, 111, 222, 333, 500, 650)
print(numbers)

numbers = (1, 2, 3, 4, 5, 10, 20, 21, 23, 15, 111, 222, 333, 500, 650)
numbers.index(2)
print(numbers)

print("-------")
#we check if # is dividable by 5 the highest # and all we do is changing sedond "if"
mxxnumber = None #none means I don't know which one is the highest yet
for n in numbers:
    if mxxnumber is None:
        if n % 5 == 0:
            mxxnumber = n #line 14 means 1st book, and line 15 we say it's the largest book
    else: #means it's not the first book
        if n % 5 == 0:
            if n > mxxnumber:  # this line means that the current book has more pages than the current max pages / cycle 2
                mxxnumber = n  # because of the previous line we change the max number of pages to match the # of pages the current book
            # line 17 & 18 we loop through everything else except first book
print(mxxnumber)

#how to find 2 highest numbers and they cannot be equal, all different numbers.

print("-------")




numbers2 = [700, 2, 3, 4, 5, 10, 20, 21, 23, 15, 111, 222, 333, 500, 650]
mxxnumber1 = None
mxxnumber2 = None
for n in numbers2:
    if mxxnumber1 is None and mxxnumber2 is None:
            mxxnumber1 = n
            mxxnumber2 = n

    if mxxnumber1 == mxxnumber2:
        mxxnumber2 = n
    if n > mxxnumber1:
        mxxnumber2 = mxxnumber1
        mxxnumber1 = n
    if n > mxxnumber2:
        if n != mxxnumber1:
            mxxnumber2 = n

print(mxxnumber1, mxxnumber2)

print("-------")
import datetime
print(datetime.datetime.now())
for n in range(1000000):

    numbers2 = [700, 2, 3, 4, 5, 10, 20, 21, 23, 15, 111, 222, 333, 500, 650]
    mxxnumber1 = None
    mxxnumber2 = None
    mxxnumber3 = None
    for n in numbers2:
        if mxxnumber1 is None:
                mxxnumber1 = n
        elif mxxnumber2 is None:
            if n > mxxnumber1:
                mxxnumber2 = mxxnumber1
                mxxnumber1 = n
            else:
                mxxnumber2 = n
        elif mxxnumber3 is None:
            if n > mxxnumber2:
                if n > mxxnumber1:
                    mxxnumber3 = mxxnumber2
                    mxxnumber2 = mxxnumber1
                    mxxnumber1 = n
                else:
                    mxxnumber3 = mxxnumber2
                    mxxnumber2 = n

            else:
                mxxnumber3 = n

        elif n > mxxnumber1:
            mxxnumber3 = mxxnumber2
            mxxnumber2 = mxxnumber1
            mxxnumber1 = n
        elif n > mxxnumber2:
            mxxnumber3 = mxxnumber2
            mxxnumber2 = n
        elif n > mxxnumber3:
            mxxnumber3 = n

print(datetime.datetime.now())

print(mxxnumber1, mxxnumber2, mxxnumber3)
print(datetime.datetime.now())
for n in range(1000000):



    numbers2 = [700, 2, 3, 4, 5, 10, 20, 21, 23, 15, 111, 222, 333, 500, 650]
    mxxnumber1 = None
    mxxnumber2 = None
    mxxnumber3 = None
    for n in numbers2:
        if mxxnumber1 is None:
            mxxnumber1 = n
        else:
            if mxxnumber1 < n:
                mxxnumber1 = n
    for n in numbers2:
        if mxxnumber2 is None:
            if n != mxxnumber1: #for num 2 we added this line
                mxxnumber2 = n #we pushed one time inside this line
        else:
            if mxxnumber2 < n:
                if n != mxxnumber1:
                    mxxnumber2 = n
    for n in numbers2:
        if mxxnumber3 is None:
            if n != mxxnumber1 and n != mxxnumber2: #for num 3 we added this line
                mxxnumber3 = n #we pushed one time inside this line
        else:
            if mxxnumber3 < n:
                if n != mxxnumber2 and n != mxxnumber1:
                    mxxnumber3 = n

print(datetime.datetime.now())
print(mxxnumber1, mxxnumber2, mxxnumber3)

#sum up odds and evens two task