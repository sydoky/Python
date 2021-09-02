import random


class Numbers:
    def __init__(self):
        self.number = []
        self.generate_numbers()

    def __str__(self):
        return str(self.number)

    def generate_numbers(self):
        for n in range(100):
            self.number.append(random.randint(1, 1000))

    def max_number(self):
        num = None
        for n in self.number:
            if num is None:
                num = n
            else:
                if n > num:
                    num = n
        return num

    def min_number(self):
        num = None
        for n in self.number:
            if num is None:
                num = n
            else:
                if n < num:
                    num = n
        return num

    def count_evens(self):
        count = 0
        for n in self.number:
            if n % 2 == 0:
                count += 1
        return count

    def all_evens(self):
        lis = []
        for n in self.number:
            if n % 2 == 0:
                lis.append(n)
        return lis

    def max_even_num(self):
        list_of_evens = self.all_evens()
        maxx = None
        for even_number in list_of_evens:
            if maxx is None:
                maxx = even_number
            else:
                if even_number > maxx:
                    maxx = even_number

        return maxx

    def count_one_digit_nums(self):
        counter = 0
        for n in self.number:
            if n < 10:
                counter += 1  # we need extra = for storing numbers
        return counter

    def two_digit_nums(self):
        counter = 0
        for n in self.number:
            if n >= 10 and n <= 99:
                counter += 1
        return counter

    def square_them_all(self):
        listt = []
        for n in self.number:
            listt.append(n ** 2)
        return listt

    def dividable_by_three(self):
        counter = 0
        for n in self.number:
            if n % 3 == 0:
                counter += 1
        return counter

    def dividable_by_three2(self):
        listttt = []
        for n in self.number:
            if n % 3 == 0:
                listttt.append(n)
        return listttt


random_number = Numbers()
print(random_number)

maximum = random_number.max_number()
print(maximum)
minimum = random_number.min_number()
print(minimum)

even_numbers = random_number.count_evens()
print(even_numbers)

my_even_numbers = random_number.all_evens()
print(my_even_numbers)

my_max_even_number = random_number.max_even_num()
print(my_max_even_number)

myzeroto10nums = random_number.count_one_digit_nums()
print(myzeroto10nums)

my_two_digit_nums = random_number.two_digit_nums()
print(my_two_digit_nums)

my_square_list = random_number.square_them_all()
print(my_square_list)

my_dividable_by_three = random_number.dividable_by_three()
print(my_dividable_by_three)

my_dividable_by_three_list = random_number.dividable_by_three2()
print(my_dividable_by_three_list)

#create a class word with strings, any words, one method that will return how many letters alphabet