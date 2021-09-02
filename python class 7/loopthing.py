numbers = [700, 2, 3, 4, 5, 10, 20, 21, 23, 15, 111, 222, 333, 500, 650]
mxxnumber = None #none means I don't know which one is the highest yet
for n in numbers:
    if mxxnumber is None:
        mxxnumber = n #line 14 means 1st book, and line 15 we say it's the largest book
    else: #means it's not the first book
        if n > mxxnumber:  # this line means that the current book has more pages than the current max pages / cycle 2
            mxxnumber = n  # because of the previous line we change the max number of pages to match the # of pages the current book
            # line 17 & 18 we loop through everything else except first book
print(mxxnumber)

print("-------")
numbers = [700, 2, 3, 4, 5, 10, 20, 21, 23, 15, 111, 222, 333, 500, 650]
mxxnumber = None
for n in numbers:
    if mxxnumber is None:
        mxxnumber = n
    else:
        if n > mxxnumber:
            mxxnumber = n
#sum up odds and evens two task
print(mxxnumber)


print("-------")

numbers = [700, 2, 3, 4, 5, 10, 20, 21, 23, 15, 111, 222, 333, 500, 650, 9, 9]
even_numbers = 0
odd_numbers = 0
for n in numbers:
    if n % 2 == 0:
        even_numbers = even_numbers + n
    else:
        odd_numbers = odd_numbers + n
print(even_numbers)
print(odd_numbers)

print("---------")

odd_digits = 0
for n in numbers:
    if n % 2 == 1:
        if 10 <= n < 100:
        #if 10 <= n < 100 A simplier way to find the sum of odd digits
            odd_digits = odd_digits + n
print(odd_digits)

print("----")
#multiply all 3 even digit numbers

even_numbers = 1
for n in numbers:
    if n % 2 == 0:
        if 100 <= n < 1000:
            even_numbers = even_numbers * n
print(even_numbers)

print("-------")

#what is greater the sum of all 3 digit numbers or the product 1 digit numbers

three_digit = 0
one_digit = 1  # because we do multiplication we have to use 1, we cannot multiply #s by 0
for n in numbers:
    if n > 99 and n <1000:
        three_digit = three_digit + n
    if n < 10:
        one_digit = one_digit * n
if three_digit < one_digit:
    print("one digit product > sum")
    print(one_digit)
elif three_digit == one_digit:
    print("They are equal")
else:
    print("one digit product < sum")
    print(three_digit)

# are the numbers more dividable by 4 or by 3
numbers = [700, 2, 3, 4, 5, 10, 20, 21, 23, 15, 111, 222, 333, 500, 650, 9, 9]
dividable_three = 0 #because we count
dividable_four = 0
for n in numbers:
    if n % 3 == 0: #we set here if it's dividable by 3
        dividable_three = dividable_three + 1 #we count here
    if n % 4 == 0:
        dividable_four = dividable_four + 1
        #previous 5 lines we test the numbers

if dividable_three > dividable_four:
    print("We have more #s dividable by 3 than dividable by 4: ", dividable_three)
elif dividable_four > dividable_three:
    print("We have more #s dividable by 4 than dividable by 3: ", dividable_four)
else:
    print("We have equal numbers of 3 and 4")

print("--------------------")

numbers = [700, 2, 3, 4, 5, 10, 20, 21, 23, 15, 111, 222, 333, 500, 650, 9, 9]
dividable_three = 0 #because we count
dividable_four = 0
for n in numbers:
    if n % 3 == 0: #we set here if it's dividable by 3
        print("Dividable by 3 numbers are: ", n)
        dividable_three = dividable_three + 1 #we count here
    if n % 4 == 0:
        print("Dividable by 4 numbers are: ", n)
        dividable_four = dividable_four + 1

if dividable_three > dividable_four:
    print("We have more #s dividable by 3 than dividable by 4: ", dividable_three)
elif dividable_four > dividable_three:
    print("We have more #s dividable by 4 than dividable by 3: ", dividable_four)
else:
    print("We have equal numbers of 3 and 4")

print("-----------------------------------------------------------------------------")


class List_analyser:

    def __init__(self, lst):
        self.lst = lst
    def __str__(self):
        return str(self.lst)

    def counter(self):
        counter1 = 0
        for c in self.lst:
            counter1 = counter1 + 1
        return counter1

    def max(self):
        maxx = None #a piece of blank paper
        for n in self.lst:
            if maxx is None:
                maxx = n #this is the staring point
            elif n > maxx: #if the # of pages is greater on the current book
                maxx = n
        return maxx
    # the first "if" in for is the first book, "else" is for the all others.
    def minimum(self):
        mini = None #mini is a paper, None means a blank piece of paper
        for n in self.lst: # n is a number of pages of a current book[700, 2, 3...], lst is a shelf(полка с книгами) of books
            if mini is None: #we check if paper is blank meaning this is the first book, we are looking for the first book. A starting point of checking
                mini = n  #we write down the # of pages of the first book on the paper(because we don't have any other number to compare to, we cannot know about other books yet)
            else: #meaning it's not the first book and therefore we have a number on a paper , we don't know which book it is we just know it's not the first we look at
                if n < mini: #if the # of pages of the current book is lesser than the current minimum # of pages written on the paper.
                    mini = n # we write down the number of pages of the current book because in the previous line we found out that the number of pages of the current book is lesser than the current minimum written on the paper
        return mini #this is after the "for" that we finish checking all the books and we have the actual minimum which we return

    def aver(self): #here we combine our two methods (def) summ and count
        return self.sum() / self.counter()

    def sum(self):
        summ = 0
        for n in self.lst:
            summ = summ + n
        return summ

    def odds(self):
        newlist = []  # we need [] to add our numbers to it
        for n in self.lst:
            if n % 2 == 1:
                newlist.append(n)
        return newlist
    def max_odd(self): # combining odds and max
        odd_list = self.odds()  # creating the list only with odd numbers from the main list from method odds
        odd_object = List_analyser(odd_list)  # !!! creating a new object, which will contain only odd numbers in its own self list I have to create a helping object. Think about this line about odd_object !!!
        maximum = odd_object.max()  # finding the maximum number in the list of a new object
        return maximum
    def max_coolwayodd(self):
        return List_analyser(self.odds()).max() #max is a method above. however we would not do this way in real world
    def max_odd_loop(self):
        max_odd_number = None
        for n in self.lst:
            if max_odd_number is None:
                if n % 2 == 1:
                    max_odd_number = n #n is the number of pages
            elif max_odd_number < n:
                if n % 2 == 1:
                    max_odd_number = n
        return max_odd_number

    def even_numbers(self):
        even_list = []
        for n in self.lst:
            if n % 2 == 0:
                even_list.append(n)
        return even_list
    def min_even_number(self):
        smallest_even_number = None
        for n in self.lst:
            if smallest_even_number is None:
                if n % 2 == 0:
                    smallest_even_number = n
            elif smallest_even_number > n:
                if n % 2 == 0:
                    smallest_even_number = n
        return smallest_even_number

    def coolest_even_minimum(self):
        return List_analyser(self.even_numbers()).minimum()

    def even_minimum_number(self):
        even_min_num = self.even_numbers()
        even_num = List_analyser(even_min_num)
        minimum = even_num.minimum()
        return minimum





l = List_analyser([700, 2, 3, 4, 5, 10, 20, 21, 23, 15, 111, 222, 333, 500, 650, 9, 9])
print(l)
print(l.counter())
print(l.max())
print(l.minimum())
print(l.sum())
print(l.aver())
print(l.odds())
print(l.max_odd())
print(l.max_coolwayodd())
print("-------")
print(l.max_odd_loop())
print(l.even_numbers())
print(l.min_even_number())
print(l.coolest_even_minimum())
print(l.even_minimum_number())














